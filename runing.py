#/usr/bin/python
#coding=utf-8

import sys,os
import tornado
import tornado.web
import tornado.options
import tornado.httpserver
from setting import LISTEN_HOST,LISTEN_PORT,IS_Multithreading
from blog import urls as blogurls


blogurls.append((r"/(favicon\.ico)",tornado.web.StaticFileHandler, dict(path = os.path.join(os.path.dirname(__file__),"static"))))

class Application(tornado.web.Application):
	def __init__(self):
		handlers = blogurls
		tornado.web.Application.__init__(self, handlers)
		
def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.bind(LISTEN_PORT, LISTEN_HOST)
	if IS_Multithreading == True:
		http_server.start(num_processes = 0)
	else:
		http_server.start() 
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()