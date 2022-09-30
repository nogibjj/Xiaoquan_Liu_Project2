#!/bin/bash
#output looks like this:
#
##./food_choice.sh --choose "Apple"   
# Eat Yogurt with your Apple



#Generate phrase "N" times
food_choice(){
	rand=$(shuf -i 2600-2700 -n 1)
	echo -en "   \u$rand"
    sleep 1

    if [ "$1" = "Apple" ]; then
    echo "Eat Yogurt with your Apple"
elif [ "$1" = "Milk" ]; then
    echo "Eat Cereal with your Milk"
elif [ "$1" = "Advocado" ]; then
    echo "Try smash Advocado with boiled Eggs, add some pepper and salt!"
else
    echo "Eat your {$1} by itself!"
fi
}

#Parse Options
while [[ $# -gt 1 ]]
do
key="$1"

case $key in
    -c|--choose)
    FOOD="$2"
    shift
    ;;
esac
shift
done

#Run program
food_choice "${FOOD}"