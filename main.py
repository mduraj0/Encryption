import argparse, getpass
import pathlib
from argparse import ArgumentParser, Namespace
from typing import Sequence
from encryption import Encryption, Decryption


class Password(argparse.Action):
    def __call__(self, parser, namespace, values, optional_string):
        if values is None:
            values = getpass.getpass()

        setattr(namespace, self.dest, values)


def file_name(value: str):
    if value.endswith(('.txt', '.dokodu')):
        return value
    raise argparse.ArgumentError()


def main(args):
    try:
        for file in args.file:
            if args.mode == 'encrypt':
                path = pathlib.Path(file)
                action = Encryption(path)
                action.execute(args.password)
            elif args.mode == 'decrypt':
                path = pathlib.Path(file)
                action = Decryption(path)
                action.execute(args.password)
    except InvalidToken:
        print('Bad password!! ERROR')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decrypt encrypt app')
    parser.add_argument(
        '-m',
        '--mode',
        choices=['encrypt', 'decrypt', 'append'],
        required=True,
        help='''encrypt --- encrypt file
    decrypt --- decrypt file
    append --- append text to encrypted file'''
    )

    parser.add_argument(
        '-p',
        '--password',
        required=True,
        nargs='?',
        dest='password',
        action=Password
    )

    parser.add_argument('-v', '--verbose', action='count', default=0)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', action='append', type=file_name, help='list of files to process.')
    group.add_argument('-d', '--dir', help='path to folder with file to process')

    args = parser.parse_args()
    main(args)
