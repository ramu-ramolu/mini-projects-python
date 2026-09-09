students=[]
def add_student():
    name=input("enter student name: ")
    age=int(input("enter student age: "))
    gender=input("enter student gender: ")
    students.append({"name":name, "age":age, "gender":gender})
    print("\n student added successfully")
def view_student():
    if len(students)==0:
        print("still no records entered")
    else:
        print("-------------------")
        print("Students List:")
        for s in students:
            print("-------------------")
            print("Name:", s["name"])
            print("Age", s["age"])
            print("Gender", s["gender"])
            print("-------------------")  
while True:
    print("\n1.Add Student")
    print("2.View Student")
    print("3.Exit")
    choice=int(input("enter your choice:"))
    if choice== 1:
        add_student()
    elif choice== 2:
        view_student()
    elif choice== 3:
        print("Thankyou😊")
        break
    else:
        print("Invalid choice")