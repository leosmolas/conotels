rm -rf *.py*
touch __init__.py
for n in $( ls *.ui )
do
	echo $n
	pyuic4 $n -o ${n/.ui/.py}
done
