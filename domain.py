from urllib.parse import urlparse


# Take full sub domain name and extract domain (example.com)
def getDomainName(url):
    try:
        results = getSubDomainName(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get full sub domain name (mail.this.is.a.bad.example.com)
def getSubDomainName(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


# print(getDomainName('https://www.mailbag.vapenation.giantbomb.com/podcasts/giant-bomb-gaming-minute/'))