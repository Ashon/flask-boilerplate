#!/bin/bash

virtualenv venv -p `which python3`
venv/bin/pip install -r requirements.txt
