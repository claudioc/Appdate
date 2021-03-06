#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from Base_Ruby import *

class Bot_Ruby19(Base_Ruby):
  """Ruby, for version 1.9.x"""
  
  def identify(self):
    return {
      'projectGroup': 'Ruby',
      'projectName': 'Ruby 1.9.x',
      'projectDescription': 'The Ruby programming language, version 1.9.x',
      'projectWebSite': 'http://ruby-lang.org'
    }

  def run(self):
    return self._run('1_9')

if __name__ == "__main__":
  bot = Bot_Ruby19()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

