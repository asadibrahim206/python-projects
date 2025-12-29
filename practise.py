class studnets:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.school = "XYZ school"
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {self.school}")

def main():
    student1 = studnets("Asad", 20)
    student2 = studnets("Ali", 22)

    student1.info()
    student2.info()

main()
