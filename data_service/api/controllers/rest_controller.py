from config import *
from data_processing.MainProcessing import MainProcessing
from flask import request



@cross_origin
@flask_app.route('/getData', methods=['GET'])
def getData():
    try:
        data = MainProcessing.getData()
        return {request.path: True, 'data': data}
    except Exception as e:
        return {request.path: False, 'data': e}