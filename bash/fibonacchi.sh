read n

fibonacci(){
    local n=$1
    local a=0
    local b=1
    for ((i=2;i<=n;i++)); do
        tmp=$((a + b))
        echo $tmp
        a=$b
        b=$tmp
    done
}

fibonacci $n