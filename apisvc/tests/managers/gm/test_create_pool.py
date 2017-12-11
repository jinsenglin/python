import unittest


class TestGmMethods(unittest.TestCase):
    def test_create_pool(self):
        import apisvc
        gm = apisvc.managers.gm.Manager(role='admin', account='0000-0000-0000-0000')
        result = gm.create_pool(tenant_id='t01')
        print(result)


if __name__ == '__main__':
    unittest.main()
