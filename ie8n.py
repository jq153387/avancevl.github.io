import os
from bs4 import BeautifulSoup
import frontmatter
import yaml
# import re
mainPath = './_main'
# filepath = "./_main/index.md"
setlang = ["en", "zh-tw", "zh-cn"]
tag = "a"
attrname = "name"
falias = "_pages"


def rfileDate(filepath, setlang, tag, attrname):
    """
    讀取目錄資料夾檔案，使用標籤參數拆分
    
    Args:
        filepath: 檔案目錄
        setlang: 檔案語言list[]
        tag: 標籤 a
        attrname: 指定查詢標籤參數 name
    Returns:
        使用查詢到的標籤參數值返回dict
        {   
            'zh-tw': [string, string],
            'zh-cn': [string, string],
            'zh-tw': [string, string]
        }
    """
    f = open(filepath, "r")
    soup = BeautifulSoup(f, 'html.parser')

    metadata = frontmatter.load(filepath).metadata
    content = frontmatter.load(filepath).content
    #print(content)
    # print(post.keys(), 'keys')
    # 內容標籤值與設定值(語系)是否存在
    langname = []
    for lang in soup.find_all(tag):
        for name in setlang:
            if lang.get(attrname) == name:
                langname.append(name)
    lang_content = {}
    for value in langname:
        now_lag_index = langname.index(value)
        finds = soup.find(tag, {attrname: value}).prettify()
        now_lang_tag = finds.replace('\n', '')
        # print(content)
        # re.search(r'^<a name=[\"|']zh-cn[\"|']>[\s\S]</a>'',content)
        now_lang_index = content.find(now_lang_tag) + len(now_lang_tag)
        # print(now_lang_index)
        if now_lag_index + 1 < len(langname):
            next_lang = langname[now_lag_index + 1]
            next_lang_tag = soup.find(tag, {
                attrname: next_lang
            }).prettify().replace('\n', '')
            next_lang_index = content.find(next_lang_tag)
            lang_content[value] = content[now_lang_index:next_lang_index]
        else:
            lang_content[value] = content[now_lang_index:len(content)]

    # print(lang_content)

    article_lang = {}
    # print(document_data)
    for value in langname:
        article = []

        #print(document_data)
        if "locales" in metadata:
            if value in metadata['locales']:
                post_title = metadata['locales'][value]['title']
                post_description = metadata['locales'][value]['description']
            else:
                ##使用default lang_mate
                post_title = metadata['title']
                post_description = metadata['description']
        else:
            ##使用default lang_mate
            post_title = metadata['title']
            post_description = metadata['description']

        lang_metadata = [
            '---', 'layout: ' + metadata['layout'], 'title: ' + post_title,
            'lang: ' + value, 'description: ' + post_description, '---\n\n'
        ]
        # data = list(yaml.load_all(f, Loader=yaml.FullLoader))
        story = '\n'.join(lang_metadata)
        # print(data)
        article.append(story)
        article.append(lang_content[value])
        article_lang[value] = article

    return article_lang


#test
# filepath = "./_main/index.md"
# article_lang = rfileDate(filepath, setlang, tag, attrname)
# print(article_lang)
print("============================================================>")


def creatFiles(article_lang, path, filename, falias):
    """
    Args:
        article_lang:  標籤參數如語系區分的資料
            {   
                'zh-tw': [string, string],
                'zh-cn': [string, string],
                'zh-tw': [string, string]
            }
        path: 輸入相對檔案路徑 "/index.md"
        filename: 輸出的資料名稱
        fname: 輸出的資料夾主別名目綠 "_pages"
    """
    for key in article_lang:
        """
        如果指定目錄不存在就建立目錄
        要不然的話就直接開檔案
        """
        _path = "./" + falias + "/" + key + "/" + path

        if not os.path.isdir(_path):
            os.mkdir(_path)
        with open(_path + "/" + filename, "w") as fp:
            for item in article_lang[key]:
                # print("filename:", filename)
                fp.write(str(item))


print("============================================>")
# walk的方式則會將指定路徑底下所有的目錄與檔案都列出來(包含子目錄以及子目錄底下的檔案)
allList = os.walk(mainPath)
# 列出所有子目錄與子目錄底下所有的檔案
for root, dirs, files in allList:
    #   列出目前讀取到的路徑
    # print("path：", root)
    #   列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
    # print("directory：", dirs)
    #   列出在這個路徑下讀取到的所有檔案
    # print("files：", files)

    for i in files:
        if os.path.splitext(root + '/' + i)[-1] == '.md':
            filepath = root + '/' + i
            filename = i
            # print("root:", root)
            path = root.replace(mainPath + "/", "") if root != mainPath else ""
            # print("filename:", i)
            # print("filepath:", path)
            article_lang = rfileDate(filepath, setlang, tag, attrname)
            # print(article_lang)
            creatFiles(article_lang, path, filename, falias)
print("成功完成!============================================================>")
