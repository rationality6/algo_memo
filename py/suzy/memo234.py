from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
import sys

import sqlite3
conn = sqlite3.connect('suzy.db')
conn = conn.cursor()

# sqlConnect = pymysql.connect(
#     host="127.0.0.1", user="root", passwd="1018", db="suzy", charset="utf8")
# conn = sqlConnect.conn()

path_phan = "{}/node_modules/phantomjs/bin/phantomjs".format(sys.path[0])

browser = webdriver.PhantomJS(path_phan)


def store(filename):
    sql = "INSERT INTO pictures (filename) VALUES ({})".format(filename)
    conn.execute(sql)
    conn.connection.commit()


def findFilenameFromDb(filename):
    print("here!!")
    sql = "SELECT filename FROM pictures WHERE filename={}".format(filename)
    conn.execute(sql)
    result = conn.fetchone()
    print(result)
    return result


for i in range(1801, 325100):
    print(i)
    url = "http://gall.dcinside.com/board/view/?id=suzy&no={}&page=1".format(i)
    browser.get(url)
    html = browser.page_source
    bsObj = BeautifulSoup(html, "html.parser")

    try:
        imgLocations = bsObj.find(
            "ul", {"class": "appending_file"}).find_all("a")
    except AttributeError as e:
        print(e)
    else:
        if len(imgLocations) > 0:
            for imgUrl in imgLocations:
                url = imgUrl["href"]
                filename = imgUrl.get_text()

                if (findFilenameFromDb(filename)):
                    print("The image already exists")
                else:
                    rp_from = "http://image.dcinside.com/download.php"
                    rp_to = "http://image.dcinside.com/viewimagePop.php"
                    url = url.replace(rp_from, rp_to)

                    newHtml = urlopen(url)
                    newBsObj = BeautifulSoup(newHtml.read(), "html.parser")
                    imgSrc = newBsObj.find("img")["src"]

                    # urlretrieve(imgSrc, "{}/dst/{}".format(sys.path[0],format(sys.path[0])))
                    urlretrieve(
                        imgSrc, "{}/dst/{}".format(sys.path[0], filename))
                    store(filename)

conn.close()
sqlConnect.close()
