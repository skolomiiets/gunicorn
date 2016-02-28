
import urlparse

def app(env, start_response):
#    query = env[QUERY_STRING]
    query = urlparse.parse_qs(env['QUERY_STRING'], keep_blank_values=True)
#    for i, j in params.items():
#        return str(str(i) + '=' + str(j))\n
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    body = ["%s=%s\n" % (str(key),str(value))
         for key,value in query.items()]
    
    return iter(body)
