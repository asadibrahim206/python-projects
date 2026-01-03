
# n= 5

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j==0 or j==n-1:
#             print("*" , end=" ")
#         else:
#             print(" ", end=" ")
#     print()


class Student:
    def __init__(self,n):
        print("asad")

    def calc(n):
        for i in range(n):
            for j in range(n):
                if i == 0 or i==n or j == 0 or j == n:
                    print("*")
        print()

def main():
    student =  Student()
    student.calc(5)

if __name__ == "__main__":