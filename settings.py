# -*- coding: utf-8 -*-

import os

#REPO_NAME = "Facker-Blog"
BEBUG = True

APP_DIR = os.path.dirname(os.path.abspath(__file__))


def parent_dir(path):
    """ Return the parent of a directory """
    return os.path.abspath(os.path.join(path, os.pardir))


PROJECT_ROOT = parent_dir(APP_DIR)
FREEZER_DESTINATION = PROJECT_ROOT
FREEZER_BASE_URL = "http://localhost/"#.format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'



