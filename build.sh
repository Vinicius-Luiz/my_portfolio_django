#!/bin/bash

# Install Dependencies
pip install -r requiriments.txt

# Run Migration
python manage.py collectstatic --no-input
python manage.py migrate