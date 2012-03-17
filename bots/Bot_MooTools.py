#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_MooTools(AppdateHTTPRetriever):
  """The MooTools bot"""
  
  def identify(self):
    return {
      'runnable': False,
      'projectGroup': 'MooTools',
      'projectName': 'MooTools',
      'projectDescription': 'The MooTools JavaScript framework',
      'projectWebSite': 'http://mootools.net'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://mootools.net')
    self.sniffer.setTargetPath('/download')
    
    ##
    # Current Release
    ##
    pattern="""<h3 class="green">Download MooTools (.*)</h3>"""
    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say("No version retrieved")
      return KO
      
    self.set('currentVersion', data.group(1).strip())
    
    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://mootools.net/download")

    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl', "http://github.com/mootools/mootools-core/blob/%s/CHANGELOG" % self.get('currentVersion'))

    ##
    # Release Date
    ##
    self.sniffer.setBaseUrl('http://github.com')
    self.sniffer.setTargetPath("/mootools/mootools-core/blob/%s/CHANGELOG" % self.get('currentVersion'))
    
    pattern = """<div .*>MooTools %s - (.*?)</div>""" % self.get('currentVersion') 

    data = self.sniffer.setTargetPattern(pattern).run()
    if data is not None:
      self.set('releaseDate', data.group(1).strip())

    return OK

if __name__ == "__main__":

  bot = Bot_MooTools()
  bot.verbose = True
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

