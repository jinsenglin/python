import unittest


class TestGmMethods(unittest.TestCase):
    def setUp(self):
        import apisvc

    def tearDown(self):
        # TODO
        pass

    def test_create_ring(self):
        from apisvc.managers.gm import Manager
        gm = Manager(role='admin', account='0000-0000-0000-0000')
        result = gm.create_ring(tenant_id='admin', account_id='u02', ring_type='user')
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
