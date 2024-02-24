#!/bin/bash

start=1689133
end=1689159
n=74

#while [ $start -gt $end ]
while [ $start -lt $end ]
do
#	echo "start(before): $start"
#	echo "n(before): $n"
	python test3.py $start $n

	# 번호가 -1씩 감소하는 경우
#	start=$(expr $start - 1)
	# 번호가 +1씩 증가하는 경우
	start=$(expr $start + 1)

	n=$(expr $n + 1)
#	echo "start(after): $start"
#	echo "n(after): $n"
done

