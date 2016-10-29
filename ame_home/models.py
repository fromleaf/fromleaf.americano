# -*- coding: utf-8 -*-

from django.db import models


class About(models.Model):
    class Meta:
        db_table = 'about'

    desc1 = models.CharField(max_length=255)
    desc2 = models.CharField(max_length=255)
    desc3 = models.CharField(max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)


class SkillSet(models.Model):
    class Meta:
        db_table = 'skill_set'

    title = models.CharField(max_length=150)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)


class Skill(models.Model):
    class Meta:
        db_table = 'skill'

    skill_set = models.ForeignKey(SkillSet, db_constraint=False,
                               related_name='skill_set', null=True)

    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=1024, null=True)
    grade = models.IntegerField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)


class Company(models.Model):
    class Meta:
        db_table = 'company'

    name = models.CharField(max_length=150)
    desc = models.CharField(max_length=255, null=True)
    what_do_i_1 = models.CharField(max_length=255, null=True)
    what_do_i_2 = models.CharField(max_length=255, null=True)
    what_do_i_3 = models.CharField(max_length=255, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)


class Project(models.Model):
    class Meta:
        db_table = 'project'

    title = models.CharField(max_length=150, null=True)
    desc = models.CharField(max_length=1024, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)


class CompanyProjectRelation(models.Model):
    class Meta:
        db_table = 'company_and_project_relation'

    company = models.ForeignKey(Company, null=True)
    project = models.ForeignKey(Project, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)
