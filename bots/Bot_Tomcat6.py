#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from Base_Tomcat import *

class Bot_Tomcat6(Base_Tomcat):
  """Tomcat BOT, for version 6"""
  
  def identify(self):
    return {
      'projectGroup': 'Tomcat',
      'projectName': 'Tomcat 6',
      'projectDescription': 'The Tomcat Application Server, version 6',
      'projectWebSite': 'http://tomcat.apache.org'
    }
  
  def run(self):
    return self._run('6')

if __name__ == "__main__":
  bot = Bot_Tomcat6()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

