#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import config
import logging
import os
import webapp2

from base_handler import BaseHandler
from webapp2_extras import jinja2
from webapp2_extras import i18n

from google.appengine.ext.webapp import template


### More detail:
### http://webapp-improved.appspot.com/_modules/webapp2_extras/jinja2.html
session_config = {}
session_config['webapp2_extras.sessions'] = {
    'secret_key': config.SESSION_SECRET_KEY,
    'cookie_name': config.SESSION_COOKIE_NAME,
}
session_config['webapp2_extras.jinja2'] = {
    'template_path': config.I18N_TEMPLATE_PATH,
    'environment_args': config.I18N_ENV_ARGS,
    'globals': config.GLOBALS_SET,
}


class MainPage(BaseHandler):
  def get(self):
    locale = self.session.get('locale')
    
    if not locale:
      locale = 'zh_TW'
    
    i18n.get_i18n().set_locale(locale)
    template_dict = {'locale':locale}
    self.render_template('index.html', template_dict)


class SetLocale(BaseHandler):
  def get(self, locale):
    self.session['locale'] = locale
    self.redirect('/')


app = webapp2.WSGIApplication([
  	('/', MainPage),
  	('/set/locale/(.*)', SetLocale),],
  	debug=True, config=session_config)
