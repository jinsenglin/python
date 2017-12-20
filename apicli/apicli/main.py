from parsers.parser2 import parser
from httpclient import client


def main():
    args = parser.parse_args()
    client.put(cmd=args.subparser_name, arg=args.command)


if __name__ == '__main__':
    main()
