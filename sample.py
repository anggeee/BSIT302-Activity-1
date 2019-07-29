class Angge:

    data = True

    my_empty = []

    my_list = ["""
            EMPLOYEE MANAGEMENT SYSTEM BY: ANGGE
            Choose your Option
            [1] Add New Employee
            [2] Enter Hourly of Employee
            [3] Show Employee Information
            [4] Exit

            **********************************
        """]
    for x in my_list:
        print(x)
        
    #print(my_list)

    def __init__(self, name, department, position, rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate

    def getSalary(self, hourly):
        return self.rate * hourly

    num = (input("Enter Option: "))

    if num == "1":
        #Name
        name = (input("Enter new Employee Name: "))
        my_empty.append(name)

        #Department
        department = (input("Enter Department: "))
        my_empty.append(department)

        #Postion
        position = (input("Enter Position: "))
        my_empty.append(position)

        #Rate
        rate = (input("Enter Rate: "))
        my_empty.append(rate)

        print(x)

    elif num == "2":
        #EmployeeNumber
        emplonum = (input("Employee Number: "))
        empHours = (input("Employee Hours: "))
        salary = empHours * rate
        print ("Employee Salary for" + empHours + "hours is ")
               
    elif num == "3":
        print(my_empty)
        print(e.name, e.department, e.position, e.rate)


    elif num == "4":
        data = False
        print("Exited")

    else:

        data = True
        print("Invalid Number")
    

    
       
        
       

   
    




