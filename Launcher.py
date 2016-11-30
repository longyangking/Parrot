#!/usr/bin/env python

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import Parrot

def PrintTerms():
    pass

def PrintSolvers():
    pass

HELP = {
    'debug':'Start debugger when an exception is raised'
    'list':'List data, what can be one of: {terms, solvers}'
}

def main():
    parser = ArgumentParser(description=__doc__,format_class=RawDescriptionHelpFormatter)
    parser.add_argument('--version',action='version',version='%(prog)s ' + Parrot.__version__)
    parser.add_argument('--debug',action='store_true',dest='debug',default=False,help=HELP['debug'])

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list',metavar='what',action='store',dest='_list',default=None,help=HELP['list'])
    group.add_argument('filename_in',nargs='?')
    options = parser.parse_args()

    if options._list is not None:
        if options._list == 'terms':
            PrintTerms()
        elif options._list == 'solvers':
            PrintSolvers()

        return
    
    if option.debug:
        pass #Import debuger from Parrot
    
    filename_in = options.filename_in


if __name__ == '__main__':
    main()