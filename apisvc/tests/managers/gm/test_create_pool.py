import unittest


class TestGmMethods(unittest.TestCase):
    def setUp(self):
        import apisvc

    def test_create_pool(self):
        from apisvc.managers.gm import Manager
        gm = Manager(role='admin', account='0000-0000-0000-0000')
        result = gm.create_pool(tenant_id='t01')
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
