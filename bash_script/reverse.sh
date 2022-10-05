#!/usr/bin/env bash

i=1;    #initialize count
j=$#;   #get script input size

while [[ $# -gt 1 ]] #compare 输入参数数量与1的大小
do
    rstring=$(echo $1 | rev);
    echo "Reversing string $i:$1: $rstring";
    i=$((i + 1));   #increment the count
    shift 1;        #process the next argument
done