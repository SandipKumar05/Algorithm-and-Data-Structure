#!/bin/bash
# names=("sandip" "kumar" "gupta" "mohan" "ji" "bihari")
# echo "${names[@]}"
# for name in "${names[@]}"
# do
#     echo "$name"
# done

fruits=(Apple Banana Orange Grapes Mango)

for fruit in "${fruits[@]}"
do
  echo "Processing $fruit"
done

read number
if [[ $number -gt 2 ]]; then
    echo "helllo"
fi
