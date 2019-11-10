from collections import defaultdict

class School():

    def __init__(self):
        self.students = defaultdict(set)

    def add_student(self, name, grade):
        self.students[grade].add(name)

    def roster(self):
        lists_of_names = [sorted(self.students[key])
                          for key in sorted(self.students.keys())]
        return [name
                for names in lists_of_names
                for name in names]

    def grade(self, grade_number):
        return sorted(self.students[grade_number])
