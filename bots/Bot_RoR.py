#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_RoR(AppdateHTTPRetriever):
  """The Ruby on Rails bot"""
  
  def identify(self):
    return {
      'projectGroup': 'Ruby on Rails',
      'projectName': 'Ruby on Rails',
      'projectDescription': 'The Ruby on Rails framework',
      'projectWebSite': 'http://rubyonrails.org'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://rubyforge.org')
    self.sniffer.setTargetPath('/frs/?group_id=307')
    
    ##
    # Current version
    ##
    pattern="""<a href="shownotes.php\?release_id=\d+">REL (.*)<\/a>"""
    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say("No version retrieved")
      return KO
      
    self.set('currentVersion', data.group(1).strip())

    ##
    # Release Date
    ##
    pattern="""(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}<\/strong>"""
    data = self.sniffer.setTargetPattern(pattern).run()
    
    if data is not None:
      self.set('releaseDate', data.group(1).strip())
    
    ##
    # Release Notes
    ##
    # self.set('releaseNotesUrl', '')

    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://rubyforge.org/frs/?group_id=307")

    return OK

if __name__ == "__main__":

  bot = Bot_RoR()
  bot.verbose = True
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

