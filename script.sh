#!/bin/bash

versions=(3.7 3.8 3.9 3.10 3.11)

for version in ${versions[*]}
do
    pyenv shell $version
    python3 --version

    python3 main.py
    echo "\n"
done