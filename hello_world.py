#!/usr/bin/env python

import os

def main():
    dirname = os.environ.get('CIRCLE_ARTIFACTS')
    f = open(dirname + '/output.txt', "w")
    f.write("hello world\n")
    f.close()

if __name__ == '__main__':
  main()
