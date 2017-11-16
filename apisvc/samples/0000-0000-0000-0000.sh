export OS_AUTH_URL=http://192.168.228.31:5000/v2.0/
export OS_TENANT_ID=5593c57c2c7b471788f0c25aee36e44f
export OS_TENANT_NAME="jimlin"
unset OS_PROJECT_ID
unset OS_PROJECT_NAME
unset OS_USER_DOMAIN_NAME
unset OS_INTERFACE
export OS_USERNAME="jimlin"
export OS_PASSWORD="jimlin"
export OS_REGION_NAME="RegionOne"
if [ -z "$OS_REGION_NAME" ]; then unset OS_REGION_NAME; fi
export OS_ENDPOINT_TYPE=publicURL
export OS_IDENTITY_API_VERSION=2
