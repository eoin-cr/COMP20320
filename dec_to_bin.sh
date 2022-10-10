#!/bin/bash

function convip()
{
    CONV=({0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1})

    ip=""
    for byte in `echo ${1} | tr "." " "`; do
        ip="${ip}.${CONV[${byte}]}"
    done
    echo ${ip:1}
}

echo "Enter the first ip"
read ip1
echo "Enter the second ip"
read ip2

a=`convip "${ip1}"`
b=`convip "${ip2}"`

echo "${a}"
echo "${b}"
