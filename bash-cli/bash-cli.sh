#!/bin/bash

echo "Welcome to my Bash CLI"
echo "================="
echo "Datasets"
echo "=================="
echo "Enter h to see the head of the datasets: "
echo "Enter t to see the tail of the datasets: "
echo "Enter q to exit"
echo -e "\n"
echo -e "Your Choices \c"
read Choices
case "$Choices" in 
    h) head ;;
    t) tail ;;
    q) exit ;;
esac


