
from lib.AppdateHTTPRetriever import *

class Base_Python(AppdateHTTPRetriever):
  """Python BOT"""

  def _run(self, target):
    self.sniffer.setBaseUrl('http://www.python.org')
    self.sniffer.setTargetPath('/')
    
    pattern = """>Quick Links \((%s\.\d\.?\d*)\)<\/a>""" % target
    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say('Unable to retrieve version')
      return KO

    self.set('currentVersion', data.group(1).strip())

    self.set('downloadUrl', "http://www.python.org/download/releases/%s" % self.get('currentVersion'))

    self.set('releaseNotesUrl', "http://www.python.org/download/releases/%s" % self.get('currentVersion'))


    self.sniffer.setTargetPath("/download/releases/%s/NEWS.txt" % self.get('currentVersion'))

    pattern = """\*Release date: (.*)\*"""
    data = self.sniffer.setTargetPattern(pattern).run()
    
    if data is not None:
      self.set('releaseDate', data.group(1))

    return OK 

