
__author__ = 'Jervis Muindi'

import random
import cmath
import math

class Poly:
    """
        Represents a polynomial
        With non-negative powers of x
    """
    def __init__(self, pow=0, coeff=[0]):
        """
            Creates a new polynomial
            pow - the highest degree of the polynomial
            coeff - is a listing of (complex) coefficients.
            The first element of this list represents the coefficient of highest x-term in the polynomial
            The last element of this list should represent the constant term.
            Note that all the coefficients should be in the list - if they do have a value, they should be set to 0.
        """
        if (pow != len(coeff) - 1):
            raise ValueError('There is mismatch between power of polynomial and coeffiecnts: %s vs %s' % (pow, coeff))

        self.coeff = []
        # Make a Copy of Values
        for x in coeff:
            self.coeff.append(x)


    def eval(self, x):
        result = 0
        curr_pow = self.highest_degree()
        for c in self.coeff:
            result += c * (x ** curr_pow)
            curr_pow -= 1
        return result


    def get_copy(self):
        """
            Returns a copy of this polynomial
        """
        result = []
        for x in self.coeff:
            result.append(x)
        return Poly(self.highest_degree(), result)

    def highest_degree(self):
        return len(self.coeff) - 1

    def size(self):
        return len(self.coeff)


    def __eq__(self, other):
        if  (self.size() != other.size()):
            return False
        else:
            size = self.size()
            for i in xrange(size):
                if (self.coeff[i] != other.coeff[i]):
                    return False
            return True

    def __str__(self):
        s = '| '
        pow = self.highest_degree()
        for x in self.coeff:
            s += '(%s,%s), ' % (x, pow)
            pow -= 1
        s += ' | '
        return s

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        """
            Add the two polynomials non-destructively
        """
        big_poly = None
        small_poly = None
        equal_size_poly = False
        if (self.size() > other.size()):
            big_poly = self
            small_poly = other
        elif (self.size() < other.size()):
            big_poly = other
            small_poly = self
        else: # they are equal in size
            equal_size_poly = True

        if (equal_size_poly):
            result = []
            size = self.size()
            for i in xrange(size):
                val = self.coeff[i] + other.coeff[i]
                result.append(val)
            return Poly(self.highest_degree(), result)
        else:
            result = []
            big_poly_size = big_poly.size()
            small_poly_size = small_poly.size()
            # A sample addition looks like this:
            # [10][20][30][40] - big poly
            #         [55][66] - small poly.
            for i in xrange(big_poly_size):
                big_poly_reverse_idx = (big_poly_size - 1) - i
                small_poly_reverse_idx = (small_poly_size -1) - i
                if (small_poly_reverse_idx < 0):
                    val = big_poly.coeff[big_poly_reverse_idx]
                    result.append(val)
                else:
                    val = big_poly.coeff[big_poly_reverse_idx] + small_poly.coeff[small_poly_reverse_idx]
                    result.append(val)
            result.reverse()
            return Poly(big_poly.highest_degree(), result)


    def get_derivative(self):
        """
            Computes the derivative of this polynomial
        """
        result = []
        size = self.size()

        for i in xrange(size - 1): # skip constant term
            curr_deg = self.get_power_at_index(i)
            curr_coeff = self.get_x_power_coeff(curr_deg)
            new_coeff = curr_deg * curr_coeff
            result.append(new_coeff)
        new_power = self.highest_degree() - 1 # derivative will be one power lower
        if new_power < 0:
            new_power = 0
        return Poly(new_power, result)




    def get_highest_degree_of_non_zero_coeff(self):
        """
            Get the degree of the highest term with a non-zero coefficient.
            If all coefficients are zero (polynomial is empty) - then None is returned.
        """
        i = 0
        for coeff in self.coeff:
            if coeff != 0:
                return self.get_power_at_index(i)
            i += 1
        return None

    def get_cauchy_poly(self):
        """
            Returns the Cauchy Polynomial from this polynomial
        """
        first_idx = 0
        last_idx = self.size() - 1
        size = self.size()
        result = []

        do_normalize = False
        norm_const = 0
        for i in xrange(size):
            if i == first_idx:
                val = self.coeff[i]
                if val != 1:
                    do_normalize = True
                    norm_const = val
                result.append(1)
            elif i == last_idx:
                val = self.coeff[i]
                if do_normalize:
                    val /= 1.0 * norm_const
                val = -abs(val)
                result.append(val)
            else:
                val = self.coeff[i]
                if do_normalize:
                    val /= 1.0 * norm_const
                val = abs(val)
                result.append(val)
        return Poly(self.highest_degree(), result)


    def divide_linear_poly(self, x_coeff, x_const):
        """
            Divides this polynomial by given linear (1-degree_ polynomial
            x_coeff - coefficient of the (x-)term
            x_const - constant term
        """

        quotient = get_empty_poly(1)
        remainder = self.get_copy()

        num_iterations = remainder.highest_degree()
        dividend_idx = 0
        curr_deg = remainder.highest_degree()
        result = []
        for i in xrange(num_iterations):
            quotient_coeff = float(remainder.coeff[dividend_idx]) / x_coeff
            result.append(quotient_coeff)
            term = Term(quotient_coeff,curr_deg - 1)
            poly_term = term.multiply_linear_poly(x_coeff, x_const)
            remainder = remainder.__sub__(poly_term)

            # zero out the highest term just in case we still have residuals
            remainder.set_coeff_at_x_power(curr_deg, 0)

            dividend_idx += 1
            curr_deg -= 1

        return Poly(self.highest_degree() - 1, result)
    def __sub__(self, other):
        """
            Does polynomial subtraction in a non-destructive manner.
            Computes this - other
            other - the polynomial to substraction
        """
        neg_poly = other.negate()
        return self.__add__(neg_poly)

    def negate(self):
        """
            Negates this polynomial.
            Does so non-destructively
        """
        result = []
        for x in self.coeff:
            result.append(-x)
        return Poly(self.highest_degree(), result)


    def const_mult(self, c):
        """
            Multiplies through this polynomial by the given constant
            c - constant to multiply
        """
        result = []
        for x in self.coeff:
            val = c * x
            result.append(val)
        return Poly(self.highest_degree(), result)

    def get_power_at_index(self, i):
        """
            Translate the index value to an x-power value
            (i.e. the value of term degree at given position)
            i - the index (0-based)
        """
        max_index = self.size() - 1
        if i < 0 or i > max_index:
            raise ValueError('Invalid index: %s', i)
        max_degree = self.highest_degree()
        return max_degree - i


    def get_x_power_coeff(self, pow):
        """
            Returns the coefficeint of the given x-power
        """
        max_pow = self.highest_degree()
        if pow > max_pow:
            raise ValueError('Invalid Power Arguemnt: %s' % str(pow))
        elif pow < 0:
            raise ValueError('This polynomial does not support negative x-powers')
        else: # it's some other number
            last_idx = self.size() - 1
            pos = last_idx - pow
            return self.coeff[pos]

    def set_coeff_at_x_power(self, pow, val):
        """
            Sets the coefficient of an x-term of given power to the given value
            pow - power of x term
            val - new value of this x-term

            Note that the given power must exist or an error will be thrown
        """
        max_pow = self.highest_degree()
        if pow > max_pow:
            raise ValueError('Invalid Power: %s' % pow)
        elif pow < 0:
            raise ValueError('Negative power arg given: %s' % pow)
        else:
            last_idx = self.size() - 1
            pos = last_idx - pow
            self.coeff[pos] = val
            return self


