#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-19 17:10:28 -0500 (Tue, 19 Jan 2016) $
# $Revision: 86255 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Lab01/getFinalScores.bash $



if [[ ! $# == 1 ]]
then
    echo "Usage: ./getFinalScores.bash <filename>"
    exit 1
fi

if [[ ! -e $1 ]]
then
    echo "Error reading input file: $1"
    exit 2
fi

output_file=$( echo $1 | cut -d '.' -f1 )".out"

if [[ -e $output_file ]]
then
    echo "Output file $output_file already exists."
    exit 3
fi

while read line
do
    name=$(echo $line | cut -d ',' -f1)
    asnmt=$(echo $line | cut -d ',' -f2) 
    mt1=$(echo $line | cut -d ',' -f3)
    mt2=$(echo $line | cut -d ',' -f4)
    proj=$(echo $line | cut -d ',' -f5)
    final_score=$(( 15 * $asnmt / 100 + 30 * $mt1 / 100 + 30 * $mt2 / 100 + 25 * $proj / 100 ))
    echo "$name,$final_score" >> $output_file
done < $1
exit 0
