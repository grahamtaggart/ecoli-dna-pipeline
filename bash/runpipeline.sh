#!/bin/bash

# First argument is the output directory
outdir=$1
mkdir -p $outdir

# Second argument is dataset ID
dataset_id=$2

# Need to update this so that email is entered by user, not python script.

# Pass the output directory and dataset ID to each stage of the pipeline
# 1
python download_data.py $outdir $dataset_id
python 