import urllib2
import urllib
import https
import ssl
import json

ssl._DEFAULT_CIPHERS = 'ALL'

#client_cert_key = "etcd-client-key.pem" # file path
client_cert_key = None
#client_cert_pem = "etcd-client.pem"     # file path 
client_cert_pem = None
#ca_certs = "etcd-ca.pem"                # file path
ca_certs = None

handlers = []

handlers.append( https.HTTPSClientAuthHandler( 
    key = client_cert_key,
    cert = client_cert_pem,
    ca_certs = ca_certs,
    #ssl_version = ssl.PROTOCOL_TLSv1,
    ssl_version = ssl.PROTOCOL_SSLv3,
    #ciphers = 'TLS_RSA_WITH_AES_256_CBC_SHA' ) )
    ciphers = 'EDH-RSA-DES-CBC-SHA' ) )

http = urllib2.build_opener(*handlers)

# request https
# GET
#resp = http.open('https://xxxx:2379/v2/members')
resp = http.open('https://192.168.120.200:443/')
data = resp.read()

'''
# POST
req = urllib2.Request(url)  
data = urllib.urlencode(data)
resp = http.open(req, data)

# PUT
request = urllib2.Request(url, data=json_data)
request.add_header('Content-Type', 'application/json')
request.get_method = lambda: 'PUT'
resp = http.open(request)

# DELETE
request = urllib2.Request(url, data=data)
request.get_method = lambda: 'DELETE'
resp = http.open(request)'''

resp.close()