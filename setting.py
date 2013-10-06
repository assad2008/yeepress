#/usr/bin/python
#coding=utf-8

from os import environ

LISTEN_HOST = '0.0.0.0'
LISTEN_PORT = 8888

WIP = '103.6.84.228'

DEBUG = False

if DEBUG == False:
	MAIN_DOMAIN = '36.coder.com'
else:
	MAIN_DOMAIN = '%s:%d' % (WIP,LISTEN_PORT)

JQUERY = "http://lib.sinaapp.com/js/jquery/1.6.2/jquery.min.js"
THEME = 'octopress'

BASE_URL = 'http://%s' % MAIN_DOMAIN

#Mysql db conf
MYSQL_DB = 'torblog'
MYSQL_USER = 'torblog'
MYSQL_PASS = 'torblog'
MYSQL_HOST_M = '127.0.0.1'
MYSQL_HOST_S = '127.0.0.1'
MYSQL_PORT = '3306'

MAX_IDLE_TIME = 5

HOT_TAGS_NUM = 10
LINK_NUM = 10

IS_Multithreading = False
