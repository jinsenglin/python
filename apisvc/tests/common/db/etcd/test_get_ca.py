import unittest


class TestStringMethods(unittest.TestCase):
    def test_get_ca(self):
        import apisvc
        from apisvc.common.db import etcd as DB
        v, k = DB.get_ca()
        print(v)
        print(k)

if __name__ == '__main__':
    unittest.main()