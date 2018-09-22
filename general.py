import os

# Each website you crawl is a separate project (folder)

def createProjectDirectory(directory): # create new folder and crawl site
    if not os.path.exists(directory):
        print('Creating Project: ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)

def createDataFiles(projectName, baseUrl):
    queue = projectName + 'queue.txt' # queue.txt is a list of links on waiting list
    crawled = projectName + 'crawled.txt' # crawled.txt is a list of finished links
    if not os.path.isfile(queue):
        writeFile(queue, baseUrl)
    if not os.path.isfile(crawled):
        writeFile(crawled,' ')

# Create a new file
def writeFile(path, data):
    f = open(path, 'w') # 'w' means write
    f.write(data)
    f.close()

# Add data onto an existing file
def appendToFile(path, data):
    with open(path, 'a') as file_object: # 'a' means append
        file_object.write(data + '\n')


# Delete the contents of a file
def deleteFileContents(path):
    with open(path, 'w'):
        pass # do nothing


# Read a file and convert each line to set items
def convertFileToSet(fileName):
    results = set()
    with open(fileName, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a new line in the file
def convertSetToFile(links, file):
    deleteFileContents(file)
    for link in sorted(links):
        appendToFile(file, link)
