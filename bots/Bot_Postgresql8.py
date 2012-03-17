#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from Base_Postgresql import *

class Bot_Postgresql8(Base_Postgresql):
  """Postgresql, for version 8.x"""
  
  def identify(self):
    return {
      'projectGroup': 'PostgreSQL',
      'projectName': 'PostgreSQL 8.x',
      'projectDescription': 'The PostgreSQL RDBMS, version 8.x',
      'projectWebSite': 'http://www.postgresql.org/'
    }

  def run(self):
    return self._run('8')

if __name__ == "__main__":
  bot = Bot_Postgresql8()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

