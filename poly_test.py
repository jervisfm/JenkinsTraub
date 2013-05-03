__author__ = 'Jervis Muindi'

import unittest
from poly import *

class MyTestCase(unittest.TestCase):

    sample_poly = [2, -11, 17, -6]
    sample_poly_pow = 3

    sample_poly_2 = [6, -13, 7]
    sample_poly_pow_2 = 2




    def test_poly_init(self):

        poly_size = len(self.sample_poly)
        p = Poly(self.sample_poly_pow, self.sample_poly)

        for i in xrange(poly_size):
            self.assertEqual(self.sample_poly[i], p.coeff[i])


    def test_poly_add(self):
        p1 = Poly(self.sample_poly_pow, self.sample_poly)
        p2 = Poly(self.sample_poly_pow_2, self.sample_poly_2)

        expected_ans = [2, -5, 4, 1]
        ans  = p1 + p2

        self.assertTrue(ans.size() == len(expected_ans))
        for i in xrange(ans.size()):
            self.assertEqual(ans.coeff[i], expected_ans[i])

    def test_poly_eq(self):
        p1 = Poly(self.sample_poly_pow, self.sample_poly)
        p2 = Poly(self.sample_poly_pow, self.sample_poly)
        p3 = Poly(self.sample_poly_pow_2, self.sample_poly_2)
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_poly_eval(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)

        actual = p.eval(0)
        expected = -6
        self.assertEqual(actual, expected)

        #Test a some random number
        actual = p.eval(17)
        expected = 6930
        self.assertEqual(actual, expected)


    def test_poly_get_power_at_index(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)

        max_deg = p.highest_degree()
        cur_deg = max_deg
        index = 0
        for c in p.coeff:
            actual = p.get_power_at_index(index)
            expected = cur_deg
            self.assertEqual(actual, expected)
            index += 1
            cur_deg -= 1

    def test_poly_get_derivative(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)

        expected_ans = [6, -22, 17]
        expected = Poly(p.highest_degree() - 1, expected_ans)
        actual = p.get_derivative()

        self.assertTrue(expected == actual)


    def test_poly_const_mult(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        multipler = 7
        expected_coeff = map(lambda x: multipler*x, self.sample_poly)
        expected = Poly(p.highest_degree(), expected_coeff)
        actual = p.const_mult(multipler)

        self.assertTrue(expected == actual)

    def test_poly_negate(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)

        expected_coeff = map(lambda x: -x, self.sample_poly)
        expected = Poly(p.highest_degree(), expected_coeff)
        actual = p.negate()
        self.assertTrue(expected == actual)

    def test_poly_subtraction(self):
        p1 = Poly(self.sample_poly_pow, self.sample_poly)
        p2 = Poly(self.sample_poly_pow_2, self.sample_poly_2)

        expected_ans = [2, -17, 30, -13]
        ans  = p1 - p2

        self.assertTrue(ans.size() == len(expected_ans))
        for i in xrange(ans.size()):
            self.assertEqual(ans.coeff[i], expected_ans[i])


    def test_get_empty_poly(self):
        expected_coeff = [0, 0, 0, 0]
        expected_pow = 3
        expected = Poly(expected_pow, expected_coeff)
        actual = get_empty_poly(3)
        self.assertTrue(actual == expected)

    def test_poly_set_coeff_at_x_power(self):
        expected_coeff = [6, -3, 0, 7]
        expected_pow = 3
        expected = Poly(expected_pow, expected_coeff)

        p = get_empty_poly(3)
        p.set_coeff_at_x_power(0,7)
        p.set_coeff_at_x_power(1,0)
        p.set_coeff_at_x_power(2,-3)
        p.set_coeff_at_x_power(3,6)
        actual = p
        self.assertTrue(actual == expected)

    def test_term_multiply_linear_poly(self):

        t = Term(2,2)
        actual = t.multiply_linear_poly(1,-3)

        expected_coeff = [2,-6,0,0]
        expected_pow = len(expected_coeff) - 1

        expected = Poly(expected_pow, expected_coeff)

        self.assertTrue(actual == expected)

    def test_poly_get_highest_degree_of_non_zero_coeff(self):
        p = get_empty_poly(3)
        p.set_coeff_at_x_power(2,6)
        expected = 2
        actual = p.get_highest_degree_of_non_zero_coeff()
        self.assertEqual(expected, actual)

    def test_poly_divide_linear_poly(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        actual = p.divide_linear_poly(1, -3)

        expected_coeff = [2, -5, 2]
        expected_pow = len(expected_coeff) - 1
        expected = Poly(expected_pow, expected_coeff)

        self.assertTrue(expected == actual)

        # Test non-perfect division example
        actual = p.divide_linear_poly(1,-4)
        expected_coeff = [2, -3, 5]
        expected_pow = len(expected_coeff) - 1
        expected = Poly(expected_pow, expected_coeff)
        self.assertTrue(expected == actual)

    def test_get_cauchy_poly(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        actual = p.get_cauchy_poly()

        #expected_coeff = [1, 11, 17, -6]
        expected_coeff = [1, 5.5, 8.5, -3]

        expected_pow = len(expected_coeff) - 1
        expected = Poly(expected_pow, expected_coeff)

        self.assertTrue(expected == actual)

    def test_solve_poly_newton(self):
        p = Poly(self.sample_poly_pow, self.sample_poly)
        err = 10 ** -6
        cauchy_poly = p.get_cauchy_poly()
        actual = solve_poly_newton(cauchy_poly, err)
        expected = 0.294016

        self.assertAlmostEquals(actual, expected, delta=err)



    def test_get_initial_s(self):

        p = Poly(self.sample_poly_pow, self.sample_poly)
        actual = get_initial_s(p)
        actual_abs = abs(actual)
        expected = 0.294016
        err = 10 ** (-4)

        self.assertAlmostEquals(actual_abs, expected, delta=err)


if __name__ == '__main__':
    unittest.main()
