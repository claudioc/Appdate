#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_Mysql(AppdateHTTPRetriever):
  """MySQL BOT"""
  
  def identify(self):
    return {
      'projectGroup': 'MySQL',
      'projectName': 'MySQL',
      'projectDescription': 'The MySQL DBMS - Community Server',
      'projectWebSite': 'http://www.mysql.com/'
    }
  
  def run(self):
    ##
    # Current Version
    ##
    self.sniffer.setBaseUrl('http://dev.mysql.com')
    self.sniffer.setTargetPath('/downloads')
    pattern = """Current Generally Available Release: 5\.(.*)\)"""
    data = self.sniffer.setTargetPattern(pattern).run()
  
    if not data:
      self.say('Unable to retrieve version')
      return KO
    
    # Get the major version number
    version = "5." + data.group(1)
    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://www.mysql.com/downloads/mysql")
    self.set('currentVersion', version)

    ##
    self.set('releaseNotesUrl', "http://dev.mysql.com/doc/refman/%s/en/news-%s.html" % (version[:3], self.get('currentVersion').replace('.','-')))

    return OK

if __name__ == "__main__":
  bot = Bot_Mysql()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()


