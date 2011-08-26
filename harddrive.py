#! /usr/bin/env python
# -*- coding: UTF-8 -*-
__version__ = 0.1

from gevent.monkey import patch_all; patch_all()
import gevent
import string,random,os

def fill_io_buffer(num_files):
    while True:
        files = []
        for i in xrange(num_files):
            files.append(open(''.join((random.choice(string.ascii_letters) for i in xrange(10))),'w'))
        events = []
        for i in files:
            events.append(gevent.spawn(_fill_file,i))
            events.append(gevent.spawn(_read_file,i))
        for i in events:
            i.join()
        for i in files:
            os.remove(i.name)
            

def _fill_file(fd):
    while True:
        fd.write(u'0'*5000)


def _read_file(fd):
    while True:
        fd.read(10000)
        fd.seek(random.randint(1,1000*1000))
        fd.rewind()

        