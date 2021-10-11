#!/bin/bash
source  ~/.venvs/chaostk/Scripts/activate
export PYTHONPATH=`pwd`
chaos --verbose run experiment.json --fail-fast
