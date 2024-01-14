# Queens College
# Dicrete Structures CSCI 220
# Winter 2024
# Assignment 2 Boolean Algebra
# Mikdad Abdullah
# Collaborated With Class

import inspect
import pandas as pd
from itertools import product
import texttable


def print_table(title, headers, data, alignments):
   tt = texttable.Texttable(0)
   tt.set_cols_align(alignments)
   tt.add_rows([headers] + data, True)
   print(title)
   print(tt.draw())
   print()


# [1] Define and implement the seven operators b_not, b_and, b_or, b_xor, b_nand, b_nor, b_xnor as 0/1 boolean functions
# (not T/F). Consider all to be binary (degree 2) functions except b_not which is unary (degree 1):

def b_not(x):
    return 1 - x


def b_and(x, y):
    return x * y


def b_or(x, y):
    return min(x + y, 1)


def b_xor(x, y):
    return abs(x - y)


def b_nand(x, y):
    return 1 - b_and(x, y)


def b_nor(x, y):
    return 1 - b_or(x, y)


def b_xnor(x, y):
    return 1 - b_xor(x, y)


# [2] Rewrite the truth_table function from Assignment 1 for 0/1 boolean algebra and call it boolean_table.
def boolean_table(f):
    values = [list(x) + [f(*x)] for x in product([0, 1], repeat=f.__code__.co_argcount)]
    return pd.DataFrame(values, columns=(list(f.__code__.co_varnames) + [f.__name__]))


# [3] Rewrite the analyze_truth_table function from Assignment 1 for 0/1 boolean algebra and call it
# analyze_boolean_table. As your starting point, use the enhanced version from class on September 6. Omit the part
# about tt_type (tautology, contingency, contradiction). You may want to reverse the binary string (using binary[::-1])
# before converting it to a decimal number, as that may better align the result with the function number.

def analyze_boolean_table(f, verbose=False):
    tt = boolean_table(f)
    tt_heads = tt.columns.tolist()
    tt_rows = tt.shape[0]
    tt_cols = tt.shape[1]
    tt_vars = tt_cols - 1
    last_col = tt.iloc[:, tt_vars]
    binary = "".join(["1" if last_col[i] else "0" for i in range(len(last_col))])[::-1]
    if verbose:
        print("Name:", f.__name__, func_body(f))
        print(tt)
        print("Rows:", tt_rows, "Cols:", tt_cols, "Vars:", tt_vars)
    return tt, tt_heads, tt_rows, tt_cols, tt_vars, last_col, binary, int(binary, 2)

# [4] Define a function func_body(f) that returns the content of the function.
# This will be used later in the truth table.
def func_body(f):
    body = inspect.getsource(f)  # gets the code
    idx = body.index("return")  # get the part after return
    return body[7 + idx:].strip()

# [4] Rewrite functions f0 thru f15 from Assignment 1 as 0/1 boolean functions. It is not necessary to include the other
# functions from that assignment (De Morgan's Laws, Modus Ponens, Modus Tollens, and Hypothetical Syllogism).
def f0_false(p, q):
    return 0


def f1_nor(p, q):
    return b_nor(p, q)


def f2_converse_nonimpl(p, q):
    return b_and(b_not(p), q)


def f3_neg_p(p, q):
    return b_not(p)


def f4_nimpl(p, q):
    return b_and(p, b_not(q))


def f5_neg_q(p, q):
    return b_not(q)


def f6_xor(p, q):
    return b_xor(p, q)


def f7_nand(p, q):
    return b_nand(p, q)


def f8_and(p, q):
    return b_and(p, q)


def f9_xnor(p, q):
    return b_xnor(p, q)


def f10_q(p, q):
    return q


def f11_impl(p, q):
    return b_or(b_not(p), q)


def f12_p(p, q):
    return p


def f13_converse(p, q):
    return f11_impl(q, p)


def f14_or(p, q):
    return b_or(p, q)


def f15_True(p, q):
    return 1

# [5] Run analyze_boolean_table looping over those 16 functions. Use a dictionary to keep track of which functions
# resulted in which binary number. Verify that all 16 numbers were each produced once and only once.
def analyze_functions():
    functions = [f0_false, f1_nor, f2_converse_nonimpl, f3_neg_p, f4_nimpl, f5_neg_q, f6_xor,
                 f7_nand, f8_and, f9_xnor, f10_q, f11_impl, f12_p, f13_converse, f14_or, f15_True]
    data = []
    for func in functions:
        results = analyze_boolean_table(func)
        row = [func.__name__, func_body(func), str(results[6]), results[7], reverse_engineer(func)]
        data.append(row)
    headers = ["name", "function", "binary", "decimal", "reversed"]
    print_table("All Binary Functions", headers, data, ["l", "l", "r", "r", "l"])


# [6] Define a function that, using the method discussed in class, reverse-engineers a 0/1 boolean table into a function
# that yields that table's output column.

def reverse_engineer(f):
    tt, tt_heads, tt_rows, tt_cols, tt_vars, tt_out, tt_bin, tt_dec = analyze_boolean_table(f, False)
    function = " + ".join(
        ["".join([tt_heads[j] + ("'" if tt.iloc[i][j] == 0 else "") for j in range(tt_vars)]) for i in range(tt_rows) if
         tt_out[i] == 1])
    return function

# [7] Write a function half_adder(x, y) that uses the functions created in Task [1] as "gates" and produces the s (sum)
# and c (carry) outputs per the table in the slides.

def half_adder():
    #s = b_and(b_or(x, y), b_not(b_and(x, y)))
    # c = b_and(x, y)
    data = [[x, y, b_and(b_or(x, y), b_not(b_and(x, y))), b_and(x, y)] for x in [1, 0] for y in [1, 0]]
    headers = ["x", "y", "s", "c"]
    title = "half-adder"
    alignments = ["r", "r", "r", "r"]
    print_table(title, headers, data, alignments)


def main():
    analyze_functions()
    half_adder()


if __name__ == '__main__':
    main()
