import requests
import re
import csv
from lxml import etree

url = "https://shanghairanking.cn/rankings/bcur/202311"
resp = requests.get(url)
resp.encoding = 'utf-8'

# print(resp.text)
tree = etree.HTML(resp.text)
name = tree.xpath('//*[@id="content-box"]/div[2]/table/tbody/tr/td[2]/div/div[2]/div[1]/div/div/a/text()')

# print(name)
shengs = tree.xpath('//*[@id="content-box"]/div[2]/table/tbody/tr/td[3]/text()')
shengs_ = []
for sheng in shengs:
    sheng.strip()
    sheng = re.sub(r'\n', " ", sheng)
    sheng = re.sub(r' ', " ", sheng)
    # print(sheng)
    shengs_.append(sheng)
print(shengs_)
score = tree.xpath('//*[@id="content-box"]/div[2]/table/tbody/tr/td[5]/text()')

# print(score)
score = [scor.replace('\n', '').replace(' ', '') for scor in score]
print(score)
dics = []
for i in range(len(name)):
    dic = [name[i], shengs_[i], score[i]]
    dics.append(dic)
with open('data.csv', mode='w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(dics)
