#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_SocketIO(AppdateHTTPRetriever):
  """Socket.io BOT"""
  
  def identify(self):
    return {
      'projectGroup': 'Socket.io',
      'projectName': 'Socket.io',
      'projectDescription': 'The Socket.io JavaScript library',
      'projectWebSite': 'http://socket.io',
      'runnable': True
    }
  
  def run(self):
    
    ##
    # Current Version
    ##
    self.sniffer.setBaseUrl("https://raw.github.com");
    self.sniffer.setTargetPath("/LearnBoost/socket.io/master/History.md");
    data = self.sniffer.getContent()

    if not data:
      self.say('Unable to retrieve version')
      return KO
      
    version = data.split("\n")[1].split("/")

    self.set('currentVersion', version[0].strip())
    
    ##
    # Release Notes is unknown
    ##
    self.set('releaseNotesUrl', "https://github.com/LearnBoost/socket.io/blob/master/History.md")
    
    ##
    # Release Date is unknown
    ##
    self.set('releaseDate', version[1].strip())
  
    ##
    # Download URL
    ##
    self.set('downloadUrl', 'https://github.com/LearnBoost/socket.io');

    return OK

if __name__ == "__main__":
  bot = Bot_SocketIO()
  rc = bot.run()
  if rc is not OK:
    print "An error occurred while running this bot"
  else:
    print bot.getProperties()
    print bot.getOutput()


