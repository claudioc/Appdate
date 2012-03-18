#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-

from lib.AppdateHTTPRetriever import *

class Bot_CKEditor(AppdateHTTPRetriever):
  """The CKEditor bot"""
  
  def identify(self):
    return {
      'runnable': True,
      'projectGroup': 'CKEditor',
      'projectName': 'CKEditor',
      'projectDescription': 'CKEditor RTE',
      'projectWebSite': 'http://ckeditor.com'
    }
  
  def run(self):
    ##
    # Current Release
    ##
    self.sniffer.setBaseUrl('http://ckeditor.com')
    self.sniffer.setTargetPath('/download')
    data = self.sniffer.setTargetPattern("""<span>CKEditor\s+(.*)<\/span>,\s+released on <span>(.*)<\/span>""").run()

    if not data:
      self.say("No version retrieved")
      print "no"
      return KO

    self.set('currentVersion', data.group(1).strip())

    ##
    # Release Notes
    ##
    self.set('releaseNotesUrl',  "http://ckeditor.com/whatsnew")

    # Release Date in unknown
    ##
    self.set('releaseDate',  data.group(2).strip())

    ##
    # Download URL
    ##
    self.set('downloadUrl', "http://ckeditor.com/download")

    return OK

if __name__ == "__main__":

  bot = Bot_CKEditor()
  rc = bot.run()
  if rc is not OK:
    print "An error occurred while running this bot"
  else:
    print bot.getProperties()
    print bot.getOutput()

