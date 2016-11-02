"""
             _
  ___  __ _ | |  ___
 / __|/ _` || | / __|
| (__| (_| || || (__
 \___|\__,_||_| \___|


Rabbit hole:
    The relative imports here (noted by the . prefix) are done as a convenience
    so that the consumers of the ``calc`` package can directly use objects
    belonging to the ``calc.calc`` module. Essentially this enables the consumer
    to do

    >>> from calc import INTEGER

    instead of having to use the slightly longer

    >>> from calc.calc import INTEGER
"""
__author__ = 'Reilly Tucker Siemens, Alex LordThorsen'
__email__ = 'reilly@tuckersiemens.com, alexlordthorsen@gmail.com'
__version__ = '0.1.0'

from calc.calc import Calc, CalcError
from calc.token import INTEGER, EOF, PLUS
from calc.token import Token
