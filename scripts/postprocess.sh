#!/bin/bash

# Removes all checkpoint folders created by Jupiter Lab
# Those folders messes up with pylint
echo "Removing all checkpoint folders..."
find . -name "*checkpoints" | xargs rm -r -f
