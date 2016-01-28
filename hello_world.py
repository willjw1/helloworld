#!/usr/bin/env python
import os

dirname = os.environ.get('CIRCLE_ARTIFACTS')
f = open(dirname + '/output.txt', "w")

f.write("hello world\n")

f.close()
