#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-02-16 17:19:18 -0500 (Tue, 16 Feb 2016) $
# $Revision: 88285 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Lab05/scheduler.bash $

if [[ ! $# == 1 ]]
then
    echo 'Usage: scheduler.bash <input file>'
    exit 1
fi

if [[ ! -e $1 ]]
then
    echo "Error: $1 does not exist."
    exit 2
fi

if [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable."
    exit 2
fi

if [[ -e "schedule.out" ]]
then
    echo "Error: schedule.out already exists."
    exit 3
fi

output="schedule.out"
check=1
while read -a line
do
	if (( check==1 ))
	then
		echo "        7:00 8:00 9:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00" >> $output
		check=0
	fi
	name=$(echo ${line[0]})
	echo -n $name >> $output
	if [[ ${line[1]} == "7:00" ]]
	then
		my_list=[]
	fi
	echo "  " >> $output
	
done <$1

exit 0
