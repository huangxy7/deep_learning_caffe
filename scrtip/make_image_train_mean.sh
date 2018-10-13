#! /usr/bin/env sh

#Compute the mean image from the net traing lmdb

EXAMPLE=/home/jsj/xylook/lmdb
DATA=~/xylook/data
TOOLS=~/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/xylook_train_lmdb $DATA/image_train_mean.binaryproto

echo "Done."

