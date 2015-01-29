# From http://anandology.com/blog/how-to-write-a-web-framework-in-python/

class application:
	def __init__(self, environ, start_response):
		self.environ = environ
		self.start_response = start_response

	# def __iter__(self):
	# 	status = '200 OK'
	# 	response_headers = [('Content-type', 'text/plain')]
	# 	self.start(status, response_headers)
	# 	yield 'Hello world!'

	def __iter__(self):
		path = self.environ['PATH_INFO']
		if path == '/':
			return self.GET_index()
		elif path == '/hello':
			return self.GET_hello()
		else:
			return self.notfound()

	def GET_index(self):
		status = '200 OK'
		response_headers = [('Content-type', 'text.plain')]
		self.start(status, response_headers)
		yield 'Welcome!'

	def GET_hello(self):
		status = '200 OK'
		response_headers = [('Content-type', 'text.plain')]
		self.start(status, response_headers)
		yield 'Hello world!'

	def notfound(self):
		status = '404 Not Found'
		response_headers = [('Content-type', 'text.plain')]
		self.start(status, response_headers)
		yield 'Not Found.'

if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	httpd = make_server('localhost', 8080, application)
	httpd.handle_request()