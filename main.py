import argparse
from poly import *

__author__ = 'Jervis Muindi'
# Date: May 2013
# Numerical Analysis and Algorithms
# Extra Credit
# Jenkins Traub Algorithm

def main():

    poly_help_msg = 'List of Coefficients of the polynomial to find the roots for. Start from the highest power and proceed in a descending order until the constant term. All coefficients must be specified and not skipped. The symbol \'j\' can be used to denote a complex number coefficient. Example:1+2j. Number coefficient must be separated by space. '

    parser = argparse.ArgumentParser(description='General Polynomial Root Solver. It applies the Jenkins-Traub Algorithm')
    parser.add_argument('-p', '--polynomial', nargs='+', type=complex, required=True,
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