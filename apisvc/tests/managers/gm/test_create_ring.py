import unittest


class TestGmMethods(unittest.TestCase):
    def test_create_ring(self):
        import apisvc
        gm = apisvc.managers.gm.Manager(role='admin', account='0000-0000-0000-0000')
        result = gm.create_ring(tenant_id='admin', account_id='u02', ring_type='user')
        print(result)


if __name__ == '__main__':
    unittest.main()
