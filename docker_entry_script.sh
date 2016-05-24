#!/usr/bin/env bash

echo "Generating config..."
python /tryton/trytond-scripts/generate_config.py

echo "Generating password file..."
echo "$TRYTONPASS" > $TRYTONPASSFILE

echo "Initializing the DB..."
/usr/local/bin/trytond -c $TRYTOND_CONFIG -d $DATABASE_NAME -v --all

echo "Removing password file..."
rm $TRYTONPASSFILE

#echo "Launching Trytond Server..."
#exec /usr/local/bin/trytond -c $TRYTOND_CONFIG -d $DATABASE_NAME -v
