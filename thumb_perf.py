import openslide
import os,sys
from subprocess import call
import argparse

def thumbit():
    size = (128,64)
    s = openslide.OpenSlide(args.file)
    downsample = max(*[dim / thumb for dim, thumb in
                zip(s.dimensions, size)])
    level = s.get_best_level_for_downsample(downsample)
    tile = s.read_region((0, 0), level, s.level_dimensions[level])

def parseargs():
    parser = argparse.ArgumentParser(description="Build svs image metadata table")
    parser.add_argument ( "-v", "--verbosity", action="count",default=0,help="increase output verbosity" )
    parser.add_argument ( "-f", "--file", type=str, help="file", default='imaging-west/5702effc-f5c6-47f8-bed5-74651f71ecce/TCGA-BQ-5875-01A-01-TS1.03879c22-0c80-4b4f-9429-03477242c682.svs')
    
    return(parser.parse_args())

if __name__ == '__main__':
    args=parseargs()
    thumbit()
