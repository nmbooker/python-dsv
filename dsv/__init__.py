#! /usr/bin/env python

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

