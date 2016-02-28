import urlparse

def app(env, start_response):
    query = QUERY_STRING
    body = urlparse.parse_qs(query, keep_blank_values=True)
    for i, j in params.items():
        return str(str(i) + '=' + str(j))\n
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return  [ body ]
