#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    WC_public_tornado
#F-Name:    tornado_db_test.py
#Login:     Administrator   
#Descripton:
#__Author__  Smartwy
#Date:      2020/7/8 11:59:09
#Version:

'''
    
'''
import os.path
import tornado
import tornado.web
import torndb

from tornado.options import define, options
define('port', default=8000, help='run on the given port', type=int)

class Indexfun(tornado.web.RequestHandler):
	def get(self, *args, **kwargs):
		ret = self.application.db.query('select * from students')
		self.render('db_echo.html',data = ret)

if __name__ == '__main__':
	options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/", Indexfun)],
								  template_path=os.path.join(os.path.dirname(__file__),'templates'))
	app.db = torndb.Connection(
		host='127.0.0.1',
		database='wcp',
		user='root',
		password='12345678'
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()

