#!/bin/bash
# Version v0.0.1
# Created Date: 2023/10/04
# Author: Hugo ChunHo Lin (@1chooo)
# GitHub: github.com/1chooo
# Copyright (C) 2023 Hugo ChunHo Lin All rights reserved.

echo "Ready to check all students homework!!!"

# Create a file to store scores
echo "studentId,score" > hw00.csv

# Find all files that start with "HW00_" and end with ".ipynb"
ipynb_files=$(find . -name "HW00_*.ipynb")

marks=50

for file in $ipynb_files; do
    # Parse the .ipynb file using the jq tool
    first_output=$(jq -r '.cells[0].outputs[0].text[0]' "$file")
    second_output=$(jq -r '.cells[1].outputs[0].text[0]' "$file")

    echo "==="

    # Extract the * part from the filename
    filename=$(basename "$file")
    studentId="${filename#HW00_}"
    studentId="${studentId%.ipynb}"

    score=0
    
    if [[ "$first_output" == "Hello World" ]]; then
        score=$((score + marks))
        echo "$studentId meets the criteria in Q1, get: $marks marks"
    else
        echo "$studentId doesn't meet the criteria in Q1, get: 0 marks"
        echo "$studentId's Answer: $first_output (expected: Hello World)"
    fi

    if [[ "$second_output" == "test" ]]; then
        score=$((score + marks))
        echo "$studentId meets the criteria in Q2, get: $marks marks"
    else
        echo "$studentId doesn't meet the criteria in Q2, get: 0 marks"
        echo "$studentId's Answer: $second_output (expected: test)"
    fi

    echo "$studentId meets the all criteria, score: $score marks"

    # Write the * part of the filename and the score to the CSV file
    echo "$studentId,$score" >> hw00.csv
    echo "$studentId's score information has stored -> hw00.csv"
done

echo "==="
echo "All student HW00 has been checked!!!"
