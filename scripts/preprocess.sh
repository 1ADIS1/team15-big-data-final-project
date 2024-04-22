#!/bin/bash
dataset_url="https://disk.yandex.com/d/NdpjIZDmP24kng"

# Check if yadisk-direct is installed
if command -v yadisk-direct >/dev/null 2>&1; then
  dataset_direct_url="$(yadisk-direct $dataset_url)"
else
  echo "Command yadisk-direct does not exist! Please, run 'pip install -r requirements.txt'"
  exit
fi

# Pull dataset from the Yandex.Disk
if wget $dataset_direct_url -O data/usedcars.zip; then
  echo "Success!"
else
  echo "Something went wrong!"
  exit
fi

# Unzip file and remove artifacts
unzip data/usedcars.zip -d data/raw/
rm data/usedcars.zip

# Run data preprocessing
python ./scripts/data-preprocessing.py 'data/raw/vehicles.csv' --output 'data/processed/sliced.csv'
