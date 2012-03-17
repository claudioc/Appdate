#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_ZendFramework(AppdateHTTPRetriever):
  """The ZendFramework bot"""
  
  def identify(self):
    return {
      'projectGroup': 'Zend Framework',
      'projectName': 'Zend Framework',
      'projectDescription': 'The Zend Framework',
      'projectWebSite': 'http://framework.zend.com'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://framework.zend.com/download/latest')
    self.sniffer.setTargetPath('/')
    
    pattern="""<h4>\s*Zend Framework(.*)Full\s*</h4>"""
    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say("No version retrieved")
      return KO
    
    ##
    # Current Release
    ##
    self.set('currentVersion', data.group(1).strip().replace(' ', ''))
 
    ##
    # Release Date
    ##
    pattern="""<span>Released (\d{4}-\d{2}-\d{2})\s*</span>"""
    data = self.sniffer.setTargetPattern(pattern).run()
    if data is not None:
      self.set('releaseDate', data.group(1).strip())
    
    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl', "http://framework.zend.com/issues/browse/ZF?report=com.atlassian.jira.plugin.system.project:changelog-panel")

    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://framework.zend.com/download/latest")

    return OK

if __name__ == "__main__":

  bot = Bot_ZendFramework()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

