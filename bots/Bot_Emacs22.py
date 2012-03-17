#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_Emacs22(AppdateHTTPRetriever):
  """The Emacs bot"""
  
  def identify(self):
    return {
      'projectGroup': 'Emacs',
      'projectName': 'Emacs',
      'projectDescription': 'An extensible, customizable text editor-and more.',
      'projectWebSite': 'http://www.gnu.org/software/emacs/'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://www.gnu.org/software/emacs/')
    self.sniffer.setTargetPath('/')
    
    ##
    # Current Release
    ##
    pattern="""<li>(.*?) - <a href="(.*?)">Emacs (\d+\.\d+) released</a></li>""" 

    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say("No version retrieved")
      return KO
      
    self.set('currentVersion', data.group(3).strip())
    self.set('releaseDate', data.group(1).strip())
    
    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://ftp.gnu.org/pub/gnu/emacs/")

    ##
    # Release Notes
    ##
    release_url = data.group(2).strip()
    self.set('releaseNotesUrl', release_url)

    return OK

if __name__ == "__main__":

  bot = Bot_Emacs22()
  bot.verbose = True
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

