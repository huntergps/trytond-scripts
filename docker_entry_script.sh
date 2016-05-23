#!/usr/bin/env bash

python /tryton/trytond-scripts/generate_config.py

exec /usr/local/bin/trytond "$@"
