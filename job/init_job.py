#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import logging
import pymysql
import os.path
import sys

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current, os.pardir))
sys.path.append(cpath)
import instock.lib.database as mdb
import data_fetcher
import push

__author__ = 'myh '
__date__ = '2023/3/10 '


# main函数入口
if __name__ == '__main__':
    pass
