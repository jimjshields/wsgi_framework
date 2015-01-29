# From http://anandology.com/blog/how-to-write-a-web-framework-in-python/

def application(environ, start_response):
	"""Simplest possible application object."""

	status = '200 OK'
	response_headers = [('Content-type', 'text/plain')]
	start_response(status, response_headers)
	return ['Hello world!']