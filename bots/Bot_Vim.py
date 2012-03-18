#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_Vim(AppdateHTTPRetriever):
  """The Vim bot"""
  
  def identify(self):
    return {
      'projectGroup': 'Vim',
      'projectName': 'Vim',
      'projectDescription': 'The Vim Editor',
      'projectWebSite': 'http://www.vim.org'
    }
  
  def run(self):
    self.sniffer.setBaseUrl('http://www.vim.org')
    self.sniffer.setTargetPath('/')
    
    ##
    # Current Release
    ##
    pattern="""    <td nowrap class="lightbg" align="right"><small>&nbsp;Vim
(.*)
    is the current version&nbsp;</small></td>"""

    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say("No version retrieved")
      return KO
    self.set('currentVersion', data.group(1).strip())

    self.set('downloadUrl', "http://www.vim.org/download.php")

    self.set('releaseNotesUrl', "http://groups.google.com/group/vim_announce")
    
    return OK

if __name__ == "__main__":

  bot = Bot_Vim()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()
