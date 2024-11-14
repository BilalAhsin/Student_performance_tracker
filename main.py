class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = ['Math', 'Science', 'English']  # Restricted to 3 subjects
        self.scores = []
    
    def add_scores(self):
        """Adds scores for each subject to the student's scores list, handling invalid input and range checks."""
        for subject in self.subjects:
            while True:
                try:
                    score = int(input(f"Enter score for {subject} (0-100): "))
                    if 0 <= score <= 100:
                        self.scores.append(score)
                        break  # Exit the loop if the input is valid
                    else:
                        print("Score must be between 0 and 100. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter an integer value for the score.")

    def average(self):
        """Calculates and returns the average score of the student, handling division by zero."""
        if not self.scores:
            print(f"No scores available for {self.name}. Returning average as 0.")
            return 0
        return sum(self.scores) / len(self.scores)

    def status(self):
        """Determines pass/fail status based on average score."""
        return "Status: Pass" if self.average() >= 40 else "Status: Fail"


class StudentPerformanceTracker:
    def __init__(self):
        self.students = [] 

    def add_student(self):
        """Adds students until the user chooses to stop, with input validation for names and confirmation choice."""
        while True:
            # Name input validation
            while True:
                name = input("Enter student's name: ").strip()
                if name:
                    break  # Exit the loop if name is not empty
                print("Name cannot be empty. Please enter a valid name.")
            
            student = Student(name)
            student.add_scores()
            self.students.append(student)
            
            # Ask if the user wants to add another student or exit
            while True:
                cont = input("If you want to add a new student, type 'y'; otherwise, type 'e': ").strip().lower()
                if cont in ['y', 'e']:
                    break  # Exit the loop if input is valid
                print("Invalid choice. Please type 'y' to continue or 'e' to exit.")
                
            if cont == 'e':
                break

    def class_average(self):
        """Calculates the overall class average, handling division by zero if no students are present."""
        if not self.students:
            print("No students have been added. Returning class average as 0.")
            return 0
        total_avg = sum(student.average() for student in self.students)
        return total_avg / len(self.students)

    def show_performance(self):

        for student in self.students:
            print(f"\nPerformance for {student.name}:")
            avg = student.average()
            print(f"Average: {avg:.2f}")
            print(student.status())



tracker = StudentPerformanceTracker()

tracker.add_student()

tracker.show_performance()

print(f"\nClass Average: {tracker.class_average():.2f}")
