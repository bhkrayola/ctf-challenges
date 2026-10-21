#!/bin/bash

cp flag.txt flag.txt.tmp
for i in {1..1000}
do
  zip flag.txt.tmp flag.txt.zip
  mv flag.txt.tmp flag.txt.zip
done
