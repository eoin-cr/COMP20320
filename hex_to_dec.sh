#!/bin/bash
echo "Type a hex number"
read hexNum
# echo -n "The decimal value of $hexNum is "
echo "obase=10; ibase=16; $hexNum" | bc
