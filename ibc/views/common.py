from flask import Blueprint

common = Blueprint('common', __name__)


@common.route('/', methods=['GET'])
def home():
    return 'Info Globo Backend Challenge'
