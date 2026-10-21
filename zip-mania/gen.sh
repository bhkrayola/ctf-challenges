#!/bin/bash

cat flag.txt | base64 | xxd -p | tr -d '\n'
