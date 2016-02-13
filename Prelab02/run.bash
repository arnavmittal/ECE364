#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-25 22:37:35 -0500 (Mon, 25 Jan 2016) $
# $Revision: 86853 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Prelab02/run.bash $

if [[ ! $# == 2 ]]
then
    echo 'Usage: run.bash <input file> <output file>'
    exit 1
fi

if [[ ! -e $1 ]]
then
    echo "Error: $1 does not exist"
fi

OUTPUT=$2
if [[ -e $2 ]]
then
    echo -n "$2 exists.  Would you like to delete it? "
    read answer
    if [[ $answer == "y" || $answer == "yes" ]]
    then
        rm $2
    else
        echo -n "Enter a new filename: "
        read newname
        touch $newname 
        OUTPUT=$newname
    fi
fi

file_exec="quick_sim"

if [[ -e $file_exec ]]
then
    rm $file_exec
fi

if $(gcc $1 -o $file_exec)
then
    echo -n ""
else
    echo "$file_exec could not be compiled!"
    exit 1
fi

select=0
max_time=100000
max_c=0
max_i=0
max_p=0
for cache in {1,2,4,8,16,32}
do
    for issues in {1,2,4,8,16}
    do
        cmnd=$($file_exec $cache $issues a)
        while read line
        do
            value=$(echo $line | cut -d':' -f2,4,6,8,10)
            time_val=$(echo "$value" | cut -d":" -f5)
            if (($time_val<=$max_time))
            then
                max_time=$time_val
                max_p=1
                max_c=$cache
                max_i=$issues
            fi
            echo $value >> $OUTPUT
        done <<< "$cmnd"

        cmnd=$($file_exec $cache $issues i)
        while read line
        do
            value=$(echo $line | cut -d':' -f2,4,6,8,10)
            time_val=$(echo "$value" | cut -d":" -f5)
            if (($time_val<=$max_time))
            then
                max_time=$time_val
                max_p=2
                max_c=$cache
                max_i=$issues
            fi
            echo $value >> $OUTPUT
        done <<< "$cmnd"
    done
done
if (( $max_p == '2' ))
then
    echo "Fastest run time achieved by Intel Core i7 with cache size $max_c and issue width $max_i was $max_time"
else
    echo "Fastest run time achieved by AMD Opteron with cache size $max_c and issue width $max_i was $max_time"
fi
exit 0

