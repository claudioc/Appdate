#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from Base_Python import *

class Bot_Python3(Base_Python):
  """Python, for version 3.x"""
  
  def identify(self):
    return {
      'projectGroup': 'Python',
      'projectName': 'Python 3.x',
      'projectDescription': 'The Python programming language, version 3.x',
      'projectWebSite': 'http://python.org'
    }
  
  def run(self):
    return self._run('3')

if __name__ == "__main__":
  bot = Bot_Python3()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

