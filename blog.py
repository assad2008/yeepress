#/usr/bin/python
#coding=utf-8

import os
import json
from hashlib import md5
from time import time
from model import Article, Comment, Link, Category, Tag
from common import BaseHandler, unquoted_unicode, quoted_string, safe_encode

class HomePage(BaseHandler):
	def get(self):
		self.write('hello world')
	
class PostDetail(BaseHandler):
	def get(self):
		pass
		
class PostList(BaseHandler):
	def get(self):
		pass
		
class CategoryPostList(BaseHandler):
	def get(self):
		pass
		
class TagPostList(BaseHandler):
	def get(self):
		pass
		
class Attachments(BaseHandler):
	def get(self):
		pass
		
class Robots(BaseHandler):
	def get(self):
		 self.echo('robots.txt')
		
class Feed(BaseHandler):
	def get(self):
		pass

urls = [
    (r"/", HomePage),
    (r"/robots.txt", Robots),
    (r"/feed", Feed),
    (r"/post/(\d+)/(.*)$", PostDetail),
    (r"/page/(\d+)/$", PostList),
    (r"/category/(.+)/$", CategoryPostList),
    (r"/tag/(.+)/$", TagPostList),
    (r"/attachment/(.+)$", Attachments),
]