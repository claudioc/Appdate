#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_OpenOffice(AppdateHTTPRetriever):
  """The OpenOffice bot"""
  
  def identify(self):
    return {
      'projectGroup': 'OpenOffice',
      'projectName': 'OpenOffice',
      'projectDescription': 'The OpenOffice.org office suite',
      'projectWebSite': 'http://www.openoffice.org'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://download.openoffice.org')
    self.sniffer.setTargetPath('/globalvars.js')
    
    ##
    # Current Release
    ##
    pattern="""var VERSION\s*=\s*"(.*)";"""
    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say("No version retrieved")
      return KO
      
    self.set('currentVersion', data.group(1).strip())

    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://download.openoffice.org/")

    ##
    # Release Date
    ##
    self.set('releaseDate', '')

    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl', "http://development.openoffice.org/releases/%s.html" % (self.get('currentVersion')))

    return OK

if __name__ == "__main__":

  bot = Bot_OpenOffice()
  bot.verbose = True
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

