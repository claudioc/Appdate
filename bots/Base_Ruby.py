#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Base_Ruby(AppdateHTTPRetriever):
  """Ruby BOT"""
  
  def _run(self, target):
    ##
    # Current Version
    ##
    self.sniffer.setBaseUrl('http://svn.ruby-lang.org/repos/ruby/tags')
    self.sniffer.setTargetPath('/')
    data = self.sniffer.setTargetPattern("""<li><a href=".*?\/">v(%s_\d+_\d+)\/<\/a><\/li>""" % target).run(mode=FIND_ALL)
  
    if not data:
      self.say('Unable to retrieve version')
      return KO
    
    versionTag = data[-1]

    self.set('currentVersion', versionTag.replace('_','.'))

    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl', "http://svn.ruby-lang.org/repos/ruby/tags/v%s/ChangeLog" % versionTag)

    ##
    # Release Date
    ##
    self.set('releaseDate', '')

    ##
    # Download URL
    ##
    self.set('downloadUrl', "ftp://ftp.ruby-lang.org/pub/ruby/%s/" % target.replace('_','.'))
    return OK


