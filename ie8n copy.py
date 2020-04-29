from bs4 import BeautifulSoup
import pickle
f = open("./_main/index.md", "r")
soup = BeautifulSoup(f, 'html.parser')
# html = soup.find(id='some_id')
# soup = BeautifulSoup(f, features="html.parser")

##print(atag.find_next_siblings())
#print(soup.find(lang))
setlang = ["en", "zh-tw", "zh-cn"]

print(soup.find_all('a'))
langname = []
for lang in soup.find_all('a'):
    print(lang.get('name'))
    for name in setlang:
        if lang.get('name') == name:
            langname.append(name)

print(langname)
article_lang = {}
for value in langname:
    atag = soup.find("a", {"name": value})
    article = []
    for elm in atag.find_next_siblings():
        article.append(elm)
        article.append(elm.next_sibling)
        #print(elm.next_sibling)
    # print(artice)
    article_lang[value] = article
# print(article_lang)
print("============================================================>")
with open("./sss.md", "w") as fp:
    for key in article_lang:

        for item in article_lang[key]:
            print(item)
            #pickle.dump(str(item), fp)
            fp.write(str(item))
# print(soup.prettify())

import os

# 指定要查詢的路徑

yourPath = './'

# # 列出指定路徑底下所有檔案(包含資料夾)

# allFileList = os.listdir(yourPath)

# print(allFileList)

# # 逐一查詢檔案清單

# for file in allFileList:

#     #   這邊也可以視情況，做檔案的操作(複製、讀取...等)

#     #   使用isdir檢查是否為目錄

#     #   使用join的方式把路徑與檔案名稱串起來(等同filePath+fileName)

#     if os.path.isdir(os.path.join(yourPath, file)):

#         print("I'm a directory: " + file)

# #   使用isfile判斷是否為檔案

#     elif os.path.isfile(yourPath + file):

#         print(file)

#     else:

#         print('OH MY GOD !!')
