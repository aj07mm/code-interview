def format_url(*args):
	url = ''.join(args)
	if(args[-1][-1] == '/'):
		return url
	return url + '/'