class Term:
    def __init__(self, coeff=0, deg=0):
        """
            Creates a new term
            deg - degree of the term
            coeff - coefficient of the
        """
        if deg < 0:
            raise ValueError("Degree cannot be negative")
        self.deg = deg
        self.coeff = coeff

    def __str__(self):
        return '(%s,%s)' % (self.coeff, self.pow)
    def __repr__(self):
        return self.__str__()

    def multiply_linear_poly(self, x_coeff, x_const):
        """
            Multiplies this term with the provided linear (1-degree) polynomial
            x_coeff - coefficient of the x^1 term
            x_const - coefficient of the x^0 term

            Returns a Polynomial object
        """
        new_poly_deg = self.deg + 1
        poly = get_empty_poly(new_poly_deg)
        highest_term_coeff = x_coeff * self.coeff
        second_highest_term_coeff = x_const * self.coeff

        poly.set_coeff_at_x_power(new_poly_deg, highest_term_coeff)
        poly.set_coeff_at_x_power(new_poly_deg - 1, second_highest_term_coeff)
        return poly



def get_empty_poly(deg):
    """
    Creates a new empty polynomial of the given degree
    """
    if deg < 0:
        raise ValueError('Invalid polynomial degree')
    size = deg + 1
    result = []
    for _ in xrange(size):
        result.append(0)
    return Poly(deg, result)

def solve_poly_newton(poly, err):
    """
        Find root of given polynomial by apply newton iteration

        poly - is the polynomial to use
        err - is the maximum error permitted in answer
    """
    x = random.uniform(0,1)
    diff_poly = poly.get_derivative()
    while abs(poly.eval(x)) > abs(err):
        x = x - (poly.eval(x) / float(diff_poly.eval(x)))
    return x


def get_initial_s(poly):
    cauchy_poly = poly.get_cauchy_poly()
    err = 10 ** (-5)

    beta = solve_poly_newton(cauchy_poly, err)
    rand = random.uniform(0,1) * math.pi
    return abs(beta) * cmath.exp(1j * rand)


