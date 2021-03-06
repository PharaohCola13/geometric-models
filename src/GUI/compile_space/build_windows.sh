#!/usr/bin/env bash
cp ../geo_windows.py ./
cp ../../Current\ Models/*.py ./
cp ../../Current\ Models/Archimedean/*.py ./
cp ../../Current\ Models/Hyperbolic/*.py ./
cp ../../Current\ Models/Misc/*.py ./
cp ../../Current\ Models/Platonic\ Solids/*.py ./
cp ../../Current\ Models/Surfaces/*.py ./
cp ../../Current\ Models/Topological/*.py ./
cp ../../Current\ Models/Two\ Space/*.py ./
cp ../../In\ Development/*.py ./

pyinstaller GeoExpanse_wind.spec --clean

rm *.py
rm -r build/
rm -r __pycache__
