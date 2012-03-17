#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from Base_Drupal import *

class Bot_Drupal5(Base_Drupal):
  """Drupal BOT, for version 5"""
  
  def identify(self):
    return {
      'projectGroup': 'Drupal',
      'projectName': 'Drupal 5',
      'projectDescription': 'The Drupal CMS, version 5',
      'projectWebSite': 'http://drupal.org',
      'runnable': False
    }
  
  def run(self):
    return self._run('downbeta')

if __name__ == "__main__":
  bot = Bot_Drupal5()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()

