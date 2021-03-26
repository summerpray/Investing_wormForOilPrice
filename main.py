import time
import requests
import re

"""请求网页"""

"""反反爬"""
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

response = requests.get('https://cn.investing.com/commodities/crude-oil',headers=headers)
# print(response.request.headers)
html = response.text

"""解析网页"""
oil_price = re.findall('<span class="arial_26 inlineblock pid-8849-last" id="last_last" dir="ltr">(.*?)</span>', html)
change_price = re.findall('<span class="arial_20 greenFont   pid-8849-pc" dir="ltr">(.*?)</span>', html)
change_persent = re.findall('<span class="arial_20 greenFont  pid-8849-pcp parentheses" dir="ltr">(.*?)</span>', html)
print(oil_price)
print(change_price)
print(change_persent)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))