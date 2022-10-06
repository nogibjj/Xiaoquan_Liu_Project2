#!/bin/bash
trap " " 2
while true
do
echo "Welcome to a Really Simple Bash CLI"
echo "================="
echo "Try Another Way to Exit"
echo "=================="
echo "Enter q to exit"
echo -e "\n"
echo -e "Your Choices \c"
read Choices
case "$Choices" in 
h) head ;;
t) tail ;;
q) exit ;;
esac
echo -e "Enter return to continue \c"
read input
done



