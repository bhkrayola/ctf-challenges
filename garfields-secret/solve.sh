#!/bin/bash

wget https://garfieldlasagnamonday.com/static/flag.png
zsteg flag.png | grep -oE "flag{.*}"
rm flag.png
