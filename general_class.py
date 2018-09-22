import os


class CyberSpidey:
     # Core logic of web crawler

    # def __init__(self, )

    # Each website you crawl is a separate project (folder)
    # create new folder and crawl site
    def createProjectDirectory(self, directory):
        if not os.path.exists(directory):
            print('Creating Project: ' + directory)
            os.makedirs(directory)

    # Create queue and crawled files (if not created)
    def createDataFiles(self, projectName, baseUrl):
        queue = projectName + '/queue.txt'  # queue.txt is a list of links on waiting list
        # crawled.txt is a list of finished links
        crawled = projectName + '/crawled.txt'
        if not os.path.isfile(queue):
            write_file(queue, baseUrl)
        if not os.path.isfile(crawled):
            write_file(crawled, ' ')

    # Create a new file
    def write_file(self, path, data):
        f = open(path, 'w')
        f.write(data)
        f.close()


crawler1 = CyberSpidey()
crawler1.createProjectDirectory('Gamefaqs')
crawler1.createDataFiles('GiantBOmb', 'https://www.giantbomb.com/')
