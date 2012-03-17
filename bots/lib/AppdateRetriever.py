from lib.constants import *

class AppdateRetriever(object):
  def __init__(self):
    self.verbose = False
    self.initialize()
    self.properties = {
      'projectGroup': UNKNOWN_GROUP,
      'projectName': UNKNOWN_PROJECT,
      'projectDescription': '',
      'projectWebSite': '',
      'runnable': True
    }

  def getProperties(self):
    properties = self.identify()
    if properties is not None:
      self.properties.update(properties)
    return self.properties

  def initialize(self):
    self.data = {
      'currentVersion': '',
      'releaseNotesUrl': '',
      'downloadUrl': '',
      'releaseDate': '',
    }
  
  def isRunnable(self):
    return self.properties.has_key('runnable') and self.properties['runnable'] == True
    
  def run(self):
    pass
  
  def identify(self):
    return self.properties
  
  def set(self, attr, value):
    self.data[attr] = value
  
  def get(self, attr):
    return self.data[attr]
  
  def getOutput(self):
    return self.data
  
  def save(self):
    self.initialize()
    
  def say(self, message):
    if self.verbose:
      print message
  
  def setVerbose(self, verbose):
    self.verbose = verbose
