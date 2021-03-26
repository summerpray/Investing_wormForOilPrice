import investpy
import requests

"""请求网页"""

"""反反爬"""
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

response = requests.get('https://cn.investing.com/commodities/crude-oil',headers=headers)
# print(response.request.headers)
html = response.text

"""解析网页"""
