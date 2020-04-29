import os
from bs4 import BeautifulSoup
# 指定要查詢的路徑

yourPath = './_main'

# 列出指定路徑底下所有檔案(包含資料夾)
allFileList = os.listdir(yourPath)
# 逐一查詢檔案清單
for file in allFileList:
    #   這邊也可以視情況，做檔案的操作(複製、讀取...等)
    #   使用isdir檢查是否為目錄
    #   使用join的方式把路徑與檔案名稱串起來(等同filePath+fileName)
    if os.path.isdir(os.path.join(yourPath, file)):
        print("I'm a directory: " + file)
#   使用isfile判斷是否為檔案
    elif os.path.isfile(yourPath + file):
        print(file)
    else:
        print('OH MY GOD !!')

# 與listdir不同的是，listdir只是將指定路徑底下的目錄和檔案列出來
# walk的方式則會將指定路徑底下所有的目錄與檔案都列出來(包含子目錄以及子目錄底下的檔案)
allList = os.walk(yourPath)
# 列出所有子目錄與子目錄底下所有的檔案
for root, dirs, files in allList:
    #   列出目前讀取到的路徑
    print("path：", root)
    #   列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
    print("directory：", dirs)
    #   列出在這個路徑下讀取到的所有檔案
    print(files)
    # mdfiles = [
    #     i for i in files if os.path.splitext(root + '/' + i)[-1] == '.md'
    # ]

    for i in files:
        if os.path.splitext(root + '/' + i)[-1] == '.md':
            f = open(root + '/' + i)
            soup = BeautifulSoup(f)
            # print(soup.prettify())
            print(
                soup.find_all("a", attrs={
                    "name": "en"
                }).find_next_siblings())
            #https://stackoverflow.com/questions/36189381/cutting-slicing-an-html-document-into-pieces-with-beautifulsoup
    #print("test", arr1)
    # if os.path.splitext(root)[-1] + '/' + files == '.md':
    #     print("file：", files)
