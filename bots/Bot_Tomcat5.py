#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from Base_Tomcat import *

class Bot_Tomcat5(Base_Tomcat):
  """Tomcat BOT, for version 5"""
  
  def identify(self):
    return {
      'projectGroup': 'Tomcat',
      'projectName': 'Tomcat 5',
      'projectDescription': 'The Tomcat Application Server, version 5',
      'projectWebSite': 'http://tomcat.apache.org'
    }
  
  def run(self):
    return self._run('5')

if __name__ == "__main__":
  bot = Bot_Tomcat5()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

