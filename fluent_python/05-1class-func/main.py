# @Author: u14e
# @Time  : 2019/6/3 13:58
# @description:
from flask import Flask, jsonify, request
import inspect

app = Flask(__name__)


def auth_param_func(username, password, **kwargs): pass


def valid_auth_empty(func, form):
    sig = inspect.signature(func)
    try:
        sig.bind(**form)
    except TypeError as e:
        return 'form data is not full'
    else:
        return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = request.get_json() or {}
    err = valid_auth_empty(auth_param_func, form)
    if err is not None:
        res = jsonify({'detail': err})
        res.status_code = 400
    else:
        res = jsonify({'success': 'ok'})
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
