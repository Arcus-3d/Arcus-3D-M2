#!/usr/bin/env python
"""
Brandon Heller
6/15/2014

Script to generate g-code scripts to help with calibrating a linear delta
3D printer.  Creates files to move the extruder to three points around a
triangle as well one for the center.

Each generated script looks like this:

o<g70> sub
G0 Z0
G0 Y80
G0 Z-5
o<g70> endsub
M2

G70-72 move to three circle positions.
G79 moves to the center.

To use this script, run:

 python create_delta_calibration_gcodes.py

For a description of the options, call with -h.
"""
from math import sin, cos, pi
import os
from argparse import ArgumentParser
    
DEF_RADIUS = 227
DEF_Z_DEPTH = 20
DEF_DIR = "../subroutines"
DEF_G_CODE_BASE = 70

# Offset for center probe point, e.g., 9 for G79 if g_code_base is 70.
CENTER_G_CODE_OFFSET = 9


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-r", "--radius", help="Radius for 3 main points",
                        default=DEF_RADIUS)
    parser.add_argument("-z", "--z_depth", help="Z depth for 3 main points",
                        default=DEF_Z_DEPTH)
    parser.add_argument("-d", "--dir", help="Directory in which to write files",
                        default=DEF_DIR)
    parser.add_argument("-g", "--g_code_base",
                        help="G-code numbering base(e.g., 70 for G70)",
                        default=DEF_G_CODE_BASE)
    args = parser.parse_args()
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)
    
    return args


def g0(x = None, y = None, z = None):
    x_s = " X%s" % x if x is not None else ""
    y_s = " Y%s" % y if y is not None else ""
    z_s = " Z%s" % z if z is not None else ""
    return "G0%s%s%s\n" % (x_s, y_s, z_s) 


def write_ngc(g_code_index, contents, g_code_base, output_dir):
    g_code = g_code_base + g_code_index
    filename = "g%s.ngc" % g_code
    s = "o<g%i> sub\n" % g_code
    s += "%s" % contents
    s += "o<g%i> endsub\n" % g_code
    s += "M2\n"
    path = os.path.join(output_dir, filename)
    print "Writing file: %s" % path
    f = open(path, 'w')
    f.write(s)


def main(opts):
    z1 = 0
    z2 = z1 - opts.z_depth

    # Add each point around the circle
    for i, theta in enumerate(range(0, -360, -120)):
        #print "theta = %s" % theta
        s = g0(z = z1)
        theta_r = (2 * pi / 360.0) * theta
        x = sin(theta_r) * opts.radius
        y = cos(theta_r) * opts.radius
        s += g0(x = x, y = y)
        s += g0(z = z2)  
        write_ngc(i, s, opts.g_code_base, opts.dir)
    
    # Add center
    s = g0(z = z1)
    s += g0(x = 0.0, y = 0.0)
    s += g0(z = z2)
    write_ngc(CENTER_G_CODE_OFFSET, s, opts.g_code_base, opts.dir)


if __name__=="__main__":
    opts = parse_args()
    main(opts)
