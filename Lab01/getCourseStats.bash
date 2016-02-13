#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-19 17:19:56 -0500 (Tue, 19 Jan 2016) $
# $Revision: 86276 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Lab01/getCourseStats.bash $

if [[ ! $# == 1 ]]
then
    echo "Usage: ./getCourseStats.bash <course name>"
    exit 1
fi

if [[ ! $1 == "ece364" && ! $1 == "ece337" && ! $1 == "ece468" ]]
then
    echo "Error: course $1 is not a valid option."
    exit 5
fi

totalstud=0
avgscore=0
currsc=0
currscname=0
maxsc=0
maxscname=0
for args in $(ls gradebooks/$1*.txt)
do
    ./getFinalScores.bash $args
    if [[ ! $? == "0" ]]
    then
        echo "Error while running getFinalScores.bash"
        exit 3
    fi
    totalstud=$(( $totalstud + $(cat $args | wc -l ) ))
    while read line
    do
        currsc=$(echo $line | cut -d ',' -f2)
        currscname=$(echo $line | cut -d ',' -f1)
        if [[ $currsc > $maxsc ]]
        then
            maxsc=$currsc
            maxscname=$currscname
        fi
        let avgscore=$(( $avgscore + $(echo $line | cut -d ',' -f2) ))
    done < $( echo $args | cut -d '.' -f1 )".out"
done
avgscore=$(( $avgscore / $totalstud ))
echo "Total students: $totalstud"
echo "Average score: $avgscore"
echo "$maxscname had the highest score of $maxsc"
exit 0
