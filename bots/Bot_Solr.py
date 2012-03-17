#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_Solr(AppdateHTTPRetriever):
  """Solr BOT"""
  
  def identify(self):
    return {
      'projectGroup': 'Solr',
      'projectName': 'Solr',
      'projectDescription': 'The Solr search server',
      'projectWebSite': 'http://lucene.apache.org/solr/'
    }
  
  def run(self):
    ##
    # Current Version
    ##
    self.sniffer.setBaseUrl('http://svn.apache.org/repos/asf/lucene/solr/tags')
    self.sniffer.setTargetPath('/')
    data = self.sniffer.setTargetPattern("""<li><a href=".*">(.*)</a></li>""").run(mode=FIND_ALL)
  
    if not data:
      self.say('Unable to retrieve version')
      return KO
    
    versionTag = data[-1][:-1]

    self.set('currentVersion', versionTag.replace('release-',''))
    
    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl', "http://svn.apache.org/repos/asf/lucene/solr/tags/%s/CHANGES.txt" % versionTag)

    ##
    # Release Date
    ##
    self.sniffer.setBaseUrl('http://www.apache.org/dist/lucene/solr')
    self.sniffer.setTargetPath('/')
    data = self.sniffer.setTargetPattern("""<a href="%s/">%s/</a>(.*) .*:.* -""" % (self.get('currentVersion'), self.get('currentVersion'))).run()
    if data is not None:
      self.set('releaseDate', data.group(1).strip())

    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://www.apache.org/dist/lucene/solr/%s" % self.get('currentVersion'))
    return OK

if __name__ == "__main__":
  bot = Bot_Solr()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()


