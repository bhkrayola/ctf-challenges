#!/bin/bash

# change hex values to align with png standard 89 50 4e 47
cp broken_forever.png solved.png
printf "\x89\x50\x4e\x47" | dd of=solved.png bs=1 seek=0 count=4 conv=notrunc
