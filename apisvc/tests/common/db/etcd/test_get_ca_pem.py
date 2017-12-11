import unittest


class TestStringMethods(unittest.TestCase):
    def test_get_ca_pem(self):
        import apisvc
        from apisvc.common.db import etcd as DB
        v, k = DB.get_ca_pem(target='crt')
        print(v)
        print(k)
        v, k = DB.get_ca_pem(target='key')
        print(v)
        print(k)

if __name__ == '__main__':
    unittest.main()