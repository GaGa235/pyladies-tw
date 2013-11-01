#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The base request handler class.
reference
webapp2 http://webapp-improved.appspot.com/index.html
session http://webapp-improved.appspot.com/api/webapp2_extras/sessions.html
"""
import json
import logging
import webapp2

from webapp2_extras import sessions
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):

  def dispatch(self):
    # Get a session store for this request.
    self.session_store = sessions.get_store(request=self.request)

    try:
      # Dispatch the request.
      webapp2.RequestHandler.dispatch(self)
    finally:
      # Save all sessions.
      self.session_store.save_sessions(self.response)

  @webapp2.cached_property
  def session(self):
    # Returns a session using the default cookie key.
    return self.session_store.get_session()

  @webapp2.cached_property
  def jinja2(self):
    return jinja2.get_jinja2(app=self.app)

  #render template
  def render_template(self, filename, template_args={}):
      self.response.write(self.jinja2.render_template(filename, **template_args))

  #render json
  def render_json(self, response):
    if self.request.GET['callback']:
      self.response.write("%s(%s);" % (self.request.GET['callback'], json.dumps(response)))
    else:
      self.response.write("%s" % json.dumps(response))

  #for debug usage
  def debug(self, data):
    pass

  #render get uuid
  def get_user_id(self):
    pass

  # locate
  def locale(self, locale_data=None):
    session = self.session_store.get_session()
    #session['locale'] = 'en_US'
    locale_from_session = session.get('locale')
    logging.info('EEEEEE:%s', locale_from_session)

    if locale_data:
      return locale_data

    else:
      return locale_from_session
