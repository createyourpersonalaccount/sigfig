from math import inf, nan
from sigfig import sigfig

def test_sigfig_nan():
    assert sigfig(nan, 3) == "0"
    assert sigfig(nan, 0) == "0"

def test_sigfig_infinity():
    assert sigfig(inf, 3) == "0"
    assert sigfig(inf, 0) == "0"

def test_sigfig_zero_argument():
    assert sigfig(123, 0) == "0"
    assert sigfig(0, 123) == "0"
    assert sigfig(0, 0) == "0"

def test_sigfig_only_floating():
    assert sigfig(0.1234, 3) == "0.123"
    assert sigfig(0.1235, 3) == "0.124"
    assert sigfig(0.1234, 4) == "0.1234"
    assert sigfig(0.1235, 4) == "0.1235"
    assert sigfig(0.1234, 5) == "0.12340"
    assert sigfig(0.1235, 5) == "0.12350"
    assert sigfig(0.1234, 6) == "0.123400"
    assert sigfig(0.1235, 6) == "0.123500"
    assert sigfig(0.001234, 3) == "0.00123"
    assert sigfig(0.001235, 3) == "0.00124"
    assert sigfig(0.001234, 4) == "0.001234"
    assert sigfig(0.001235, 4) == "0.001235"
    assert sigfig(0.001234, 5) == "0.0012340"
    assert sigfig(0.001235, 5) == "0.0012350"
    assert sigfig(0.001234, 6) == "0.00123400"
    assert sigfig(0.001235, 6) == "0.00123500"

def test_sigfig_short_integer():
    assert sigfig(12, 3) == "12.0"
    assert sigfig(1, 3) == "1.00"

def test_sigfig_with_decimal():
    assert sigfig(123.4, 3) == "123"
    assert sigfig(123.5, 3) == "124"
    assert sigfig(12.34, 3) == "12.3"
    assert sigfig(12.35, 3) == "12.4"

def test_sigfig_zero():
    assert sigfig(0, 3) == "0"
    assert sigfig(1234, 0) == "0"

def test_sigfig_long_integer():
    assert sigfig(1000, 1) == "1000"
    assert sigfig(1000, 1) == "1000"
    assert sigfig(1200, 2) == "1200"
    assert sigfig(1200, 2) == "1200"
    assert sigfig(1234, 3) == "1230"
    assert sigfig(1236, 3) == "1240"
    assert sigfig(1234.4, 3) == "1230"
    assert sigfig(1236.6, 3) == "1240"
    assert sigfig(1234, 4) == "1234"
    assert sigfig(1236, 4) == "1236"

def test_sigfig_zero_argument_negative():
    assert sigfig(-123, 0) == "0"
    assert sigfig(-0, 123) == "0"
    assert sigfig(-0, 0) == "0"

def test_sigfig_only_floating_negative():
    assert sigfig(-0.1234, 3) == "-0.123"
    assert sigfig(-0.1235, 3) == "-0.124"
    assert sigfig(-0.1234, 4) == "-0.1234"
    assert sigfig(-0.1235, 4) == "-0.1235"
    assert sigfig(-0.1234, 5) == "-0.12340"
    assert sigfig(-0.1235, 5) == "-0.12350"
    assert sigfig(-0.1234, 6) == "-0.123400"
    assert sigfig(-0.1235, 6) == "-0.123500"
    assert sigfig(-0.001234, 3) == "-0.00123"
    assert sigfig(-0.001235, 3) == "-0.00124"
    assert sigfig(-0.001234, 4) == "-0.001234"
    assert sigfig(-0.001235, 4) == "-0.001235"
    assert sigfig(-0.001234, 5) == "-0.0012340"
    assert sigfig(-0.001235, 5) == "-0.0012350"
    assert sigfig(-0.001234, 6) == "-0.00123400"
    assert sigfig(-0.001235, 6) == "-0.00123500"

def test_sigfig_short_integer_negative():
    assert sigfig(-12, 3) == "-12.0"
    assert sigfig(-1, 3) == "-1.00"

def test_sigfig_with_decimal_negative():
    assert sigfig(-123.4, 3) == "-123"
    assert sigfig(-123.5, 3) == "-124"
    assert sigfig(-12.34, 3) == "-12.3"
    assert sigfig(-12.35, 3) == "-12.4"

def test_sigfig_zero_negative():
    assert sigfig(-0, 3) == "0"
    assert sigfig(-1234, 0) == "0"

def test_sigfig_long_integer_negative():
    assert sigfig(-1000, 1) == "-1000"
    assert sigfig(-1000, 1) == "-1000"
    assert sigfig(-1200, 2) == "-1200"
    assert sigfig(-1200, 2) == "-1200"
    assert sigfig(-1234, 3) == "-1230"
    assert sigfig(-1236, 3) == "-1240"
    assert sigfig(-1234.4, 3) == "-1230"
    assert sigfig(-1236.6, 3) == "-1240"
    assert sigfig(-1234, 4) == "-1234"
    assert sigfig(-1236, 4) == "-1236"
