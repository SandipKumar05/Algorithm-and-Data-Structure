#!/bin/bash
# names=("sandip" "kumar" "gupta" "mohan" "ji" "bihari")
# echo "${names[@]}"
# for name in "${names[@]}"
# do
#     echo "$name"
# done

# fruits=(Apple Banana Orange Grapes Mango)

# for fruit in "${fruits[@]}"
# do
#   echo "Processing $fruit"
# done

# read number
# if [[ $number -gt 2 ]]; then
#     echo "helllo"
# fi

read n

print(){
  echo $1
}

dekho(){
  for i in {1..5}; do
    echo $i
  done
}

# for ((i=0;i<n;i++)); do
#   print $i
# done
dekho
