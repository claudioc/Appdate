#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *
from BeautifulSoup import BeautifulSoup
import re

class Bot_NodeJS(AppdateHTTPRetriever):
  """The Nodejs bot"""
  
  def identify(self):
    return {
      'projectGroup': 'NodeJS',
      'projectName': 'NodeJS',
      'projectDescription': 'nodejs.org',
      'projectWebSite': 'http://nodejs.org'
    }

  def run(self):
    self.sniffer.setBaseUrl('http://nodejs.org')
    self.sniffer.setTargetPath('/')

    soup = BeautifulSoup(self.sniffer.getContent())

    a = soup.find('p', {"class": "version"}).contents[0]
    version = a.replace('v', '').replace(' docs', '').strip()

    ##
    # Current Release
    ##

    if not version:
      self.say("No version retrieved")
      return KO

    self.set('currentVersion', version)

    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://nodejs.org/dist/node-v%s.tar.gz" % version)

    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl', "https://github.com/joyent/node/wiki/ChangeLog")

    ##
    # Release Date
    ##
    date = soup.find('p', text=re.compile("v%s \(stable" % version))

    if date is not None:
      self.set('releaseDate', date[:10])

    return OK

if __name__ == "__main__":

  bot = Bot_NodeJS()
  bot.verbose = True
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

