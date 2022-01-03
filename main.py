import re
import sys
import urllib.error
import urllib.request


def main():
    baseurl = "http://mana.daa.ink/bible/"
    getData(baseurl)


def getData(baseurl):
    for i in range(1, 1190):
        if i < 10:
            url = baseurl + "000" + str(i) + ".html"
        elif i < 100:
            url = baseurl + "00" + str(i) + ".html"
        elif i < 1000:
            url = baseurl + "0" + str(i) + ".html"
        else:
            url = baseurl + str(i) + ".html"
        print(url)
        html = askURL(url)
        getMP4(html, "/Users/lyb/Desktop/bible/" + str(i))
        # saveHTML("/Users/lyb/Desktop/bible/" + str(i), html)


def saveHTML(file_name, file_content):
    with open(file_name + ".html", "wb") as f:
        f.write(file_content)


def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
        # html = response.read().decode("UTF-8")
        html = response.read()
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def callbackfunc(blocknum, blocksize, totalsize):
    global url
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    downsize = blocknum * blocksize
    if downsize >= totalsize:
        downsize = totalsize
    s = "%.2f%%" % percent + "====>" + "%.2f" % (downsize / 1024 / 1024) + "M/" + "%.2f" % (
                totalsize / 1024 / 1024) + "M \r"
    sys.stdout.write(s)
    sys.stdout.flush()
    if percent == 100:
        print('')


def getMP4(html, filename):
    r = r'http://.*?\.mp4'
    re_mp4 = re.compile(r)
    html = html.decode('utf-8')
    mp4List = re.findall(re_mp4, html)
    for mp4url in mp4List:
        urllib.request.urlretrieve(mp4url, '%s.mp4' % filename, callbackfunc)
        print("file %s.mp4 done" % filename)


if __name__ == '__main__':
    main()
