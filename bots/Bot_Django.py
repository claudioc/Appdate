#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_Django(AppdateHTTPRetriever):
  """Django BOT"""
  
  def identify(self):
    return {
      'runnable': True,
      'projectGroup': 'Django',
      'projectName': 'Django',
      'projectDescription': 'The web framework for perfectionists with deadlines',
      'projectWebSite': 'http://www.djangoproject.com'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://www.djangoproject.com')
    self.sniffer.setTargetPath('/')
    
    pattern = """<a href="\/download\/">Latest release: <strong>((\d+\.\d+)[\.\d]*)<\/strong><\/a>"""
    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say('Unable to retrieve version')
      return KO

    self.set('currentVersion', data.group(1).strip())

    self.set('downloadUrl', "http://www.djangoproject.com/download/%s/tarball/" % self.get('currentVersion'))

    # The best release notes I can find for now
    short_version = data.group(2).strip()
    self.set('releaseNotesUrl', "http://docs.djangoproject.com/en/%s/releases/%s/" % (short_version, short_version))

    # I wasn't able to find the release date
    return OK
    
if __name__ == "__main__":
  bot = Bot_Django()
  bot.verbose = True
  rc = bot.run()
  if rc is not OK:
    print "An error occurred while running this bot"
  else:
    print bot.getProperties()
    print bot.getOutput()
