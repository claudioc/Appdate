
from lib.AppdateHTTPRetriever import *
from BeautifulSoup import BeautifulSoup
import re

class Base_Drupal(AppdateHTTPRetriever):
  """Drupal BOT"""

  def _run(self, target):
    self.sniffer.setBaseUrl('http://drupal.org')
    self.sniffer.setTargetPath('/project/drupal')
    soup = BeautifulSoup(self.sniffer.getContent())
    data = soup.find('tr', {"class": re.compile("%s.*release-update-status-0" % target)})

    if not data:
      self.say('Unable to retrieve version')
      return KO

    data = data.findAll('td')

    self.set('currentVersion', data[0].find('a').contents[0].strip())
    self.set('releaseNotesUrl', "http://drupal.org" + data[3].find('a')['href'])
    self.set('downloadUrl', data[1].find('a')['href'])
    self.set('releaseDate', data[2].contents[0].strip())

    return OK

