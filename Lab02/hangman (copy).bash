#! /bin/bash
#
# $Author: ee364d07 $
# $Date: 2016-01-26 17:04:52 -0500 (Tue, 26 Jan 2016) $
# $Revision: 86975 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364d07/Lab02/hangman%20(copy).bash $
check=0
while (( $check == 0 ))
do
    number=$RANDOM
    if (( number < 3 ))
    then
        option=$number
        echo "$number"
        check=1
    fi
done

if (( $number == 1 ))
then
    value="b a n a n a"
elif (( $number == 2 ))
then
    value="p a r s i m o n i o u s"
else
    value="s e s q u i p e d a l i a n"
fi

word=($value)
#(( count=$(echo $word |wc -c) - 1 ))
echo "Your word is ${#word[*]} letters long."
echo ${!word[*]}
echo -n "Word is: "

exit 0

