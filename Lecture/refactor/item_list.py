from bs4 import BeautifulSoup as bs
from urllib.request import urlopen


class ItemList:

    pass


if __name__ == "__main__":
    krx_url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method=download'
    konex = krx_url + '&marketType=konexMkt'
    kospi = krx_url + '&marketType=stockMkt'
    kosdaq = krx_url + '&marketType=kosdaqMkt'
    item_data = []
    for title in [konex, kosdaq, kospi]:
        print(title)
        item_list = bs(urlopen(title), 'html.parser').find_all('tr')
        headers = [name.get_text() for name in item_list[0].findChildren()]
        for i in range(1, len(item_list)):
            item_data.append([ele for ele in zip(headers, [name.get_text() for name in item_list[i].findChildren()])])
    print(len(item_data))

    # print(item_list[0])

    # item_list = bs(urlopen(kospi), 'html.parser').find_all('tr')
    # header = item_list[0]
    # headers = []
    # for ele in header.findChildren():
    #     headers.append(ele.get_text())
    # print(headers)
    # item_data = []
    # pk = 0
    # for i in range(1, len(item_list)):
    #     idx = 0
    #     data = {}
    #     for ele in item_list[i].findChildren():
    #         data[headers[idx]] = ele.get_text()
    #         idx += 1
    #     item_data.append(data)
