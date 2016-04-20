#!/bin/bash

# Go to the modules directory
cd ../trytond/trytond/modules/

echo 'Downloading a list of all the modules...'
wget https://downloads.tryton.org/modules.txt

for i in $( cat modules.txt )
do
        echo ' '
        echo 'Cloning '$i
        git clone https://github.com/tryton/$i

#        echo 'Checking out to 3.8 version'
#        cd $i
#        git checkout 3.8
#        cd ..
done

echo 'Cleaning modules.txt file...'
rm modules.txt

cd ../../../trytond-scripts/
