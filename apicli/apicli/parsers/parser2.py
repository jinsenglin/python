import argparse

parser = argparse.ArgumentParser(description='Example of nesting parsers')

subparsers = parser.add_subparsers(help='commands')

# A openstack command
openstack_parser = subparsers.add_parser('openstack', help='Proxy openstack commands')
openstack_parser.add_argument('command', action='store', help='Command to proxy')

# A kubectl command
kubectl_parser = subparsers.add_parser('kubectl', help='Proxy kubectl commands')
kubectl_parser.add_argument('command', action='store', help='Command to proxy')
