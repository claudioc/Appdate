#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from Base_Ruby import *

class Bot_Ruby18(Base_Ruby):
  """Ruby, for version 1.8.x"""
  
  def identify(self):
    return {
      'projectGroup': 'Ruby',
      'projectName': 'Ruby 1.8.x',
      'projectDescription': 'The Ruby programming language, version 1.8.x',
      'projectWebSite': 'http://ruby-lang.org'
    }

  def run(self):
    return self._run('1_8')

if __name__ == "__main__":
  bot = Bot_Ruby18()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

