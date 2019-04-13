#!/bin/bash

OUTDIR=/home/chanceygardener/repos/probed/bin
SDIR=/home/chanceygardener/repos/probed/src
CC= g++
inf=$1 # take first positional command line arg
name=${inf::-3}; # assumes .cc suffix

# compile dat shit

$CC $SDIR'/'$inf  -o $OUTDIR'/'$name; 

