import os
from datetime import datetime
class Explorer:
    def __init__(self,path):
        self.fileList={'name':[],'type':[],'created':[],'modified':[],'accessed':[],'fullpath':[],'size':[]}
        self.path=path
        self.file_count=0
    def searchPath(self,path,lev):
        if self.printF=='yes':
            print(' '*lev*3,'>>>',path)
        with os.scandir(path) as flist:
            for i in flist:
                if i.is_file():
                    self.file_count+=1
                    self.fileList['name'].append(i.name)
                    stat=i.stat()
                    self.fileList['type'].append(os.path.splitext(i)[1])
                    self.fileList['created'].append(datetime.utcfromtimestamp(stat.st_ctime).strftime('%Y %d %m'))
                    self.fileList['modified'].append(datetime.utcfromtimestamp(stat.st_mtime).strftime('%Y %d %m'))
                    self.fileList['accessed'].append(datetime.utcfromtimestamp(stat.st_atime).strftime('%Y %d %m'))
                    self.fileList['fullpath'].append(os.path.abspath(i))
                    self.fileList['size'].append(stat.st_size)
                else :
                    self.searchPath(i,lev+1)
    def searchInit(self,printF):
        self.printF=printF
        self.searchPath(self.path,0)
        return self.fileList,self.file_count