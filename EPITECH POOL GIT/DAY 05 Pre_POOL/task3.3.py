# Create a student dictionary
student = {
    "name": "John Doe",
    "academic_year": "Sophomore",
    "units": [
        {"name": "Web Development", "credits": 3, "grade": "A"},
        {"name": "Network and System Administration", "credits": 4, "grade": "B"},
        {"name": "Java", "credits": 3, "grade": "A"}
    ]
}
print("Student dictionary:", student)

# Create a grade weight mapping and calculate total credits and GPA
grade_weight_mapping = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}
total_credits = sum(unit["credits"] for unit in student["units"])
student["total_credits"] = total_credits

# Calculate GPA
total_points = sum(grade_weight_mapping[unit["grade"]] * unit["credits"] for unit in student["units"])
student["GPA"] = total_points / total_credits if total_credits else 0

print("Final student dictionary with GPA:", student)
