#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-25 23:06:12 -0500 (Mon, 25 Jan 2016) $
# $Revision: 86863 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Prelab02/process_temps.bash $


if [[ ! $# == 1 ]]
then
    echo 'Usage: process_temps.bash <input file>'
    exit 1
fi

if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file."
    exit 2
fi
loop=0
while read time temps
do
    sum=0
    avg=0
    if ((loop==0))
    then
        loop=1
        continue
    fi
    temp_array=($temps)
    for i in ${!temp_array[*]}
    do
        ((sum=$sum + ${temp_array[$i]}))
    done
    (( avg=$sum/${#temp_array[*]} ))
    echo Average temperature for time $time was $avg C.
done < $1

exit 0
