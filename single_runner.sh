#!/bin/bash

PROGRAM_NAME=$1
MY_NAME=`basename $0`
process_info=`ps -ef|grep $PROGRAM_NAME|grep -v $MY_NAME|grep -v grep`
if [ "$process_info" != "" ];then
    echo "$PROGRAM_NAME is running."
    exit 0
fi
$PROGRAM_NAME

