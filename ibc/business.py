# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import requests
import xml.dom.minidom

from flask import current_app as app


def create_update_file_xml(file_name):
    response = requests.get(app.config['FEED_URL'],  timeout=app.config['FEED_TIMEOUT'])
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(response.text)
        f.close()


def process_file_xml(file_name):
    list_itens = []
    DOMTree = xml.dom.minidom.parse(file_name)
    collection = DOMTree.documentElement
    items = collection.getElementsByTagName("item")

    for item in items:
        title_data = item.getElementsByTagName('title')[0]
        title = title_data.childNodes[0].data
        description_data = item.getElementsByTagName('description')[0]
        description = description_data.childNodes[0].data
        link_data = item.getElementsByTagName('link')[0]
        link = link_data.childNodes[0].data
        list_itens.append({"title": title, "link": link, "description": description})

    return list_itens


def process_html_content(process_itens_xml):
    list_itens = []
    for test in process_itens_xml:
        content = []
        description_xml = test["description"]
        soup = BeautifulSoup(description_xml, 'html.parser')

        p_itens = soup.find_all('p')
        img_itens = soup.find_all('img')
        uls = soup.find_all('ul')
        lis = [li for ul in uls for li in ul.findAll('li')]
        links = [a for li in lis for a in li.findAll('a')]
        links_a = [link.get('href') for link in links]

        for item in p_itens:
            cleanr = re.compile("<.*?>")
            cleantext = re.sub(cleanr, '', str(item))
            text_content = cleantext.replace("\n", '').replace('\t', '').replace(" ", '')
            if text_content:
                content.append({
                    "type": "text",
                    "content": text_content
                })
        for item in img_itens:
            content.append({
                "type": "image",
                "content": item.get("src")
            })

            content.append({
                "type": "links",
                "content": links_a
            })

        list_itens.append({"item": {"title": test["title"], "link": test["link"], "description": content}})

    return list_itens
