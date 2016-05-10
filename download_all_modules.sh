#!/bin/bash
echo "Downloading modules of version "$1

target_version=$1

# Go to the modules directory
cd ../trytond/trytond/modules/

echo 'Downloading a list of all the modules...'
wget https://downloads.tryton.org/modules.txt

for i in $( cat modules.txt )
do
    echo ' '
    echo 'Cloning '$i
    git clone -b $target_version https://github.com/tryton/$i
done

echo 'Cleaning modules.txt file...'
rm modules.txt

cd ../../../trytond-scripts/
