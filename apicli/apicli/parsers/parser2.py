import argparse


parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--endpoint', '-e', action="store", default='http://localhost:5080', help='default: http://localhost:5080')
parent_parser.add_argument('--role', '-r', action="store", default='admin', help='default: admin')
parent_parser.add_argument('--user', '-u', action="store", default='0000-0000-0000-0000', help='default: 0000-0000-0000-0000')


parser = argparse.ArgumentParser(description='apicli - apisvc command line', parents=[parent_parser])

subparsers = parser.add_subparsers(help='commands', dest='subparser_name')

# A openstack command
openstack_parser = subparsers.add_parser('openstack', help='proxy remote openstack command')
openstack_parser.add_argument('args_string', action='store', help='openstack command arguments, e.g., "project list"')

# A kubectl command
kubectl_parser = subparsers.add_parser('kubectl', help='proxy remote kubectl command')
kubectl_parser.add_argument('args_string', action='store', help='kubectl command arguments, e.g., "get ns"')
