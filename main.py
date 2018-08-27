import requests
import os
import codecs
import json
from bs4 import BeautifulSoup

def find_more_url(url):
    response = requests.get(url)
    temp = response.text.split('"')


    for item in temp:
        if("http" in item):
            write_file("website.txt", item+"\n")



def get_url_info(url):
    filename = "item_url.txt"
    response = requests.get(url)

    # print(response.text)

    temp = response.text.split('"')


    for item in temp:
        if("http://ragial.org/item/iRO-Renewal/" in item):
            print(item)
            # if(check_file(filename, item)):
            write_file(filename, item+"\n")

def check_file(filename, info):
    file = open(filename,'r')
    if(info in file.read()):
        return True
    else:
        return False

def write_file(filename, info):
    file = codecs.open(filename, 'a')
    file.write(info)

if __name__ == '__main__':
    # get_url_info("http://ragial.org/vending/iRO-Renewal")
    for i in range(0,100):
        get_url_info("http://ragial.org/vending/iRO-Renewal"+"/"+str(i))
    # find_more_url("http://ragial.org/vending/iRO-Renewal")
