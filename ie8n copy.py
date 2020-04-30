from bs4 import BeautifulSoup
import frontmatter
import yaml
filepath = "./_main/index.md"
setlang = ["en", "zh-tw", "zh-cn"]
tag = "a"
attrname = "name"

# ducyaml = """
# ---
# layout: default
# title: Welcome to my web!
# lang: zh-cn
# lang-ref: welcome-to-my-web
# ---
# """
# data = exec(ducyaml)
# with open(ducyaml, "r") as stream:
# data = yaml.load(ducyaml)
# dict = {'name': 'ngy', 'age': 23, 'height': 180}
# print(dict)
# print(dict["nams"])
# data = list(yaml.load_all(ducyaml))[0]
# if key in mydict:
#     value = mydict[key]
# print(data['filepath'])
# for s in data:

#     print(s)


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
    print(metadata)
    # print(post.keys(), 'keys')
    # 內容標籤值與設定值(語系)是否存在
    langname = []
    for lang in soup.find_all(tag):
        for name in setlang:
            if lang.get(attrname) == name:
                langname.append(name)

    # print(langname)
    article_lang = {}
    # print(document_data)
    for value in langname:
        atag = soup.find(tag, {attrname: value})
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
            'lang: ' + value, 'description: ' + post_description,
            'lang-ref: welcome-to-my-web', '---\n\n'
        ]
        # data = list(yaml.load_all(f, Loader=yaml.FullLoader))
        story = '\n'.join(lang_metadata)
        # print(data)
        article.append(story)
        ##第一的元素的之後的文字
        article.append(atag.next_sibling.strip() + "\n\n")
        atag_next_siblings = atag.find_next_siblings()
        # if elm.get(attrname) == value:
        now_lag_index = langname.index(value)
        # print(now_lag_index)
        # print(langname[now_lag_index + 1])
        if now_lag_index + 1 < len(langname):
            # print(now_lag_index + 1)
            next_element = soup.find(tag,
                                     {attrname: langname[now_lag_index + 1]})
            if next_element != None:
                next_element_index = atag_next_siblings.index(next_element)
                atag_split = atag_next_siblings[0:next_element_index]
        else:
            atag_split = atag_next_siblings
            # print(atag_split)
        # print(atag_next_siblings)
        for atag_elm in atag_split:
            article.append(atag_elm)
            article.append(atag_elm.next_sibling)
            pass

        #print(elm.next_sibling)
        # print(artice)
        article_lang[value] = article
    pass

    return article_lang


article_lang = rfileDate(filepath, setlang, tag, attrname)

# print(article_lang)
print("============================================================>")

path = "/index.md"
fname = "_pages_"


def creatFiles(article_lang, path, fname):
    """
    Args:
        filepath:  標籤參數如語系區分的資料
            {   
                'zh-tw': [string, string],
                'zh-cn': [string, string],
                'zh-tw': [string, string]
            }
        path: 輸入相對檔案路徑 "/index.md"
        name: 輸出的資料夾主別名目綠 "_pages_"
   
    """
    for key in article_lang:
        with open("./" + fname + key + path, "w") as fp:
            for item in article_lang[key]:
                # print(item)
                #pickle.dump(str(item), fp)
                fp.write(str(item))


creatFiles(article_lang, path, fname)
print("end============================================================>")
# print(soup.prettify())
# 建立的目錄路徑
# folderpath = "/home/gtwang/my_folder"

# # 使用 try 建立目錄
# try:
#     os.makedirs(folderpath)
# # 檔案已存在的例外處理
# except FileExistsError:
#     print("檔案已存在。")
