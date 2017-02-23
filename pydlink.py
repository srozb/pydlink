#!/usr/bin/env python

import sys
from camera import Camera
from imgrender import AnsiRender

def banner():
    print("pydlink (c) 2017: @srozb")

def usage():
    print("usage:")
    print("    {} [host] [camera password]".format(sys.argv[0]))
    sys.exit(-1)

def main():
    c = Camera(sys.argv[1], sys.argv[2])
    if not c.checkAuth():
        sys.exit(-2)
    name, location = c.checkName()
    c.checkSdcard()
    jpeg = c.getScreenshot()
    with open('/tmp/temp.jpg', 'wb') as f:
        f.write(jpeg)
        f.flush()
    AnsiRender('/tmp/temp.jpg')


if __name__ == "__main__":
    banner()
    if len(sys.argv) < 3:
        usage()
    main()
