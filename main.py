from math import ceil, pi, sin, exp, sqrt

import sys
from poly import *


__author__ = 'Jervis Muindi'
# Date: April 2013
# Numerical Analysis and Algorithms
# Extra Credit
# Jenkins Traub Algorithm

def do_main(x0):
    """
        Main program code..
        x0 - coefficients of polynomial
    """
    print 'Using Polynomial with coefficents : %s' % str(x0)






def usage():
    #TODO(jervis): update this
    print '**************'
    print 'Jenkins Traub Polynomial Solver: '
    print 'Usage: '
    print 'python main.py [P]'
    print '     [P] : is comma separated list of coefficeints of polynomial to solve for. ' \
          'First number is the highest degree'
    print '\nExample: python main.py 1 2 3 4 5 \n'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def valid_inputs(x0):
    if not is_number(x0):
        'x-value must be a number : %s' % str(x0)
        return False
    else:
        return True

def main():
    arg_count = len(sys.argv) - 1
    if arg_count != 1:
        usage()
    else:
        x0 = sys.argv[1]
        if not valid_inputs(x0):
            print 'Invalid Input detected'
            print '************************'
            usage()
            exit(-1)
        else:
            x0 = float(x0)
            do_main(x0)


if __name__ == '__main__':
    x0 = 0.1
    main()