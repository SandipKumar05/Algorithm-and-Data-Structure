#!/bin/bash

echo $@
echo $#
echo $1
echo $2

if [ $# -eq 0 ]; then
    echo "no input"
fi

file_name=$1
if [ -e $file_name ]; then
    size=$(du -k "$file_name" | cut -f1)
    echo $size
fi