#/usr/bin/python3.4
import urlparse

def app(env, start_response):
#    query = env[QUERY_STRING]
    query = urlparse.parse_qs(env['QUERY_STRING'], keep_blank_values=True)
#    for i, j in params.items():
#        return str(str(i) + '=' + str(j))\n
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    nobody = ""

    for key, value in body.items():
        if type(value) is list:
            for i in value:
                nobody = nobody + key + "=" + str(i) + "\n"
        else:
            nobody = nobody + key + "=" + str(value) + "\n"    

    
    return [nobody]
