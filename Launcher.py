#!/usr/bin/env python

from argparse import ArgumentParser, RawDescriptionHelpFormatter

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
    parser

if __name__ == '__main__':
    main()