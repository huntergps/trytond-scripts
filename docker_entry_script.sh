#!/usr/bin/env bash

echo "Generating config..."
python /tryton/trytond-scripts/generate_config.py

echo "First run."

echo "Generating password file..."
echo "$TRYTONPASS" > $TRYTONPASSFILE

echo "Initializing the DB..."
/usr/local/bin/trytond -c $TRYTOND_CONFIG -d $DATABASE_NAME -v --all

echo "Removing password file..."
rm $TRYTONPASSFILE

if [ $1 == 'first-run' ]; then
    echo "Install ALL the modules..."
    python /tryton/trytond-scripts/install_modules.py
fi

echo "Launching Trytond Server..."
exec /usr/local/bin/trytond -c $TRYTOND_CONFIG -d $DATABASE_NAME -v
