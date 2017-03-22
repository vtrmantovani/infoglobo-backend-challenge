# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from ibc import business

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/', methods=['GET'])
def index():
    file_name = 'feed.xml'
    business.create_update_file_xml(file_name)
    process_itens_xml = business.process_file_xml(file_name)
    feed = business.process_html_content(process_itens_xml)
    return jsonify(feed=feed)
