from urllib.request import urlopen
from link_finder import LinkFinder
from general import*


class Spider:

    # Class variables (shared among all instances)
    projectName = ''
    baseUrl = ''
    domainName = ''
    queueFile = ''
    crawledFile = ''
    queue = set()
    crawled = set()

    def __init__(self, projectName, baseUrl, domainName):
        Spider.projectName = projectName
        Spider.baseUrl = baseUrl
        Spider.domainName = domainName
        Spider.queueFile = Spider.projectName + '/queue.txt'
        Spider.crawledFile = Spider.projectName + '/crawled.txt'
        self.boot()
        self.crawlPage('First spider', Spider.baseUrl)

    @staticmethod
    def boot():
        createProjectDirectory(Spider.projectName)
        createDataFiles(Spider.projectName, Spider.baseUrl)
        Spider.queue = convertFileToSet(Spider.queueFile)
        Spider.crawled = convertFileToSet(Spider.crawledFile)

    @staticmethod
    def crawlPage(threadName, pageUrl):
        if pageUrl not in Spider.crawled:
            print(threadName + 'now crawling ' + pageUrl)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled | ' + str(len(Spider.crawled)))
            Spider.addLinksToQueue(Spider.gatherLink(pageUrl))
            Spider.queue.remove(pageUrl)
            Spider.crawled.add(pageUrl)
            Spider.updateFiles()

    @staticmethod
    def gatherLinks(pageUrl):
        '''Connect to site, take html and convert to string format. Pass data to LinkFinder for parsing.'''
        htmlString = ''
        try:
            response = urlopen(pageUrl)
            if response.getheader('Content-Type') == 'text/html':
                htmlBytes = response.read()
                htmlString = htmlBytes.decode('utf - 8')
            finder = LinkFinder(Spider.baseUrl, pageUrl)
            finder.feed(htmlString)
        except:
            print('Error: cannot crawl page!!!')
            return set()
        return finder.pageLinks()

    @staticmethod
    def addLinksToQueue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domainName not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def updateFiles():
        convertSetToFile(Spider.queue, Spider.queueFile)
        convertSetToFile(Spider.crawled, Spider.crawledFile)




