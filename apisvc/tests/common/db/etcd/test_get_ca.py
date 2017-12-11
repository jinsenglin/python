import unittest


class TestEtcdMethods(unittest.TestCase):
    def setUp(self):
        import apisvc

    def test_get_ca(self):
        from apisvc.common.db import etcd as DB
        v, k = DB.get_ca()
        self.assertIsNotNone(v)

if __name__ == '__main__':
    unittest.main()