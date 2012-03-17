#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_FlowPlayer(AppdateHTTPRetriever):
  """The FlowPlayer bot"""
  
  def identify(self):
    return {
      'projectGroup': 'FlowPlayer',
      'projectName': 'FlowPlayer',
      'projectDescription': 'The FlowPlayer Media player',
      'projectWebSite': 'http://flowplayer.org'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://flowplayer.org')
    self.sniffer.setTargetPath('/download/index.html')
    
    ##
    # Current Release
    ##
    pattern="""Version<br/>\s*<strong>(.*?)</strong>"""
    data = self.sniffer.setTargetPattern(pattern).run()
    if not data:
      self.say("No version retrieved")
      return KO
    self.set('currentVersion', data.group(1).strip())

    self.set('downloadUrl', "http://flowplayer.org/download/index.html")

    self.set('releaseNotesUrl', "http://flowplayer.org/documentation/version-history.html")
    
    return OK

if __name__ == "__main__":

  bot = Bot_FlowPlayer()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

