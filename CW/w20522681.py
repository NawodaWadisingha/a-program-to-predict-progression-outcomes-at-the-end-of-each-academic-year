# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20222153(IIT) / W20522681(UOW)
# Date: 22/11/2023

from graphics import *
import datetime

#Creating and initializing variables
progress_count = 0
trailer_count = 0
exclude_count = 0
retriever_count = 0
record_data = []

#Getting user inputs for credits at pass, defer and fail.
def getting_credits():
    while True: 
        while True:
            while True:
                try:
                    pass_credit = input("Please enter your credits at pass: ")
                    pass_credit = int(pass_credit)
                    break
                except KeyboardInterrupt:
                    print("Invalid input.\nTry again.\n")
                except:
                    print("Integer required.\n")
            if pass_credit in range(0,140,20):
                break
            else:
                print("Out of range.\n")

        while True:
            while True:
                try:
                    defer_credit = input("Please enter your credit at defer: ")
                    defer_credit = int(defer_credit)
                    break
                except KeyboardInterrupt:
                    print("Invalid input.\nTry again.\n")
                except:
                    print("Integer required\n")
            if defer_credit in range(0,140,20):
                break
            else:
                print("Out of range.\n") 

        while True:
            while True:
                try:
                    fail_credit = input("Please enter your credit at fail: ")
                    fail_credit = int(fail_credit)
                    break
                except KeyboardInterrupt:
                    print("Invalid input.\nTry again.\n")
                except:
                    print("Integer required\n")
            if fail_credit in range(0,140,20):
                break
            else:
                print("Out of range.\n")

        total_credits = pass_credit + defer_credit + fail_credit
        if total_credits == 120:
                break
        else:
            print("Total incorrect.\n")
    return(pass_credit,defer_credit,fail_credit)

#This user defined function display the appropriate progression outcome
def checking_progression(pass_credit,fail_credit,defer_credit):
    global progress_count
    global trailer_count
    global exclude_count
    global retriever_count

    if pass_credit == 120:
        print("Progress")
        grade = "Progress"
        progress_count += 1

    elif pass_credit == 100:
        print("Progress (module trailer)")
        grade = "Progress (module trailer)"
        trailer_count +=1

    elif fail_credit >= 80:
        print("Exclude")
        grade = "Exclude"
        exclude_count += 1

    else:
        print("Do not progress – module retriever")
        grade= "Do not progress – module retriever"
        retriever_count += 1
    record = f"{grade} - {pass_credit}, {defer_credit}, {fail_credit}"  #https://docs.python.org/3/tutorial/inputoutput.html
    record_data.append(record)

#Produce a ‘histogram’ representing the number of students who achieved a progress outcome in each category range
def creating_histogram():
    grades_counts = [progress_count,trailer_count,retriever_count,exclude_count]
    total_grades = progress_count + trailer_count + retriever_count + exclude_count
    bar_names = ["Progress","Trailer","Retriever","Excluded"]
    bar_colours = ["palegreen","darkseagreen","darkkhaki","lightcoral"]
    presentage_of_grades = [0,0,0,0]
    win = GraphWin("Histogram", 500, 450)
    win. setBackground("white")
    height = 200
    title = Text(Point(100,30),"Histogram Results")
    title.setSize(13)
    title.draw(win)
    bar_line =Line(Point(15,win.getHeight() - 79),Point(win.getWidth() - 15,win.getHeight() - 79))
    bar_line.draw(win)

    i = 0
    for value in grades_counts:
        presentage_of_grades[i] = value/total_grades
        i += 1

    i = 0
    for value in grades_counts:
        TLCR_x = 20+(i * 120)                     #TLCR = Top Left Corner Rectangle
        TLCR_y =win.getHeight() - 80              #BRCR = Bottom Right Corner Rectangle
        BRCR_x = (20+(i * 120)) + 100
        BRCR_y = (370 - presentage_of_grades[i]*height)
        bar = Rectangle(Point(TLCR_x,TLCR_y),Point(BRCR_x,BRCR_y))
        bar.setFill(bar_colours[i])
        bar.draw(win)
        bar_names_text = Text(Point(((20+(i * 120))+50),390),bar_names[i])
        bar_names_text.setSize(10)
        bar_names_text.draw(win)
        total_grades_text_format = f"{total_grades} outcomes in total"
        total_grades_text = Text(Point(200,420),total_grades_text_format)
        total_grades_text.draw(win)
        num_of_grade_text = Text(Point(((20+(i * 120))+50),BRCR_y-10),grades_counts[i])
        num_of_grade_text.draw(win)
        i += 1

    win.getMouse()  
    win.close() 

#Part 2 – List (extension)
def print_results():
    for i in record_data:
        print(i)
  
#Part 3 - Text File (extension)
def generate_text_file():
    current_datetime = datetime.datetime.now()     #https://www.geeksforgeeks.org/get-current-date-and-time-using-python/
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")   #https://www.w3schools.com/python/python_datetime.asp
    file_name = f"output_{formatted_datetime}.txt"    

    with open (file_name,"w") as file:
        for i in record_data:
            rec = str(i)
            file.write(rec + "\n")
    #print(f"Data written to {file_name}")

#Run the main program and getting progression outcomes for multiple students.
while True:
    try:
        user_role = input("Are you a student or a staff member?\nEnter 'student' or 'staff': ")
        print()
        if user_role.lower() == 'student':
            Student_credits = getting_credits()
            checking_progression(Student_credits[0],Student_credits[2],Student_credits[1])
            break  
        elif user_role.lower() == 'staff':
            while True:
                Student_credits = getting_credits()
                checking_progression(Student_credits[0],Student_credits[2],Student_credits[1])
                while True:
                    user_response = input("\nWould you like to enter another set of grades_counts?\nEnter 'y' for yes or 'q' to quit and view result: ").lower()
                    print()
                    if user_response in ["y", "q"]:
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'q'.")
                if user_response == "q":
                    break
            generate_text_file()
            creating_histogram()
            print_results()
            break  
    except KeyboardInterrupt:
        print("Invalid input.\nTry again.\n")
    except:
        print("Invalid input.\nTry again.\n")