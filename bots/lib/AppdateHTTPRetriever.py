from lib.AppdateRetriever import *
from lib.PageFetcher import *
from lib.AppdateHTTPSniffer import *

class AppdateHTTPRetriever(AppdateRetriever):
  def __init__(self):
    super(AppdateHTTPRetriever, self).__init__()
    self.fetcher = PageFetcher(debug=False, timeout=float(15))
    self.sniffer = AppdateHTTPSniffer(self.fetcher)

