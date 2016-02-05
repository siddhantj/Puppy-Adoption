#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import flask_app


def get_connection_info():
    host = '0.0.0.0'
    port = 5000
    return host, port


if __name__ == '__main__':
    flask_app.secret_key = '\xbc\xcc+\x90\x8f\x15]\xd4\xbc\x05\xdaQs\xbf\xce\x1eT\xc79\x04\x14g}\xe2'
    flask_app.debug = True
    host, port = get_connection_info()
    flask_app.run(host, port)




