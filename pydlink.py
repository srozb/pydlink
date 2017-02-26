#!/usr/bin/env python

import sys
from camera import Camera
from imgrender import AnsiRender, SaveJpeg

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
    name, location = c.getName()
    c.getSdcard()
    c.getWirelessConfig()
    c.getICR()
    c.getLED()
    c.getSpeaker()
    c.getAudioDetection()
    c.getMotionDetection()
    c.getSensorInfo()
    jpeg = c.getScreenshot()
    filename = SaveJpeg(jpeg)
    AnsiRender(filename)



if __name__ == "__main__":
    banner()
    if len(sys.argv) < 3:
        usage()
    main()
