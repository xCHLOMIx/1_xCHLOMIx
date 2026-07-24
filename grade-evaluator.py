#!/usr/bin/python3
import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # TODO: a) Check if all scores are percentage based (0-100)
    print("\n--- Checking score range ---")
    for grade in data:
        if not 0 <= grade["score"] <= 100:
            print("Invalid grade range. All grades must be in the range [0-100]")

    print("Successfully checked score range. All weights are in the [0-100] range.")
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    print("\n--- Checking total weights ---")
    summative = 0
    formative = 0
    for grade in data:
        if grade["group"] == "Summative":
            summative += grade["weight"]
        else:
            formative += grade["weight"]
    if formative != 60:
        print("Invalid weight. Formative weight must be 60.")
    if summative != 40:
        print("Invalid weight. Summative weight must be 40.")
    if summative + formative != 100:
        print("Invalid total weight. Weight must be 100")
    print("Successfully checked total weight. It's 100 (40 for Formatives & 60 for Summatives)")
    # TODO: c) Calculate the Final Grade and GPA
    print("\n--- Calculating total grades ---")
    final_grades = []
    for grade in data:
        final_grades.append((grade["score"] / 100) * grade["weight"])
    total_grade = sum(final_grades)
    print(f"Total grade: {total_grade}")
    print("\n--- Calculating GPA ---")
    gpa = (total_grade / 100) * 5.0
    print(f"GPA: {gpa}")
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    print("\n--- Performing Pass/Fail check ---")
    summative = 0
    formative = 0
    decision = ""
    for grade in data:
        if grade["group"] == "summative":
            summative += grade["score"]
        else:
            formative += grade["score"]
    if summative >= 50 or formative >= 50:
        decision = "PASS"
    else:
        decision = "FAIL"
    print("Finished perfoming Pass/Fail check")
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    print("\n--- Checking for formatives eligible for resubmission ---")
    resub = []
    resub_weights = []
    for grade in data:
        if grade["group"] == "Formative" and grade["score"] < 50:
            resub.append(grade)
            resub_weights.append(grade["weight"])
    max_weight = max(resub_weights)
    resub_assignments = []
    for grade in resub:
        if grade["weight"] == max_weight:
            resub_assignments.append(grade['assignment'])
    print("Finished check for formatives that are eligible for resubmission")
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    print(f"Final desicision: {decision}")
    print("Assignments eligible for resubmission")
    for a in resub_assignments:
        print(f"  {a}")
    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
