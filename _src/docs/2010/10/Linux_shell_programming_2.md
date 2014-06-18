**if command**

    :::bash
    if cat $1; then
        echo "\n\nFile $1, foutnd and successfully echoed"
    else
        echo "No file found."
    fi

we can put `if-else` into one line like this:

    :::bash
    if [ $USER = 'mitnk' ] ; then echo 'Hello'; else echo 'Hi'; fi

**test command or [expr]**

    :::bash
    if test $1 -gt 0; then
        echo "$1 number is positive"
    fi

or

    :::bash
    if [ $1 -gt 0 ]; then
        echo "$1 number is positive"
    fi

**For Mathematics**


    :::bash
    -eq  ==
    -ne  !=
    -lt   <
    -le  <=
    -gt  >
    -ge  >=


**For string Comparisons use**


    :::bash
    string1 = string2	string1 is equal to string2
    string1 != string2	string1 is NOT equal to string2
    string1	string1 is NOT NULL or not defined 
    -n string1	string1 is NOT NULL and does exist
    -z string1	string1 is NULL and does exist


**Shell also test for file and directory types**


    :::bash
    -e file Is File exist
    -s file   	Non empty file
    -f file   	Is File exist or normal file and not a directory 
    -d dir    	Is Directory exist and not a file
    -w file  	Is writeable file
    -r file   	Is read-only file
    -x file   	Is file is executable


**Logical Operators**


    :::bash
    ! expression	 Logical NOT
    expression1  -a  expression2	Logical AND
    expression1  -o  expression2	Logical OR


**Multilevel if-then-else**


    :::bash
    if [ $1 -gt 0 ]; then
      echo "$1 is positive"
    elif [ $1 -lt 0 ]
    then
      echo "$1 is negative"
    elif [ $1 -eq 0 ]
    then
      echo "$1 is zero"
    else
      echo "Opps! $1 is not number, give number"
    fi


**for Loop**


    :::bash
    for i in 1 2 3 4 5
    do
      echo "Welcome $i times"
    done

    for ((  i = 0 ;  i &lt;= 5;  i++  ))
    do
      echo "Welcome $i times"
    done


**while Loop**


    :::bash
    n=$1
    i=1
    while [ $i -le 10 ]
    do
      echo "$n * $i = `expr $i \* $n`"
      i=`expr $i + 1`
    done


**The case Statement**


    :::bash
    #
    # if no vehicle name is given
    # i.e. -z $1 is defined and it is NULL
    #
    # if no command line arg

    if [ -z $1 ]
    then
      rental="*** Unknown vehicle ***"
    elif [ -n $1 ]
    then
    # otherwise make first arg as rental
      rental=$1
    fi

    case $rental in
       "car") echo "For $rental Rs.20 per k/m";;
       "van") echo "For $rental Rs.10 per k/m";;
       "jeep") echo "For $rental Rs.5 per k/m";;
       "bicycle") echo "For $rental 20 paisa per k/m";;
       *) echo "Sorry, I can not gat a $rental for you";;
    esac


**How to de-bug the shell script?**


    :::bash
    $ cat > dsh1.sh
    #
    # Script to show debug of shell
    #
    tot=`expr $1 + $2`
    echo $tot

    $ sh -v dsh1.sh 4 5


Reference: [freeos.com](http://www.freeos.com/guides/lsst/index.html)
