#!/bin/bash
TEMPLATE_DIR="dayN-py"
NEXT_DIR="day$1"
mkdir ${NEXT_DIR}
cp $TEMPLATE_DIR/* $NEXT_DIR
cd $NEXT_DIR
olds=("dayN.py" "dayN_test.py")
IFS=
for i in "${olds[@]}"; do
  cat $i | while read line; do
    echo ${line//N/$1} >> ${i/N/$1}
  done
  rm $i
done