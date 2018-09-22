from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    # baseUrl = link formatting / pageUrl = gathering links
    def __init__(self):
        super().__init__()
    '''self.baseUrl = baseUrl
        self.pageUrl = pageUrl
        self.links = set()'''

    def handle_starttag(self, tag, attrs):
        print(tag)
        if tag == 'a':
            for(attribute, value) in attrs:
                if attribute == 'href':  # convert relative url to full url
                    url = parse.urljoin(self.baseUrl, value)
                    self.links.add(url)

    def pageLinks(self):
        return self.links

    def error(self, message):
        pass


#print(help(LinkFinder))

finder = LinkFinder()
finder.feed("<html><head><title>Test</title></head><body><h1>Parse me!!!</h1></body></html>")
