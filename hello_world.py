#!/usr/bin/env python
import os

f = open(os.environ.get('CIRCLE_ARTIFACTS')"/output.txt", "w")

f.write("hello world\n")

f.close()
