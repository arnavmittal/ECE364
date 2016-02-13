#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-25 20:43:17 -0500 (Mon, 25 Jan 2016) $
# $Revision: 86814 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Prelab02/yards.bash $

if [[ ! $# == 1 ]]
then
    echo 'Usage: yards.bash <filename>'
    exit 1
fi

if [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 1
fi

max_avg=0
while read name yards
do
    sum=0
    avg=0
    var=0
    yards_arr=($yards)
    for i in ${!yards_arr[*]}
    do
        ((sum=$sum + ${yards_arr[$i]}))
    done
    ((avg=$sum/${#yards_arr[*]}))
    
    for i in ${!yards_arr[*]}
    do
        ((var=$var + (${yards_arr[$i]} - $avg)*(${yards_arr[$i]} - $avg)))
    done
    ((var=$var / ${#yards_arr[*]}))
    if [[ $avg > $max_avg ]]
    then
        max_avg=$avg
    fi
    echo "$name schools average $avg yards receiving with a variance of $var"
done < $1
echo "The largest average yardage was $max_avg"
exit 0
