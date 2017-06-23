#!/bin/bash

export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages

python ./src/cmc.py &
python ./src/cmb.py &
bash
