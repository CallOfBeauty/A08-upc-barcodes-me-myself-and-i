from a08_upc_start import *
import sys

from inspect import getframeinfo, stack

def unittest(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def a08_test_suite():
    unittest(is_valid_input("036000291452") == True)
    unittest(is_valid_input("1") == False)
    # TODO Add tests for your functions here!


if __name__ == "__main__":
    a08_test_suite()
