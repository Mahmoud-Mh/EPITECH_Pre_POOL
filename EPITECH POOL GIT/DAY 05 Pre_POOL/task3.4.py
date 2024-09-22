# Create a student dictionary
student = {
    "name": "John Doe",
    "academic_year": "Sophomore"
}
print("Student dictionary:", student)

# Create an array of students and sort them
students = [
    {"name": "Alice", "GPA": 3.5},
    {"name": "Bob", "GPA": 2.8},
    {"name": "Charlie", "GPA": 3.9}
]

# Sort by name
students_sorted_by_name = sorted(students, key=lambda x: x["name"])
print("Students sorted by name:", students_sorted_by_name)

# Sort by GPA in ascending order
students_sorted_by_gpa_asc = sorted(students, key=lambda x: x["GPA"])
print("Students sorted by GPA (ascending):", students_sorted_by_gpa_asc)

# Sort by GPA in descending order
students_sorted_by_gpa_desc = sorted(students, key=lambda x: x["GPA"], reverse=True)
print("Students sorted by GPA (descending):", students_sorted_by_gpa_desc)
