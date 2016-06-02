#!/bin/bash
echo "Downloading modules of version "$1

target_version=$1
target_version_next=$(awk "BEGIN {print $target_version+0.1}")

echo 'Downloading a list of all the modules...'
wget https://downloads.tryton.org/modules.txt

for i in $( cat modules.txt )
do
    pip install "trytond_$i>=$target_version.0,<$target_version_next.0"
     break  # temp hax for tests
done

echo 'Cleaning modules.txt file...'
rm modules.txt
