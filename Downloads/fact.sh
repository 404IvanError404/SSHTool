#!/bin/bash
echo "Введите число для подсчета факториала -"
read counter
fact=1
if [ $counter -lt 0 ]
then
echo "Введите положительное число/ноль -"
else
while [ $counter -gt 0 ]
do
fact=$(( $fact * $counter ))
counter=$(( $counter - 1 ))
done
echo "->" $fact
fi
exit 0
