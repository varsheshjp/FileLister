import os
from datetime import datetime
import sys
class Explorer:
    def __init__(self,path):
        self.fileList={'name':[],'type':[],'created':[],'modified':[],'accessed':[],'fullpath':[],'size':[]}
        self.path=path
        self.file_count=0
    def searchPath(self,path):
        try:
            flist=os.scandir(path)
            for i in flist:
                if i.is_file():
                    self.file_count+=1
                    self.fileList['name'].append(i.name)
                    stat=i.stat()
                    self.fileList['type'].append(os.path.splitext(i)[1])
                    self.fileList['fullpath'].append(os.path.abspath(i))
                    self.fileList['size'].append(stat.st_size)
                    try:
                        self.fileList['created'].append(datetime.utcfromtimestamp(stat.st_ctime).strftime('%Y %d %m'))
                    except:
                        self.fileList['created'].append(stat.st_ctime)
                    try:
                        self.fileList['modified'].append(datetime.utcfromtimestamp(stat.st_mtime).strftime('%Y %d %m'))
                    except:
                        self.fileList['modified'].append(stat.st_mtime)
                    try:
                        self.fileList['accessed'].append(datetime.utcfromtimestamp(stat.st_atime).strftime('%Y %d %m'))
                    except:
                        self.fileList['accessed'].append(stat.st_atime)
                    sys.stdout.write('\rfile scanned:{0}'.format(self.file_count))
                    sys.stdout.flush()
                else :
                    self.searchPath(i)
        except:
            sys.stdout.write('\rerror for file/dictionary :{0}'.format(path))
            print()
    def searchInit(self):
        self.searchPath(self.path)
        return self.fileList,self.file_count