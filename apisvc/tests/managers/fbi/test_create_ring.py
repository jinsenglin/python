import unittest


class TestFbiMethods(unittest.TestCase):
    def test_create_ring(self):
        import apisvc
        fbi = apisvc.managers.fbi.Manager()
        result = fbi.create_ring(ring_type='tenant', account_id='t01', k8s_credential='dummy', os_credential='dummy')
        print(result)


if __name__ == '__main__':
    unittest.main()
