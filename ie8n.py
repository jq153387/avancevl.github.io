msg = 'hello'
print(msg)
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

import os

# 指定要查詢的路徑

yourPath = './'

# 列出指定路徑底下所有檔案(包含資料夾)

allFileList = os.listdir(yourPath)

print(allFileList)

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
