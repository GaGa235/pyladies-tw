#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Holds configuration settings """
SESSION_SECRET_KEY = '@#$ER12348736ABCdefgZ*&^'
SESSION_COOKIE_NAME = 'pyladies-tw'


""" i18n """
I18N_TEMPLATE_PATH = 'templates'
I18N_ENV_ARGS = {'extensions': ['jinja2.ext.i18n']}


""" jinja2 globals """
GLOBALS_SET = {'zip': zip}