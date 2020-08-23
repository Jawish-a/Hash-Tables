class HashTable:
    def __init__(self, dict_size):
        self.dict_size = dict_size
        self.dict = {
            "A":[None for item in range(dict_size)],
            "B":[None for item in range(dict_size)],
            "C":[None for item in range(dict_size)],
            "D":[None for item in range(dict_size)],
        }

    def hash(self, key, collision_count=0):
        hash_code = sum(key.encode())
        return hash_code + collision_count
    def compress(self, hash_code):
        return hash_code % self.dict_size

    # def insert(self,group, key, value):
    #     index = self.compress(self.hash(key))
    #     self.dict[group][index] = {key: value}

    def insert(self,group, key, value):
        collision_count = 0

        while True:
            hash_code = self.hash(key, collision_count)
            index = self.compress(hash_code)
            current_dict_value = self.dict[group][index]
            if (current_dict_value is None) or (current_dict_value == value):
                self.dict[group][index] = {key: value}
                break
            else:
                collision_count += 1



size_of_classes = int(input("What is the maximum number of students in class? "))


students_class_list = HashTable(size_of_classes)


print("-"*20)



students = [
    {
        "name": "Jean-Luc Garza",
        "age": 24
    },
    {
        "name": "Teddy Munoz",
        "age": 79
    },
    {
        "name": "Georgia Ali",
        "age": 17
    },
    {
        "name": "Vicky Calhoun",
        "age": 8
    },
    {
        "name": "Awais Weaver",
        "age": 65
    },
    {
        "name": "Athena Kline",
        "age": 52
    },
    {
        "name": "Zacharia Whitaker",
        "age": 38
    },
        {
        "name": "Clarice Davenport",
        "age": 99
    },
    {
        "name": "Viktoria Flynn",
        "age": 84
    },
    {
        "name": "Ianis Crossley",
        "age": 20
    },
    {
        "name": "Johnnie Owens",
        "age": 74
    },
    {
        "name": "Emily-Rose Erickson",
        "age": 33
    },
    {
        "name": "Adeel Nieves",
        "age": 100
    },
    {
        "name": "Dustin Villegas",
        "age": 98 
    },
    {
        "name": "Maxine Hughes",
        "age": 65
    },
    {
        "name": "Bilaal Harding",
        "age": 79
    },
    {
        "name": "Maddie Ventura",
        "age": 71
    },
    {
        "name": "Leroy Rees",
        "age": 44
    },
    {
        "name": "Wanda Frank",
        "age": 73
    },
    {
        "name": "Margaux Herbert",
        "age": 80
    },
    {
        "name": "Ali Rios",
        "age": 70
    },
    {
        "name": "Nigel Santiago",
        "age": 25
    },
    {
        "name": "Markus Greene",
        "age": 78
    },
    {
        "name": "Harlan Parrish",
        "age": 97
    },
    {
        "name": "Baran Davidson",
        "age": 43
    },
    {
        "name": "Seth Rodriguezh",
        "age": 67
    },
    {
        "name": "Diego Mayer",
        "age": 100
    },
]

for student in students:

    if student["age"] >= 90:
        students_class_list.insert("A", student["name"], student["age"])
    elif 90 > student["age"] >= 80:
        students_class_list.insert("B", student["name"], student["age"])
    elif 80 > student["age"] >= 70:
        students_class_list.insert("B", student["name"], student["age"])
    elif 70 > student["age"] >= 60:
        students_class_list.insert("B", student["name"], student["age"])
    elif 60 > student["age"]:
        continue


print("*"*30)
print("Class A students")
print("*"*30)
print(students_class_list.dict["A"])

print("")
print("*"*30)
print("Class B students")
print("*"*30)
print(students_class_list.dict["B"])

print("")
print("*"*30)
print("Class C students")
print("*"*30)
print(students_class_list.dict["C"])

print("")
print("*"*30)
print("Class D students")
print("*"*30)
print(students_class_list.dict["D"])


