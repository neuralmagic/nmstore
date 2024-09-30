#!/usr/bin/env bash

# echo "green encased checkmark" if "${1} == 0"
# echo "red X"                   if "${1} != 0"

if [ "$1" -eq 0 ]; then
    # green check
    echo -e "\xE2\x9C\x85"
else
    # red x
    echo -e "\xE2\x9D\x8C"
fi
