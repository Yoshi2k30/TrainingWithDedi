import json
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S',
                    filename="./yossi_test/yos.log", level=logging.DEBUG)
Obj_storage = dict()


@app.route('/list', methods=['GET'])
def list_obj():
    logging.info("List was requested")
    return str(Obj_storage)
    # return "List"


@app.route('/save', methods=['POST'])
def save_obj():
    data = json.loads(request.data)
    # if data[Value]
    for _key, _value in data.items():
        if type(_value) == bool:
            message = '[{}] is not a valid value, expecting type of ID.'.format(_value)
            isError = True
            statusCode = 500
        else:
            Obj_storage.update(data)
            message = '[{}] has been saved to the list'.format(data)
            isError = False
            statusCode = 200

    logging.info(message)
    return jsonify(isError=isError,
                   message=message,
                   statusCode=statusCode), statusCode


@app.route('/get/<name>', methods=['GET'])
def get_obj(name):

    res_obj = None
    for Key, Value in Obj_storage.items():
        if Key == name:
            res_obj = str({Key: Value})

    if res_obj:
        message = '[{}] has been requested'.format(res_obj)
    else:
        message = 'could not find an Object with the name [{}]'.format(name)
        res_obj = jsonify(isError=True,
                          message=message,
                          statusCode=404), 404

    logging.info(message)

    return res_obj


if __name__ == '__main__':
    app.run(debug=True, port=1234)
