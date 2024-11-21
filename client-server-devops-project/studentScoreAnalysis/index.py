# Function to read ratings from file

def read_grades_from_file(filename):
    grades = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, grade = line.strip().split(',')
                    grades.append((name, int(grade)))  
                except ValueError:
                    print(f"Error str not corrected:=> '{line.strip()}' not view message.")
    except FileNotFoundError:
        print(f"Error: file {filename} not found.")
    return grades

# Function to calculate the average score
def calculate_average(grades):
    if not grades:
        return 0
    total = sum(grade for _, grade in grades)
    return total / len(grades)

# Function to find minimum and maximum scores
def find_min_and_max(grades):
    if not grades:
        return None, None
    grades_only = [grade for _, grade in grades]
    return min(grades_only), max(grades_only)

# The main part of the program
def main():
    filename = 'grades.txt'
    grades = read_grades_from_file(filename)

    if not grades:
        print("No data to process.") 
        return

    average = calculate_average(grades)
    min_grade, max_grade = find_min_and_max(grades)

    print("Analysis results:")
    print(f"Average score:=> {average:.2f}")
    print(f"Minimum score:=> {min_grade}")
    print(f"Maximum score:=> {max_grade}")

# Launching the program
if __name__ == "__main__":
    main()
