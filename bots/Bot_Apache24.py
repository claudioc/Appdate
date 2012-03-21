#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from Base_Apache import *

class Bot_Apache24(Base_Apache):
  """Apache, for version 2.4.x"""
  
  def identify(self):
    return {
      'projectGroup': 'Apache',
      'projectName': 'Apache 2.4',
      'projectDescription': 'The Apache HTTP server, version 2.4',
      'projectWebSite': 'http://httpd.apache.org'
    }

  def run(self):
    return self._run('4')

if __name__ == "__main__":
  bot = Bot_Apache24()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

