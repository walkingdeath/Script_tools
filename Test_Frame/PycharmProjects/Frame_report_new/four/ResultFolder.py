import os
class ResultFolder(object):

    def GetRunDirectory(self):
        allRunFolders = [fd for fd in os.listdir(".") if os.path.isdir(fd) and fd.startswith("TestRun")]
        latestFolder = max(allRunFolders,key=os.path.getmtime)
        return latestFolder