
from lib.AppdateHTTPRetriever import *

class Base_Apache(AppdateHTTPRetriever):
  """Apache BOT"""

  def _run(self, target):
    self.sniffer.setBaseUrl('http://www.apache.org/dist/httpd')
    self.sniffer.setTargetPath(("/Announcement2.%s.txt" % target))
    
    pattern = """Apache HTTP Server (.*) Released"""

    data = self.sniffer.setTargetPattern(pattern).run()

    if not data:
      self.say('Unable to retrieve version')
      return KO

    version = data.group(1)
    self.set('currentVersion', version)

    version_major = 2
    version_minor = target
    version_micro = version.split('.')[2]

    self.set('releaseNotesUrl', ("http://www.apache.org/dist/httpd/CHANGES_%s.%s.%s" % (version_major, version_minor, version_micro)))

    self.set('downloadUrl', ("http://httpd.apache.org/download.cgi#apache2%s" % (version_minor)))

    return OK

