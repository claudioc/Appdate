#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_Appdate(AppdateHTTPRetriever):
  """BOT for Appdate"""
  
  def identify(self):
    return {
      'projectGroup': 'Appdate',
      'projectName': 'Appdate',
      'projectDescription': 'The Appdate project',
      'projectWebSite': 'http://www.appdate.it'
    }
  
  def run(self):
    
    ##
    # Current Version
    ##
    self.sniffer.setBaseUrl('http://www.appdate.it')
    self.sniffer.setTargetPath('/')
    data = self.sniffer.setTargetPattern("""<span class="currentVersion">(.*?)</span>""").run()
    
    if not data:
      self.say('Unable to retrieve version')
      return KO
      
    self.set('currentVersion', data.group(1).strip())
    
    ##
    # Release Date
    ##
    data = self.sniffer.setTargetPattern("""<span class="releaseDate">(.*?)</span>""").run()
    if data is not None:
      self.set('releaseDate', data.group(1).strip())
  
    ##
    # Release Notes
    ##
    data = self.sniffer.setTargetPattern("""<a class="releaseNotesUrl" href="(.*?)">.*</a>""").run()
    if data is not None:
      self.set('releaseNotesUrl', data.group(1).strip())
  
    ##
    # Download URL
    ##
    data = self.sniffer.setTargetPattern("""<a class="downloadUrl" href="(.*?)">.*</a>""").run()
    if data is not None:
      self.set('downloadUrl', data.group(1).strip())
    
    return OK

if __name__ == "__main__":
  bot = Bot_Appdate()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()


