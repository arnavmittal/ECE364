#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-18 11:24:31 -0500 (Mon, 18 Jan 2016) $
# $Revision: 85475 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Prelab01/exist.bash $

for allfiles in $@
do
    if [[ -r $allfiles ]]
    then
        echo "File $allfiles is readable!"
    elif [[ ! -e $allfiles ]]
    then
        touch $allfiles
    fi
done

exit 0
