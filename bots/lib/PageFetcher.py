#import lib.httplib2 as HttpLib
import httplib2 as HttpLib

class PageFetcher:
  problem = None
  debug = False
  headers = None
  content = None
  http = None
  
  def __init__(self,timeout=10,debug=False):
    self.http = HttpLib.Http(None,timeout)
    self.debug = debug
  
  def fetch(self, url):
    self.problem = None
    # Get the page within the specified timeout and correct name resolution
    try:
      self.headers, self.content = self.http.request(uri=url, method="GET", headers={'user-agent': 'Appdate bot - http://www.appdate.it/page/bot'})
    except HttpLib.ServerNotFoundError:
      self.problem = "server not found"
    except HttpLib.socket.timeout:
      self.problem = "the request takes too long to be fullfilled"
    except HttpLib.socket.error, error:
      self.problem = "%s (%d)" % (error[1], error[0])
    else:
      if self.headers['status'] != '200':
        self.problem = 'status code is not 200 (%s)' % self.headers['status']
      else:
        if self.debug: print url + " fetched"

    if self.problem:
      self.problem = "While fetching %s : %s" % (url, self.problem)

    return self.problem == None


