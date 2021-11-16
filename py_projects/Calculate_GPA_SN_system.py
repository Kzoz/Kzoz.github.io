# program to calculate your grades in Senegal



from tabulate import tabulate
# this library allows table creation from a list (with captions) 

# Get the number of subjects the student is taking
def get_num_sub():
    numb = input(" Combien de matières?: ")
    return(numb)
numb = int(get_num_sub())


def input_sub_grad(numb):
    #Get the name, mark, coef of each subject and add them all to **list_of_coef**
    # Use *list_of marks* to calculate the average which is (grade(s) * coef(s))/total coef

    list_of_marks = [] #**
    list_of_coef = [] #*
    total_coef = 0
    for i in range(numb):
        subject_name = input("Quelle est la " + str(i+1) +"e matière?: ")
        subj = input("Note en " + subject_name+ " ")
        coef = input("Coefficient de "+ subject_name+ " ")
        total_coef += int(coef)
        list_of_coef.extend([[subject_name, subj, coef]])
        list_of_marks.append(int(subj) * int(coef))
    list_of_marks = sum(list_of_marks)/total_coef
    return(list_of_coef,list_of_marks) 
mon_bulletin = input_sub_grad(numb)


# Print out a board of all the grades to allow the student to visualize his inputs
# Print The GPA

tableau = mon_bulletin[0]
print(tabulate(tableau, headers=['Matière', 'Note','Coefficent']))
print("Ta moyenne générale est de: ","{:.2f}".format(mon_bulletin[-1]))