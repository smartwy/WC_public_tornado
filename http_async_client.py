#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    WC_public_tornado
#F-Name:    http_async_client.py
#Login:     Administrator
#Descripton:
#__Author__  Smartwy
#Date:      2020/7/9 10:02:51
#Version:

'''

'''

import tornado
import tornado.web
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define,options
define('port', default=8000, help='run on the given port', type=int)

class Indexfun(tornado.web.RequestHandler):
    @tornado.web.asynchronous  # 不关闭连接，也不发送响应
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://wthrcdn.etouch.cn/WeatherApi?city=北京市",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error:
            self.send_error(500)
        else:
            data = response.body.decode('UTF-8')
            if data:
                self.write(data)
            else:
                self.write("城市信息错误")
        self.finish()  # 发送响应信息，结束请求处理


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", Indexfun)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

# import tornado
# import tornado.web
# import tornado.httpclient
# import tornado.httpserver
# import tornado.ioloop
# import tornado.options
#
# from tornado.options import define,options
# define('port', default=8000, help='run on the given port', type=int)
#
# class Indexfun(tornado.web.RequestHandler):
#     async def get(self):
#         url = "http://wthrcdn.etouch.cn/WeatherApi?city=北京市"
#         http_client = tornado.httpclient.AsyncHTTPClient()
#         try:
#             response = await http_client.fetch(url)
#         except Exception as e:
#             self.write('error %s' % e)
#         else:
#             self.write(response.body)
#
#
# if __name__ == '__main__':
#     tornado.options.parse_command_line()
#     app = tornado.web.Application(handlers=[(r"/", Indexfun)])
#     http_server = tornado.httpserver.HTTPServer(app)
#     http_server.listen(options.port)
#     tornado.ioloop.IOLoop.current().start()

# tornado.gen实现生成器的协程

# import tornado
# import tornado.web
# import tornado.gen
# import tornado.httpclient
# import tornado.httpserver
# import tornado.ioloop
# import tornado.options
#
# from tornado.options import define,options
# define('port', default=8000, help='run on the given port', type=int)
#
# class Indexfun(tornado.web.RequestHandler):
#     @tornado.gen.coroutine
#     def get(self):
#         rep = yield self.get_info("北京市")
#         self.write(rep)
#
#     @tornado.gen.coroutine
#     def get_info(self, city):
#         http = tornado.httpclient.AsyncHTTPClient()
#         response = yield http.fetch("http://wthrcdn.etouch.cn/WeatherApi?city=" + city)
#         if response.code == 200:
#             rep = response.body
#         else:
#             rep = {'status': 'get data error !'}
#         # raise tornado.gen.Return(rep)  # 此处需要注意
#         return rep
#
# if __name__ == '__main__':
#     tornado.options.parse_command_line()
#     app = tornado.web.Application(handlers=[(r"/", Indexfun)])
#     http_server = tornado.httpserver.HTTPServer(app)
#     http_server.listen(options.port)
#     tornado.ioloop.IOLoop.current().start()

# @tornado.gen.coroutine
# def get(self):
#     http_client = AsyncHTTPClient()
#     response1, response2 = yield [http_client.fetch(url1),
#                                   http_client.fetch(url2)]