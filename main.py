import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'giantbomb'
HOMEPAGE = 'https://www.giantbomb.com/'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 3
queue = Queue()

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# create worker threads (will die when main exits)
def createWorkers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawlPage(threading.current_thread().name, url)
        queue.task_done()

# each queued link is a new job
def createJobs():
    for link in convertFileToSet(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# check for items in queue and crawl
def crawl():
    queuedLinks = convertFileToSet(QUEUE_FILE)
    if len(queuedLinks) > 0:
        print(str(len(queuedLinks)) + ' links in the queue.')
        createJobs()


createWorkers()
crawl()
