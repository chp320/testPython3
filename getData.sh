#!/bin/bash

start=194393
end=194342
n=1

while [ $start -gt $end ]
do
#	echo "start(before): $start"
#	echo "n(before): $n"
	python test3.py $start $n

	start=$(expr $start - 1)
	n=$(expr $n + 1)
#	echo "start(after): $start"
#	echo "n(after): $n"
done

