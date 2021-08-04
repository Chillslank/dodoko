from bs4 import BeautifulSoup
import http.cookiejar as hc
import urllib

def weather():
    html_url="http://www.weather.com.cn/weather1d/201060100.shtml"
    limitation=500
    cj = hc.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('Host',"jd.com"),('User-agent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'),('Connection','Keep-Alive'),] 
    result = opener.open(html_url).read()
    soup = BeautifulSoup(result,'html.parser')
    tem = soup.select('.tem')
    print(tem[0].select('span')[0].string,end='/')
    print(tem[1].select('span')[0].string)
    return(tem[0].select('span')[0].string + '℃/' + tem[1].select('span')[0].string + '℃')

