import apisvc

gm = apisvc.managers.gm.Manager(role='admin', account='0000-0000-0000-0000')
result = gm.create_ring(tenant_id='admin', account_id='u00', ring_type='tenant')

print(result)