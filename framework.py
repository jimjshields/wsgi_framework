# From http://anandology.com/blog/how-to-write-a-web-framework-in-python/

import re
import traceback

class WSGIapp:
	"""Base class for my WSGI application."""

	def __init__(self, environ, start_response):
		self.environ = environ
		self.start = start_response
		start.status = '200 OK'
		start._headers = []

	def header(self, name, value):
		self._headers.append((name, value))

	def __iter__(self):
		try:
			x = self.delegate()
			self.start(self.status, self._headers)
		except:
			headers = [('Content-type', 'text/plain')]
			self.start('500 Internal Error', headers)
			x = 'Internal Error:\n\n' + traceback.format_exec()

		if isinstance(x, str):
			return iter([x])
		else:
			return iter(x)

	def delegate(self):
		path = self.environ['PATH_INFO']
		method = self.environ['REQUEST_METHOD']

		for pattern, name in self.urls:
			m = re.match('^' + pattern + '$', path)
			if m:
				args = m.groups()
				func_name = method.upper() + "_" + name
				func = getattr(self, func_name)
				return func(*args)

		return self.not_found()

class Application(WSGIapp):

	urls = [
			("/", "index"),
			("/hello/(.*)", "hello")
	]

	def GET_index(self):
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		self.start(status, response_headers)
		yield 'Welcome!'

	def GET_hello(self, name):
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		self.start(status, response_headers)
		yield 'Hello %n!' % (name)

	def not_found(self):
		status = '404 Not Found'
		response_headers = [('Content-type', 'text/plain')]
		self.start(status, response_headers)
		yield 'Not Found.'

if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	httpd = make_server('localhost', 8080, application)
	httpd.handle_request()