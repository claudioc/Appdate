#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_PHP(AppdateHTTPRetriever):
  """The PHP bot"""
  
  def identify(self):
    return {
      'projectGroup': 'PHP',
      'projectName': 'PHP',
      'projectDescription': 'The PHP programming language',
      'projectWebSite': 'http://php.net'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://www.php.net')
    self.sniffer.setTargetPath('/')
    
    ##
    # Current Release
    ##
    pattern="""<li class="php5"><a href="(.*?)">Current PHP 5\.\d Stable: <span class="release">(.*?)</span></a></li>"""
    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say("No version retrieved")
      return KO
      
    self.set('currentVersion', data.group(2).strip())

    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://php.net%s" % data.group(1).strip() )

    ##
    # Release Date
    ##

    self.sniffer.setTargetPath('/downloads.php')
    pattern = """<a href="/get/php-%s\.tar\.bz2/from/a/mirror">PHP %s \(tar\.bz2\)</a>.* -  (.*?)<br""" % (self.get('currentVersion'), self.get('currentVersion')) 

    data = self.sniffer.setTargetPattern(pattern).run()
    if data is not None:
      self.set('releaseDate', data.group(1).strip())

    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl', "%s/ChangeLog-%s.php#%s" % (self.sniffer.getBaseUrl(), self.get('currentVersion')[0:1], self.get('currentVersion')))

    return OK

if __name__ == "__main__":

  bot = Bot_PHP()
  bot.verbose = True
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

