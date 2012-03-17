import re
from lib.AppdateSniffer import *

class AppdateHTTPSniffer(AppdateSniffer):
  def __init__(self, fetcher):
    self.fetcher = fetcher
    self.content = None

  def run(self,mode=FIND_FIRST):
      
    self.getContent()
    
    if mode == FIND_FIRST:
      return re.compile(self.target).search(self.content, re.MULTILINE)
    if mode == FIND_ALL:
      return re.compile(self.target).findall(self.content, re.MULTILINE)

    return None

  def getContent(self):
    if not self.content:
      self.fetcher.fetch(self.baseUrl + self.targetPath)
      self.content = self.fetcher.content

    return self.content

  def setBaseUrl(self, data):
    self.baseUrl = data
    return self
    
  def getBaseUrl(self):
    return self.baseUrl
    
  def setTargetPath(self, data):
    self.targetPath = data
    self.content = None
    return self
    
  def setTargetPattern(self, data):
    self.target = data
    return self

