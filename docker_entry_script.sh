#!/usr/bin/env bash

echo "Generating config..."
python /tryton/trytond-scripts/generate_config.py

echo "Generating password file..."
echo "$TRYTONPASS" > $TRYTONPASSFILE

echo "Initializing the DB..."
trytond-admin -c $TRYTOND_CONFIG -d $DATABASE_NAME -v --all

echo "Removing password file..."
rm $TRYTONPASSFILE

if [ $1 == 'first-run' ]; then
    echo "Install ALL the modules..."
    python /tryton/trytond-scripts/install_modules.py
else
    echo "No first run since TRYTOND_FIRST_RUN="$1
fi

echo "Launching Trytond Server..."
exec trytond -c $TRYTOND_CONFIG -d $DATABASE_NAME -v
