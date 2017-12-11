import unittest


class TestFbiMethods(unittest.TestCase):
    def setUp(self):
        import apisvc

    def tearDown(self):
        # TODO
        pass

    def test_create_ring(self):
        from apisvc.managers.fbi import Manager
        fbi = Manager()
        result = fbi.create_ring(ring_type='tenant', account_id='t01', k8s_credential='dummy', os_credential='dummy')
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
