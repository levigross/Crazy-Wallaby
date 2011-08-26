#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#Warning!!! this program will destroy your server.
__version__ = 0.1

from harddrive import fill_io_buffer

if __name__ == '__main__':
    num_files = raw_input("How many files would you like to create? ")
    fill_io_buffer(int(num_files))
