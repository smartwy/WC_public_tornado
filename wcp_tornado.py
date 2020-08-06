#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    WC_public_tornado
#F-Name:    wcp_tornado.py
#Login:     Administrator   
#Descripton:
#__Author__  Smartwy
#Date:      2020/7/6 14:53:18
#Version:

'''
    
'''
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import torndb

from tornado.options import define, options
define('port', default=8000, help='run on the given port', type=int)

class Indexfun(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class echofun(tornado.web.RequestHandler):
	def post(self):
		v1 = self.get_argument('name')
		v2 = self.get_argument('gender')
		v3 = self.get_argument('age')
		self.render('info.html',v1=v1,v2=v2,v3=v3)

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/", Indexfun),(r'/exp',echofun)],
								  template_path=os.path.join(os.path.dirname(__file__),'templates'))
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()



















