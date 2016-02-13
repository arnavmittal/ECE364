#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-18 18:54:54 -0500 (Mon, 18 Jan 2016) $
# $Revision: 85723 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Prelab01/svncheck.bash $

n=1

while read line
do
    a[$n]=$line
    let n=$n+1
done < file_list

for file in ${a[*]}
do
    check=$( svn status $file | cut -c 1 )
    if [[ -e $file ]]
    then
        if [[ $check == '?' ]]
        then
            if [[ ! -x $file ]] 
            then
                echo "Do you want to make the file executable?"
                read answer
                if [[ $answer == 'y' ]]                        
                then
                    chmod +x $file
                fi                                            
            fi                                         
            svn add $file
        else
            if [[ ! -x $file ]]
            then
                svn propset svn:executable ON $file
            fi
        fi
    else        
        if [[ -z  $check ]]
        then
            echo "Error: File $file appears to not exist here or in the svn"
        exit 0
    fi
fi

done

svn commit -m "Auto-committing code"

exit 0
