#!/bin/bash

# Create Data folder if it doesn't exist
if [ ! -d "Data" ]; then
    mkdir Data
    echo "Created Data folder."
fi

# Create Results folder if it doesn't exist
if [ ! -d "Results" ]; then
    mkdir Results
    echo "Created Results folder."
fi

# Run Python script
python3 Hunter.py
