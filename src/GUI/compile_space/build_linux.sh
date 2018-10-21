#!/usr/bin/env bash

#cp ./geo_gui.spec ./compile_space/
#cp ./icon.ico ./compile_space/
#cp ./geo_gui.py./compile_space/
cp ../geo_gui.py ./
cp ../../Current\ Models/*.py ./
cp ../../Current\ Models/Archimedean/*.py ./
cp ../../Current\ Models/Hyperbolic/*.py ./
cp ../../Current\ Models/Misc./*.py ./
cp ../../Current\ Models/Platonic\ Solids/*.py ./
cp ../../Current\ Models/Surfaces/*.py ./
cp ../../Current\ Models/Topological/*.py ./
cp ../../Current\ Models/Two\ Space/*.py ./
cp ../../In\ Development/*.py ./

pyinstaller geo_gui.spec --clean

#mv ./build/ ./compile_space/

rm *.py
rm -r build/
rm -r __pycache__