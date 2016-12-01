import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MyFeeling(models.Model):
    class Meta:
        db_table = 'my_feeling'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    morning = models.IntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    afternoon = models.IntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    evening = models.IntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]
    )

    after_breakfast = models.IntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    after_lunch = models.IntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    after_dinner = models.IntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]
    )

    grade = models.CharField(max_length=10, default='NORMAL', null=False)

    created_date = models.DateField(null=True)
    updated_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):

        super(MyFeeling, self).save(*args, **kwargs)
