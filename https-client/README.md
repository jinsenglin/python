# Fork

from https://blog.csdn.net/ns2250225/article/details/79528827

# Usage

```
python main.py
```

# In my case

```
import ssl
ssl._DEFAULT_CIPHERS = 'ALL'

import https # see https.py
https.HTTPSClientAuthHandler( 
    ssl_version = ssl.PROTOCOL_SSLv3,
    ciphers = 'EDH-RSA-DES-CBC-SHA' )
```

# About openssl

Mac OSX built-in

```
openssl version

OpenSSL 0.9.8zh 14 Jan 2016


# vagrant box :: bento/centos-7.4 v201801.02.0
# OpenSSL 1.0.2k-fips  26 Jan 2017
```

Does it support cipher suite 'EDH-RSA-DES-CBC-SHA' ?

```
openssl ciphers -v 'DEFAULT' | grep EDH-RSA-DES-CBC-SHA

# no result -> which means no support for 'EDH-RSA-DES-CBC-SHA' by default

openssl ciphers -v 'ALL' | grep EDH-RSA-DES-CBC-SHA

EDH-RSA-DES-CBC-SHA     SSLv3 Kx=DH       Au=RSA  Enc=DES(56)   Mac=SHA1
EXP-EDH-RSA-DES-CBC-SHA SSLv3 Kx=DH(512)  Au=RSA  Enc=DES(40)   Mac=SHA1 export


# vagrant box :: bento/centos-7.4 v201801.02.0
# DEFAULT : no
# ALL : no
```

# About python

Mac OSX built-in

```
python --version

Python 2.7.10


# vagrant box :: bento/centos-7.4 v201801.02.0
# Python 2.7.5
```

Does it support SSLv3 protocol?

```
import ssl
ssl.PROTOCOL_SSLv3

1

# vagrant box :: bento/centos-7.4 v201801.02.0
# 1
```

# About 192.168.120.200:443

Scan

```
nmap --script ssl-enum-ciphers -p 443 192.168.120.200
```

Output

```
Starting Nmap 7.70 ( https://nmap.org ) at 2018-04-16 20:46 CST
Nmap scan report for 192.168.120.200
Host is up (0.016s latency).

PORT    STATE SERVICE
443/tcp open  https
| ssl-enum-ciphers:
|   SSLv3:
|     ciphers:
|       TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA - E
|       TLS_DHE_RSA_WITH_DES_CBC_SHA (dh 2048) - E
|       TLS_RSA_EXPORT_WITH_DES40_CBC_SHA - E
|     compressors:
|       NULL
|     cipher preference: client
|     warnings:
|       64-bit block cipher DES vulnerable to SWEET32 attack
|       64-bit block cipher DES40 vulnerable to SWEET32 attack
|       CBC-mode cipher in SSLv3 (CVE-2014-3566)
|       Weak certificate signature: SHA1
|_  least strength: E

Nmap done: 1 IP address (1 host up) scanned in 1.06 seconds
```

# About 192.168.120.200:443

Scan

```
openssl s_client -connect 192.168.120.200:443 -ssl3
```

Output

```
SSL-Session:
    Protocol  : SSLv3
    Cipher    : EDH-RSA-DES-CBC-SHA
```

# Build openssl to support ECDHE-RSA-DES-CBC3-SHA

```
wget https://www.openssl.org/source/openssl-1.0.2o.tar.gz
tar -zxf openssl-1.0.2o.tar.gz
cd openssl-1.0.2o

./config enable-weak-ssl-ciphers enable-des

make depend
make install

/usr/local/ssl/bin/openssl ciphers -v 'ALL' | grep EDH-RSA-DES-CBC-SHA

EDH-RSA-DES-CBC-SHA     SSLv3 Kx=DH       Au=RSA  Enc=DES(56)   Mac=SHA1
EXP-EDH-RSA-DES-CBC-SHA SSLv3 Kx=DH(512)  Au=RSA  Enc=DES(40)   Mac=SHA1 export
```
