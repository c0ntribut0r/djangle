#!/bin/sh
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $ROOT/../..

python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt -r envs/local/requirements.txt

cp envs/local/.env .env
