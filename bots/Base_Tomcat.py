
from lib.AppdateHTTPRetriever import *

class Base_Tomcat(AppdateHTTPRetriever):
  """Tomcat BOT"""

  def _run(self, target):
    self.sniffer.setBaseUrl('http://tomcat.apache.org')
    self.sniffer.setTargetPath('/')
    
    pattern = """<a name="Tomcat %s\.(\d+)\.(\d+) Released">""" % target 
    #pattern = """<font face="arial,helvetica,sanserif" size="-1" color="#000000">(%s\..*)</font>""" % target
    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say('Unable to retrieve version')
      return KO

    version = data.group(1)
    self.set('currentVersion', "%s.%s.%s" % (target, data.group(1), data.group(2)))

    version_major = target
    version_minor = data.group(1) #version.split('.')[1]

    self.set('releaseNotesUrl', ("http://tomcat.apache.org/tomcat-%s.%s-doc/RELEASE-NOTES.txt" % (version_major, version_minor)))

    self.set('downloadUrl', ("http://tomcat.apache.org/download-%s%s.cgi#%s" % (version_major, version_minor, version)))

    self.sniffer.setBaseUrl(self.get('releaseNotesUrl'))
    self.sniffer.setTargetPath('')

    pattern = """\$Id: RELEASE-NOTES \d+ (\d{4}-\d{2}-\d{2}) .*\$"""
    data = self.sniffer.setTargetPattern(pattern).run()
    if data is not None:
      self.set('releaseDate', data.group(1))
      
    return OK


