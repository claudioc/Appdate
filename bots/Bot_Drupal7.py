#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from Base_Drupal import *

class Bot_Drupal7(Base_Drupal):
  """Drupal BOT, for version 7"""
  
  def identify(self):
    return {
      'projectGroup': 'Drupal',
      'projectName': 'Drupal 7',
      'projectDescription': 'The Drupal CMS, version 7',
      'projectWebSite': 'http://drupal.org'
    }
  
  def run(self):
    return self._run('odd')

if __name__ == "__main__":
  bot = Bot_Drupal6()
  rc = bot.run()
  if rc is not OK:
    print "An error occurred while running this bot"
  else:
    print bot.getProperties()
    print bot.getOutput()

