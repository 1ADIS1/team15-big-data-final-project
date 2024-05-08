#!/bin/bash
dataset_url="https://disk.yandex.com/d/NdpjIZDmP24kng"

# Check if dataset already exists
already_exists=false
if [ -f data/raw/vehicles.csv ]; then
  already_exists=true
  echo "Dataset already exists! Skipping downloading..."
fi

if [ "$already_exists" = false ]; then

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
  unzip -o data/usedcars.zip -d data/raw/
  rm data/usedcars.zip

fi

echo "Data is ready!"

# Run data preprocessing
echo "Running data preprocessing. Please, wait..."
python3 scripts/stage1/data_preprocessing.py "data/raw/vehicles.csv" --output "data/processed/sliced.csv"
