from flask import Blueprint, jsonify

common = Blueprint('common', __name__)


@common.route('/', methods=['GET'])
def index():
    return jsonify({"service": "Info Globo Backend Challenge",
                    "version": "1.0"})
