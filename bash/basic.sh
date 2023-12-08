#!/bin/bash
# names=("sandip" "kumar" "gupta" "mohan" "ji" "bihari")
# echo "${names[@]}"
# for name in "${names[@]}"
# do
#     echo "$name"
# done

fruits=(Apple Banana Orange Grapes Mango)

# Loop through the array
for fruit in "${fruits[@]}"
do
  echo "Processing $fruit"
  # Add your processing logic here
done
read number
if [[ $number -gt 2 ]]; then
    echo "helllo"
fi
