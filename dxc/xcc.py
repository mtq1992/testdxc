import datetime
import urllib2

import threadpool
import time


def hello(i):
    print "I sleep %s seconds"%i
    time.sleep(i)
    print "weekup after %s seconds"%i
if __name__ == "__main__":
    a = datetime.datetime.now()
    print a
    urls = [
        'http://www.python.org',
        'http://www.python.org/about/',
        'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
        'http://www.python.org/doc/',
        'http://www.python.org/download/',
        'http://www.python.org/getit/',
        'http://www.python.org/community/',
        'https://wiki.python.org/moin/',
        'http://planet.python.org/',
        'https://wiki.python.org/moin/LocalUserGroups',
        'http://www.python.org/psf/',
        'http://docs.python.org/devguide/',
        'http://www.python.org/community/awards/'
        # etc..
    ]
    pool = threadpool.ThreadPool(100)
    reqs = threadpool.makeRequests(urllib2.urlopen,urls)
    [pool.putRequest(req) for req in reqs]
    pool.wait()
    b = datetime.datetime.now()
    print b
    print b-a