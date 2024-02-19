#!/bin/bash

SCRIPT="assignment1_template.py"

TEST_DIR="tests"

FULL_SCRIPT_PATH="$(pwd)/$SCRIPT"

for i in {1..11}
do
  echo "Running test case $i"
  python3 "$FULL_SCRIPT_PATH" "$TEST_DIR/testgraph_$i" "$TEST_DIR/testset_$i" "$TEST_DIR/testpair_$i"
  echo "-----------------------------------------------------------------------"
done
