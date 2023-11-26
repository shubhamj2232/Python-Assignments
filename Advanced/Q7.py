# Using for loop
def construct_dictionary_for_loop(students, subjects):
    student_subject_dict = {}
    for i in range(len(students)):
        student_subject_dict[students[i]] = subjects[i]
    return student_subject_dict

# Using dictionary comprehension
def construct_dictionary_comprehension(students, subjects):
    return {students[i]: subjects[i] for i in range(len(students))}

#Input
students_list = ["Sam", "Alice", "Mona"]
subjects_list = ["Commerce", "Science", "Computer"]

# Construct dictionary using for loop
result_for_loop = construct_dictionary_for_loop(students_list, subjects_list)

# Construct dictionary using dictionary comprehension
result_comprehension = construct_dictionary_comprehension(students_list, subjects_list)

# Results
print("Using For Loop:")
print(result_for_loop)

print("\nUsing Dictionary Comprehension:")
print(result_comprehension)
