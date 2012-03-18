#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_Virtualbox(AppdateHTTPRetriever):
  """The Virtualbox bot"""
  
  def identify(self):
    return {
      'runnable': True,
      'projectGroup': 'Virtualbox',
      'projectName': 'Oracle Virtualbox',
      'projectDescription': 'Oracle Virtualbox virtualizer',
      'projectWebSite': 'http://www.virtualbox.org'
    }
  
  def run(self):
    ##
    # Current Release
    ##
    self.sniffer.setBaseUrl('http://www.virtualbox.org')
    self.sniffer.setTargetPath('/wiki/Changelog')
    data = self.sniffer.setTargetPattern("""<strong>VirtualBox (.*)<\/strong>\s+\(released (.*)\)""").run()

    if not data:
      self.say("No version retrieved")
      return KO
      
    self.set('currentVersion', data.group(1).strip())

    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl',  "http://www.virtualbox.org/wiki/Changelog")
  
    # Release Date in unknown
    ##
    self.set('releaseDate',  data.group(2).strip())
  
    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://www.virtualbox.org/wiki/Downloads")

    return OK

if __name__ == "__main__":

  bot = Bot_Virtualbox()
  rc = bot.run()
  if rc is not OK:
    print "An error occurred while running this bot"
  else:
    print bot.getProperties()
    print bot.getOutput()

