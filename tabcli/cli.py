import requests
import argparse

BASE_URI = "http://localhost:5427"

def show_tabs(args):
    windows = make_request(BASE_URI).json()
    for window in windows['windows']:
        for tab in window['tabs']:
            print "%s\t%s\t%s" % (
                window['id'],
                tab['url'],
                tab['title'])

def make_request(endpoint, args=None):
    if args is None:
        args = {}
    return requests.get(endpoint, params=args)

def init_parser():
    parser = argparse.ArgumentParser(description='Interact with Chrome over the command line.')
    subparsers = parser.add_subparsers(help='sub-command help')

    ls_parser = subparsers.add_parser('ls', help='show tabs')
    ls_parser.add_argument('--verbose', type=bool, help='Show more tab information')
    ls_parser.set_defaults(func=show_tabs)
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    args.func(args)
