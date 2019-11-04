class Garden(object):

    STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny",
                "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

    PLANTS = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}

    def __init__(self, diagram, students=None):
        students = sorted(students or self.STUDENTS)
        top, bottom = diagram.splitlines()
        self.cups = {}
        for index, student in enumerate(students[:len(top)]):
            a = index * 2
            b = a + 2
            self.cups.setdefault(student, [])
            self.cups[student].extend(
                self.PLANTS[plant] for plant in top[a:b]
            )
            self.cups[student].extend(
                self.PLANTS[plant] for plant in bottom[a:b]
            )

    def plants(self, student):
        return self.cups.get(student, [])
