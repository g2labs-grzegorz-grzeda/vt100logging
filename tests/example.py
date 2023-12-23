from argparse import ArgumentParser
from vt100logging import vt100logging_init, D, I, W, E


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
                        default=False, help='verbose mode')
    args = parser.parse_args()
    return args


def log_example_data():
    D('example DEBUG message')
    I('example INFO message')
    W('example WARNING message')
    E('example ERROR message')


def main():
    args = parse_args()
    vt100logging_init('example', args.verbose)
    if not args.verbose:
        I("If you don't see the DEBUG log, try to run this script with '-v' option.")
    log_example_data()


if __name__ == '__main__':
    main()
