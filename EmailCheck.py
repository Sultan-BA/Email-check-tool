#!/usr/bin/env python3
from typing import List  # for beautifying the code
import re


def isEmail(email: str) -> bool:
    reg = re.compile(r'[a-zA-Z0-9][a-zA-Z0-9_.-]*@[a-zA-Z0-9]+[.][a-zA-Z]{2,}')

    text = reg.search(email)

    return 1


# call the function and enter the email as the parameter
# ( dont forget to use the print function to see the result )

isEmail("sultanxx575@gmail.com")  # <-----------
'''
The function depends on these terms :

** The parenthesis is only for clearing the symbols and it's not included.

the email does not start with a symbol

the first part must contain at least one character (before the (@) symbol)

it must contain the (@) symbol

at least one character must be followed by the (@) symbol

the (@) symbol must then be followed by the (.) symbol

at least two characters must be followed by the (.) symbol

the first part (before the (@) symbol) can contain the following symbols : (.) (_) (-)
'''