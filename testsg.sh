#!/bin/bash -e

make;

time ./probed data/raw/paradise_lost.txt data/raw/dantes_inferno.txt;

du -h "test_sg_classics.csv";

