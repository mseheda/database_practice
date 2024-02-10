import random

group_names = ['CS101', 'CS102', 'CS103', 'CS104', 'CS105']  # Define your group names here

first_names = ["John", "Jane", "Emily", "Chris", "Alex", "Michael", "Emma", "Olivia",
               "James", "Isabella", "Sophia", "Amelia", "Lucas", "Charlotte", "Aiden", "Mia",
               "Ethan", "Harper", "Mason", "Ella", "Ava", "William", "Sophie", "Benjamin", "Zoe",
               "Liam", "Lily", "Noah", "Grace", "Oliver", "Chloe", "Elijah", "Aria", "Logan",
               "Avery", "Alexander", "Evelyn", "Jacob", "Abigail", "Daniel", "Nora", "Matthew",
               "Scarlett", "David", "Madison", "Joseph", "Layla", "Jackson", "Riley", "Samuel"]
last_names = ["Doe", "Smith", "Davis", "Brown", "Johnson", "Wilson", "Moore", "Taylor",
              "Anderson", "Thomas", "Jackson", "Martin", "Lee", "Hall", "Young", "King",
              "Wright", "Lopez", "Hill", "Scott", "Adams", "James", "Turner", "Green",
              "Evans", "Baker", "Harris", "Robinson", "Clark", "Lewis", "Walker", "Parker",
              "Cook", "Edwards", "Morris", "Rivera", "Cooper", "Morgan", "Peterson", "Cooper",
              "Reed", "Bailey", "Bell", "Gonzalez", "Carter", "Phillips", "Mitchell", "Ross",
              "Reyes", "Stewart", "Morales", "Murphy", "Sanchez", "Foster", "Clark"]

def generate_student_name():
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    return name

def generate_students_inserts_to_file(num_students_per_group, group_names, filename):
    """Generates INSERT statements and writes them to a file in batches."""
    with open(filename, 'w') as file:
        file.write("INSERT INTO students (student_name, group_id) VALUES\n\t")
        total_records = num_students_per_group * len(group_names)
        for i in range(total_records):
            group_id = (i // num_students_per_group) + 1
            student_name = generate_student_name()
            file.write(f"('{student_name}', {group_id})")
            # Check if it's the last record overall or in a group, to avoid adding a comma
            if (i + 1) % num_students_per_group == 0 or i + 1 == total_records:
                if i + 1 < total_records:  # Not the last record, start a new INSERT statement
                    file.write(";\n\nINSERT INTO students (student_name, group_id) VALUES\n\t")
                else:  # Last record
                    file.write(";")
            else:
                file.write(",\n\t")

    print(f"Output written to {filename} with {total_records} records.")


# Example usage
num_students_per_group = 7500  # Adjust the number of students per group as needed
filename = "output.sql"

generate_students_inserts_to_file(num_students_per_group, group_names, filename)
