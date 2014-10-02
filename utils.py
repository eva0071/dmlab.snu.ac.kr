#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os

from settings import APP_STATIC


def read_csv_data(filename):
    filepath = os.path.join(APP_STATIC, 'data', filename)
    with open(filepath, 'r') as f:
        return [row.decode('utf-8').split(',')\
            for row in f.read().splitlines()]

def read_txt_data(filename):
    filepath = os.path.join(APP_STATIC, 'data', filename)
    with open(filepath, 'r') as f:
        return f.read().splitlines()
