#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_jQuery(AppdateHTTPRetriever):
  """jQuery BOT"""
  
  def identify(self):
    return {
      'projectGroup': 'jQuery',
      'projectName': 'jQuery',
      'projectDescription': 'The jQuery JavaScript library',
      'projectWebSite': 'http://jquery.com'
    }
  
  def run(self):
    
    ##
    # Current Version
    ##
    self.sniffer.setBaseUrl('http://jquery.com')
    self.sniffer.setTargetPath('/')
    data = self.sniffer.setTargetPattern("""<p class="jq-version"><strong>Current Release:</strong>(.*)</p>""").run()
  
    if not data:
      self.say('Unable to retrieve version')
      return KO
      
    self.set('currentVersion', data.group(1).strip())
    
    ##
    # Release Notes is unknown
    ##
    self.set('releaseNotesUrl', "")
    
    ##
    # Release Date is unknown
    ##
    self.set('releaseDate', "")
  
    ##
    # Download URL
    ##
    self.set('downloadUrl', 'http://code.google.com/p/jqueryjs/downloads/list');
    #data = self.sniffer.setTargetPattern("""<form action="(http\:\/\/code.google.com\/p\/jqueryjs\/downloads\/detail)" method="get">""").run()
    #if data is not None:
    #  self.set('downloadUrl', data.group(1).strip())

    return OK

if __name__ == "__main__":
  bot = Bot_jQuery()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()


