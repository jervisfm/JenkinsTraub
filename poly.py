
__author__ = 'Jervis Muindi'


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

