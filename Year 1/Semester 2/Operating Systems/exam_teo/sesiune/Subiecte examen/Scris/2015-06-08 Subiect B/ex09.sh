#!/bin/bash

SUM=0

shift
shift

while [ $# -ge 1 ]; do
    #echo $1
    SUM=$(($SUM+$1))
    shift
    shift
    shift
done

echo $SUM

