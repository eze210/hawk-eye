#!/bin/bash

export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages

python ./src/cmc.py &
sleep 2
python ./src/cmb.py &
python ./src/Database/DBWrapper.py &
python ./src/RestAPI/Apiserver.py &
bash
