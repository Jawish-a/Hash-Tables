students = [
    {
        "name": "Jean-Luc Garza",
        "score": 24
    },
    {
        "name": "Teddy Munoz",
        "score": 79
    },
    {
        "name": "Georgia Ali",
        "score": 17
    },
    {
        "name": "Vicky Calhoun",
        "score": 8
    },
    {
        "name": "Awais Weaver",
        "score": 65
    },
    {
        "name": "Athena Kline",
        "score": 52
    },
    {
        "name": "Zacharia Whitaker",
        "score": 38
    },
        {
        "name": "Clarice Davenport",
        "score": 99
    },
    {
        "name": "Viktoria Flynn",
        "score": 84
    },
    {
        "name": "Ianis Crossley",
        "score": 20
    },
    {
        "name": "Johnnie Owens",
        "score": 74
    },
    {
        "name": "Emily-Rose Erickson",
        "score": 33
    },
    {
        "name": "Adeel Nieves",
        "score": 100
    },
    {
        "name": "Dustin Villegas",
        "score": 98 
    },
    {
        "name": "Maxine Hughes",
        "score": 65
    },
    {
        "name": "Bilaal Harding",
        "score": 79
    },
    {
        "name": "Maddie Ventura",
        "score": 71
    },
    {
        "name": "Leroy Rees",
        "score": 44
    },
    {
        "name": "Wanda Frank",
        "score": 73
    },
    {
        "name": "Margaux Herbert",
        "score": 80
    },
    {
        "name": "Ali Rios",
        "score": 70
    },
    {
        "name": "Nigel Santiago",
        "score": 25
    },
    {
        "name": "Markus Greene",
        "score": 78
    },
    {
        "name": "Harlan Parrish",
        "score": 97
    },
    {
        "name": "Baran Davidson",
        "score": 43
    },
    {
        "name": "Seth Rodriguezh",
        "score": 67
    },
    {
        "name": "Diego Mayer",
        "score": 100
    },
]


class HashTable:
    def __init__(self, class_size):
        self.class_size = class_size
        self.classes = {
            "A":[],
            "B":[],
            "C":[],
            "D":[],
        }

    def hash(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return None

    def insert(self, name, score):
        class_group = self.hash(score)
        if class_group:
            if len(self.classes[class_group]) < self.class_size:
                self.classes[class_group].append({"name": name, "score": score})
            else:
                print("no more room")



size_of_classes = int(input("What is the maximum number of students in class? "))


students_class_list = HashTable(size_of_classes)


print("-"*20)


for student in students:
    students_class_list.insert(student["name"], student["score"])


print("*"*30)
print("Class A students")
print("*"*30)
for i in students_class_list.classes["A"]:
    print(i["name"] + " | " + str(i["score"]))

print("")
print("*"*30)
print("Class B students")
print("*"*30)
for i in students_class_list.classes["B"]:
    print(i["name"] + " | " + str(i["score"]))

print("")
print("*"*30)
print("Class C students")
print("*"*30)
for i in students_class_list.classes["C"]:
    print(i["name"] + " | " + str(i["score"]))

print("")
print("*"*30)
print("Class D students")
print("*"*30)
for i in students_class_list.classes["D"]:
    print(i["name"] + " | " + str(i["score"]))


