# A significant figures Python3 module

This module provides the `sigfig()` function which computes a number to the given [significant figures](https://en.wikipedia.org/wiki/Significant_figures). For example:

```
from sigfig import sigfig

assert sigfig(0.001235, 6) == "0.00123500"
assert sigfig(12, 3) == "12.0"
assert sigfig(123.4, 3) == "123"
assert sigfig(123.5, 3) == "124"
assert sigfig(1234.4, 3) == "1230"
```

The function works for negative numbers as well. The rounding mode can be set too in the `rounding=` argument, and it defaults to `ROUND_HALF_UP`. See the [rounding modes of Decimal](https://docs.python.org/3/library/decimal.html#rounding-modes) for other modes.
