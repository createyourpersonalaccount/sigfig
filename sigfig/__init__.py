from decimal import localcontext, Decimal, ROUND_HALF_UP
from re import search

def sigfig(x, n, rounding=ROUND_HALF_UP):
    neg = False
    if n == 0:
        return "0"
    with localcontext() as ctx:
        ctx.prec = n
        ctx.rounding=rounding
        y = Decimal(str(x)).normalize()
        if y == 0 or not y.is_finite():
            return "0"
        elif y < 0:
            neg = True
            y = -y
        s = f'{y:f}'
    parts = s.split(".", 1)
    diff = n - len(parts[0])
    if len(parts) == 1:
        if diff > 0:
            s += "." + "0" * diff
    else:
        if parts[0] == "0":
            diff += 1
        j = search(r'[^0]', parts[1])
        if j is None:
            raise Exception("Error (bug), conversion of argument to string has no fractional part.")
        j = j.start()
        diff -= (len(parts[1]) - j)
        if diff > 0:
            s += "0" * diff
    if neg:
        s = "-" + s
    return s
