#!/usr/bin/env python

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import Parrot

def PrintTerms():
    pass

def PrintSolvers():
    pass

HELP = {
    'debug'
}

def main():
    parser = ArgumentParser(description=__doc__,
                            format_class=RawDescriptionHelpFormatter)
    parser.add_argument('--version',action='version',
                        version='%(prog)s ' + Parrot.__version__)

if __name__ == '__main__':
    main()