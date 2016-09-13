#!/bin/bash
#
DIR=$(pwd)
DIR="$DIR/.venv/bin/activate"
source $DIR
python make-backup.py
deactivate
