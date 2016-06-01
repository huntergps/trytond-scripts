#!/usr/bin/env bash

echo "Generating config..."
python /tryton/trytond-scripts/generate_config.py

echo "Generating password file..."
echo "$TRYTONPASS" > $TRYTONPASSFILE

echo "Initializing the DB..."
trytond-admin -c $TRYTOND_CONFIG -d $DATABASE_NAME -v --all

echo "Removing password file..."
rm $TRYTONPASSFILE

echo "Installing additional modules..."
$1

echo "Launching Trytond Server..."
exec trytond -c $TRYTOND_CONFIG -d $DATABASE_NAME -v
