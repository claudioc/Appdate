#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_Linux(AppdateHTTPRetriever):
  """The Linux Kernel Bot"""

  def identify(self):
    return {
      'projectGroup': 'Linux',
      'projectName': 'Linux Kernel',
      'projectDescription': 'The Linux Kernel',
      'projectWebSite': 'http://kernel.org'
    }
  
  def run(self):

    ##
    # Current Release
    ##
    self.sniffer.setBaseUrl('http://kernel.org')
    self.sniffer.setTargetPath('/')
    
    data = self.sniffer.setTargetPattern("""<td >stable:</td>\s*<td ><strong>(.*?)</strong></td>\s*<td >(.*?)</td>\s*<td >\[<a href="(.*?)".*\]</td>\s*<td >(.*?)</td>\s*<td >(.*?)</td>\s*<td >(.*?)</td>\s*<td >(.*?)</td>\s*<td >\[<a href="(.*?)".*\]</td>""").run()

    if not data:
      print "No version retrieved"
      return KO
      
    self.set('currentVersion',  data.group(1).strip())
    self.set('releaseDate',     data.group(2).strip())
    self.set('downloadUrl',     data.group(3).strip())
    self.set('releaseNotesUrl', data.group(8).strip())
    
    return OK

if __name__ == "__main__":

  bot = Bot_Linux()
  if bot.isRunnable():
    rc = bot.run()
    if rc is not OK:
      print "An error occurred while running this bot"
    else:
      print bot.getProperties()
      print bot.getOutput()
  
