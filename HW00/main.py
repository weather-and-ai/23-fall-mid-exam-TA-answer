# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/04
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
GitHub: github.com/1chooo
Copyright (C) 2023 Hugo ChunHo Lin All rights reserved.
'''

import os
import json

print("Ready to check all students homework!!!")

# Create a file to store scores
with open("hw00.csv", "w") as csv_file:
    csv_file.write("studentId,score\n")

ipynb_files = [file for file in os.listdir() if file.startswith("HW00_") and file.endswith(".ipynb")]

marks = 50

for file in ipynb_files:
    print("===")

    student_id = file.replace("HW00_", "").replace(".ipynb", "")

    score = 0
    
    try:
        with open(file, "r") as nb_file:
            notebook = json.load(nb_file)
        
        first_output = notebook["cells"][0]["outputs"][0]["text"][0].strip("\n")
        if first_output == "Hello World":
            score += marks
            print(f"{student_id} meets the criteria in Q1, get: {marks} marks")
        else:
            print(f"{student_id} doesn't meet the criteria in Q1, get: 0 marks")
            print(f"{student_id}'s Answer: {first_output} (expected: Hello World)")
        
        second_output = notebook["cells"][1]["outputs"][0]["text"][0].strip("\n")
        if second_output == "test":
            score += marks
            print(f"{student_id} meets the criteria in Q2, get: {marks} marks")
        else:
            print(f"{student_id} doesn't meet the criteria in Q2, get: 0 marks")
            print(f"{student_id}'s Answer: {second_output} (expected: test)")
        
        print(f"{student_id} meets the all criteria, score: {score} marks")

        # Write the * part of the filename and the score to the CSV file
        with open("hw00.csv", "a") as csv_file:
            csv_file.write(f"{student_id},{score}\n")
            print(f"{student_id}'s score information has stored -> hw00.csv")
    
    except Exception as e:
        print(f"Error processing {file}: {str(e)}")

print("===")
print("All student HW00 has been checked!!!")
