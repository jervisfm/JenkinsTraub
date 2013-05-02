from math import ceil, pi, sin, exp, sqrt

import sys



__author__ = 'Jervis Muindi'
# Date: April 2013
# Numerical Analysis and Algorithms
# Homework 13

def f(x):
    """
        The function we're finding roots for.
        You can change it something else (i.e. redefine it) if you'd like to solve a different problem.
        Remember to also update the df(x) derivative function as well.
    """
    return float((x ** 20) - 1)

def df(x):
    """
        This is the derivative of the function we're finding roots for
    """
    return float(20 * (x ** 19))


def next_x_netwon(x):
    """
        Finds the next number using netwon iteration formula
    """
    return x - (f(x) / df(x))

def u(x):
    """
        Ratio of f(x) and f'(x) - i.e. f(x) / f'(x)
    """
    return f(x) / df(x)

def next_point_iteration(x):
    """
        Finds the next number usign 3-point iteration Formula.

        3-point iteration is defined as follows:
	    x_(i+1) = x_i -u(x_i) + (u(x_i) * f(x_i - u(x_i))) / ( 2*f(x_i - u(x_i))  - f(x_i) )

        where u(x_i) is:
	        u(x_i) = f(x_i) / f'(x_i)
    """

    a = x
    b = u(x)
    numerator = u(x) * f(x - u(x))
    denominator = 2 * f(x - u(x)) - f(x)

    #print 'u(x) = %f' % (u(x))
    #print 'f(x - u(x)) = %f' % (f(x - u(x)))
    #print 'x = %f | dem=%f' % (x,denominator)

    try:
        return a - b + numerator / denominator
    except ZeroDivisionError:
        # Due to nature of formula (in the denominator), this would only occur
        # when we're _very_ close to a true root if not
        # there already.
        return x









def do_main(x0):
    """
        Main program code..
        x0 - initial x-point.
    """
    print 'Using Initial X-value : %s' % str(x0)
    print 'Finding Roots using both Newton Iteration and 3-point Iteration'


    LIMIT = 10 ** 9 # Maximum number of loop iterations
    MIN_PROGRESS = 10 ** (-3) # Minimum amount of progress we should make at each step
    count = 1


    x = x0
    prev_x = x0

    newton_x = x0
    point_iter_x = x0

    while  True:
            # Stop if we exceed our iteration limit
            if count > LIMIT:
                print 'Stopping Iteration. Loop Limit Reached: %d' % LIMIT
                break

            # Compute the Next Points
            try:
                next_newton = next_x_netwon(newton_x)
                next_iter_point = next_point_iteration(point_iter_x)
            except OverflowError:
                print 'Floating Overflow occurred. Stopping Iteration. Latest X-values are:'
                print '%d) Newton=%.15f | 3-Point-Iteration=%.15f' % (count, newton_x, point_iter_x)
                break

            # Print the Current Results
            print '%d) Newton=%.15f | 3-Point-Iteration=%.15f' % (count, next_newton, next_iter_point)

            # Stop if we didn't make progress on either
            step_newton = abs(next_newton - newton_x)
            step_iter = abs(next_iter_point - point_iter_x)
            max_step = max(step_newton, step_iter)
            if max_step < MIN_PROGRESS:
                print "Stopping Iteration. We're progressing slower than %f per loop" % MIN_PROGRESS
                break

            # Update the loop count and x-points
            count += 1
            newton_x = next_newton
            point_iter_x = next_iter_point



def usage():
    print '**************'
    print 'General Root Solver : '
    print 'Usage: '
    print 'python main.py [x0]'
    print '     x0 : initial x-point to use.'
    print '\nExample: python main.py 0.98 \n'

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
    #do_main(x0)
    main()