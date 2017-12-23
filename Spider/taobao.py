#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: taobao.py
@Time: 2017/12/23 10:56
"""
"""
    查看淘宝的某一个商品的价格
    只用搜索的话，正则表达式更快
"""

import requests
import re


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parse_page(ilt, html):
    try:
        tlt = re.findall(r'"title"\:".*? "', html)
        plt = re.findall(r'"price"\:"[\d.]*"', html)
        for i in range(len(tlt)):

            # eval去掉包围在外面的引号
            price = eval(plt[i].split(":")[-1])
            title = eval(tlt[i].split(":")[-1])
            ilt.append([title, price])
    except:
        return ""


def print_info(ilt):
    tplt = "{:4}\t{:16}\t{:8}"
    print(tplt.format("序号", "商品", "价格"))
    count = 0
    for info in ilt:
        count += 1
        print(tplt.format(count, info[0], info[1]))


def main():
    goods = "手机"
    depth = 1   # 表示我们查的页数是多少
    start_url = "https://s.taobao.com/search?q=" + goods
    # 表示输出结果
    info_list = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(48 * i)
            html = get_html_text(url)
            parse_page(info_list, html)
        except:
            continue
    print_info(info_list)


if __name__ == '__main__':
    main()
