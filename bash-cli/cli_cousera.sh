#!/usr/bin/env bash
#output looks like this
#
# Run Script:
#         ./cli_cousera.sh --count 5 --phrase "hello world"
#hello world
#hello world
#hello world
#hello world
#hello world

## A. Does the Work
#Generate phrase 'N' times
phrase_generator(){
    for ((i=0; i<$1; i++)); do
        echo "You entered phrase: $2"
    done
}

## B. Parse input from the CLI
#Parse Options
while [[ $# -gt 1 ]]
do
key="$1"

case $key in
    -c|--number)
    COUNT="$2"
    shift
    ;;
    -p|--message)
    PHRASE="$2"
    shift
    ;;
esac
shift
done

##C.  Pass parsed input to function and run everything
#Run program
phrase_generator "${COUNT}" "${PHRASE}"
