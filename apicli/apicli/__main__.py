from parsers.parser2 import parser
from httpclient import client


def main():
    args = parser.parse_args()
    print(args)
    client.put(endpoint=args.endpoint, role=args.role, user=args.user, cmd=args.subparser_name, arg=args.args_string)


if __name__ == '__main__':
    main()
