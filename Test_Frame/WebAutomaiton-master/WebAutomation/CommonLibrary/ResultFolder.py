# import os
#
# def GetRunDirectory():
#     # allRunFolders = [fd for fd in os.listdir("F:\\qgk\\python\\WebAutomaiton-master\\WebAutomation") if os.path.isdir(fd) and fd.startswith("TestRun")]    #判断指定文件夹内文件及文件夹名是路径且以TestRun开头
#     allRunFolders = [fd for fd in os.listdir("F:\\qgk\\python\\WebAutomaiton-master\\WebAutomation") if  fd.startswith("TestRun")]
#
#     print(allRunFolders)
#     latestFolder = max(allRunFolders,key=os.path.getmtime)
#     return latestFolder