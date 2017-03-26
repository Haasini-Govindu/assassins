#!/bin/bash

sleep 20

python create_db.py

flask run --host=0.0.0.0
