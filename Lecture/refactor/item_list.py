from bs4 import BeautifulSoup as bs
from urllib.request import urlopen


class ItemList:

    pass


if __name__ == "__main__":
    krx_url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method=download'
    konex = krx_url + '&marketType=konexMkt'
    kospi = krx_url + '&marketType=stockMkt'
    kosdaq = krx_url + '&marketType=kosdaqMkt'
    tot = 0
    for title in [konex, kosdaq, kospi]:
        html = urlopen(title)
        item_list = bs(html, 'html.parser').find_all('tr')
        tot += len(item_list)
        print(len(item_list))
    print(tot)
    # print(item_list[0])
