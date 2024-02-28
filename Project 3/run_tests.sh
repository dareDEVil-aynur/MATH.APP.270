#!/bin/bash

SCRIPT="secret_socities.py"

TEST_DIR="tests"

FULL_SCRIPT_PATH="$(pwd)/$SCRIPT"

for i in {1..3}
do
  echo "Running test case $i"
  python3 "$FULL_SCRIPT_PATH" "$TEST_DIR/test$i.txt" 
  echo "------------------------------------------------"
  echo " "
done
