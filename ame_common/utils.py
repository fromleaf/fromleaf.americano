# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


def read_file_from_local(path, file):
    if path[len(path) - 1] != '/':
        path += '/'

    try:
        file_path = path + file
        read_file = open(file_path, 'r')

        return read_file

    except OSError as e:
        logger.error(e)