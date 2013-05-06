from math import ceil, pi, sin, exp, sqrt

import sys
import argparse
from poly import *


__author__ = 'Jervis Muindi'
# Date: May 2013
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

    poly_help_msg = 'List of Coefficients of the polynomial to find the roots for. Start from the highest power and proceed in a descending order until the constant term. All coefficients must be specified and non skipped'

    parser = argparse.ArgumentParser(description='General Polynomial Root Solver. It applies the Jenkins-Traub Algorithm')
    parser.add_argument('-p', '--polynomial', nargs='+', type=float, required=True,
                        help=poly_help_msg)
    parser.add_argument('-e', '--error', type=float)

    args = vars(parser.parse_args())
    poly_coeff = args['polynomial']

    err = 10 ** (-6) # Default Error Values
    if args['error']:
        err=args['error']


    poly_pow = len(poly_coeff) - 1
    poly = Poly(poly_pow, poly_coeff)

    print 'Finding Roots for the Polynomial:\n %s\n' % poly.pretty_string()
    print 'Using Error Value of: %s\n' % err


    print 'Starting Root Search ...'
    ans = solve_poly_jt(poly)
    print 'Root Search Complete'

    print '\n*********************\n'
    print 'For The Polynomial\n%s\nThe roots found in order of increasing magnitude are:' % poly.pretty_string()
    counter = 1
    for root in ans:
        print  '%d) %s' % (counter, root)
        counter += 1



if __name__ == '__main__':
    main()