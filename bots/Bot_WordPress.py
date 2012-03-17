#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_WordPress(AppdateHTTPRetriever):
  """The WordPress bot"""
  
  def identify(self):
    return {
      'projectGroup': 'WordPress',
      'projectName': 'WordPress',
      'projectDescription': 'The WordPress blog platform',
      'projectWebSite': 'http://www.wordpress.org'
    }
  
  def run(self):
    ##
    # Current Release
    ##
    self.sniffer.setBaseUrl('http://www.wordpress.org')
    self.sniffer.setTargetPath('/download/')
    data = self.sniffer.setTargetPattern("""<strong>Download&nbsp;WordPress&nbsp;(.*)</strong>""").run()

    if not data:
      self.say("No version retrieved")
      return KO
      
    self.set('currentVersion', data.group(1).strip())

    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl',  "")
  
    ##
    # Release Date in unknown
    ##
    self.set('releaseNotesUrl',  "")
  
    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://wordpress.org/latest.tar.gz")

    return OK

if __name__ == "__main__":

  bot = Bot_WordPress()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

