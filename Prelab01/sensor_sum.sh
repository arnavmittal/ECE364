#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-18 19:22:52 -0500 (Mon, 18 Jan 2016) $
# $Revision: 85753 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Prelab01/sensor_sum.sh $

if [[ ! $# == 1 ]]
then
    echo "Usage: ./sensor_sum.sh <filename>"
    exit 0
fi

if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file"
fi

while read sensornumber a b c
do
    sensornum=$(echo $sensornumber | cut -c 1-2 )
    echo "$sensornum $(( $a+$b+$c ))"
done < $1

exit 0
