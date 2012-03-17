#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_jEdit(AppdateHTTPRetriever):
  """The WordPress bot"""
  
  def identify(self):
    return {
      'projectGroup': 'jEdit',
      'projectName': 'jEdit',
      'projectDescription': 'The jEdit text editor',
      'projectWebSite': 'http://jedit.org'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://jedit.org')
    self.sniffer.setTargetPath('/')
    
    pattern="""Last Site Update: (.*) \| Stable Version: <a class="header_text" href="(.*?)">(.*?)</a>"""
    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say("No version retrieved")
      return KO
      
    ##
    # Release Date
    ##
    self.set('releaseDate', data.group(1).strip())
    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl', "%s/%s" % (self.sniffer.getBaseUrl(), data.group(2).strip()))
    ##
    # Current Release
    ##
    self.set('currentVersion', data.group(3).strip())

    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://jedit.org/index.php?page=download")

    return OK

if __name__ == "__main__":

  bot = Bot_jEdit()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

