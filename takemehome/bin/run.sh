#!/bin/bash

printf "can you find the way home\n"

cd /home/
MY_PROMPT='$ '
while :
do
  echo -n "$MY_PROMPT"
  read line
  eval "$line"
  done

exit 0
