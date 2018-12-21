from bs4 import BeautifulSoup
import requests
import csv
import time

url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

class FetchHouse:
    '''
    抓取房源

    '''
    def __init__(self):
        # 已完成的页数序号，初时为0
        self.page = 0

        self.csv_file = open("rent.csv", "w")
        self.csv_writer = csv.writer(self.csv_file, delimiter=',')

    def fetch(self):
        while True:
            time.sleep(1)
            self.page += 1
            print("fetch: ", url.format(page=self.page))
            response = requests.get(url.format(page=self.page))
            html = BeautifulSoup(response.text, features="html.parser")
            house_list = html.select(".list > li")

            # 循环在读不到新的房源时结束
            if not house_list:
                break

            for house in house_list:
                house_title = house.select("h2")[0].string
                house_url = "http://bj.58.com/%s" % (house.select("a")[0]["href"])
                house_info_list = house_title.split()

                # 如果第二列是公寓名则取第一列作为地址
                if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
                    house_location = house_info_list[0]
                else:
                    house_location = house_info_list[1]

                house_money = house.select(".money")[0].select("b")[0].string
                # 写一行数据
                self.csv_writer.writerow([house_title, house_location, house_money, house_url])

                self.csv_file.close()

fetchHouse =  FetchHouse()
fetchHouse.fetch()