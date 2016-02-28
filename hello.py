import urlparse

def app(env, start_response):
#    query = env[QUERY_STRING]
    body = urlparse.parse_qs(env['QUERY_STRING'], keep_blank_values=True)
#    for i, j in params.items():
#        return str(str(i) + '=' + str(j))\n
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return  iter([ body ])
