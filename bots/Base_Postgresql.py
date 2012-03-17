#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Base_Postgresql(AppdateHTTPRetriever):
  """Postgresql BOT"""
  
  def _run(self, target):
    ##
    # Current Version
    ##
    self.sniffer.setBaseUrl('http://www.postgresql.org')
    self.sniffer.setTargetPath('/')
    data = self.sniffer.setTargetPattern("""<b>(%s\.\d+\.\d+)<\/b>""" % target).run(mode=FIND_ALL)
  
    if not data:
      self.say('Unable to retrieve version')
      return KO
      
    self.set('currentVersion', data[0])

    ##
    # Release Notes and Release date
    ##
    data = self.sniffer.setTargetPattern("""<b>%s<\/b>\s+&middot;\s+(.*)\s+&middot;\s+<a href="(.*?)">""" % self.get('currentVersion')).run()

    if data is not None:
      self.set('releaseDate', data.group(1).strip())
      self.set('releaseNotesUrl', "http://www.postgresql.org%s" % data.group(2).strip())

    self.set('downloadUrl', 'http://www.postgresql.org/download/')
    
    return OK

