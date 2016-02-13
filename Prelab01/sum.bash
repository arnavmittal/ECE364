#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-18 10:48:11 -0500 (Mon, 18 Jan 2016) $
# $Revision: 85470 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Prelab01/sum.bash $
sum=0
while ((! $# == 0 ))
do
    ((sum=$1+sum))
    shift
done

echo $sum

exit 0
