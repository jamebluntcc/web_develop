# coding=utf-8

import os

DEBUG = True
DB_NAME = 'dev.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), DB_NAME)
UPLOAD_FOLDER = '/tmp/permdir'
SQLALCHEMY_TRACK_MODIFICATIONS = False
