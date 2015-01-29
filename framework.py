# From http://anandology.com/blog/how-to-write-a-web-framework-in-python/

class application:
	def __init__(self, environ, start_response):
		self.environ = environ
		self.start_response = start_response

	def __iter__(self):
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		self.start(status, response_headers)
		yield 'Hello world!'