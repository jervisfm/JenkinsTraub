
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
            coeff - is a listing of coefficients.
            The first element of this list represents the coefficient of highest x-term in the polynimal
            The last element of this list should represent the constant term.
            Note that all the coefficients should be in the list - if they do have a value, they should be set to 0.
        """
        if (pow != len(coeff) - 1):
            raise ValueError('There is mismatch between power of polynomial and coeffiecnts: %s vs %s' % (pow, coeff))

        self.coeff = []
        for x in coeff:
            self.coeff.append(x)

    def highest_degree(self):
        return len(self.coeff) - 1

    def size(self):
        return len(self.coeff)

    def __str__(self):
        str = '| '
        pow = self.highest_degree()
        for x in self.coeff:
            str += '(%s,%s), ' % (x, pow)
            pow -= 1
        str = ' | '
        return str

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



    def get_x_power_coeff(self, pow):
        max_pow = self.highest_degree()
        if (pow > max_pow):
            raise ValueError('Invalid Power Arguemnt: %s' % str(pow))
        elif (pow == 0):
            last_idx = self.size() - 1
            return self.coeff(last_idx)
        else: # It's a negative power
            raise ValueError('This polynomial does not support negative x-powers')