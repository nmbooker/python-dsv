#! /usr/bin/env python

"""Contains the DSV dialect for Python's CSV module

Should also be compatible with the oekit.unicsv module too.


There are two scripts provided too (for more info run with --help or read README.mkd):

 dsv2csv     --  takes DSV colon-separated data on stdin and outputs
                 CSV on stdout in the csv module's default dialect 'excel'

 dsvjoinline --  takes a series of positional arguments, and outputs those
                 arguments joined together into a single DSV record on stdout.
                 stdin is not read.
"""

import csv

class DSVDialect:
    """Dialect for Python's csv module.

    The format is as follows:
    field:field:field:field
    field:field:field:field

    Literal colons are escaped by backslash.
    Newlines in the data are also escaped by backslash.

    /etc/passwd is an example of a file that can be parsed with this dialect.
    """
    delimiter = ':'
    escapechar = '\\'
    quoting = csv.QUOTE_NONE
    lineterminator = '\n'
    skipinitialspace = False
    quotechar = ''

