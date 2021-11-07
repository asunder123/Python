#!/bin/bash
source  ~/.venvs/chaostk/Scripts/activate
export PYTHONPATH=`pwd`
chaos run experiment.json --fail-fast
