#Build a new class that takes user info we will compute for BMI, BMR and optimal calorie intake
#Name ain't really needed
class Bodybuilding:
    def __init__(self, xname, xage, xsex, xweight, xheight, l_activity, xobjectives):#,#xbmi = 0, xbmr=0, xdi=0,xoi=0) :
        self.name = xname
        self.age = xage
        self.sex = xsex
        self.weight = xweight
        self.height = xheight
        self.activity = l_activity
        self.objectives = xobjectives

#calculate BMI with this formula #Calculation: [weight (kg) / height (cm) / height (cm)] x 10,000
    def bmi(self):
        mybmi = self.weight/self.height/self.height*10000
        return round(mybmi,2)

#Calculate BMR with BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years)
    def bmr(self):
        if self.sex == "male":
            mybmr = 88.362+(13.397 * self.weight)+(4.799*self.height)-(5.677*self.age)
        #BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) – (4.330 x age in years)
        elif self.sex == "female":
            mybmr = 447.593+(9.247 * self.weight)+(3.098*self.height)-(4.330*self.age)
        return round(mybmr,2)

#Calculate the daily calorie intake using user's level of activity
    def cal_intake(self):
        if self.activity == "low"or self.activity == 1:
            daily_intk = self.bmr()*1.2
        elif self.activity == "moderate" or self.activity == 2:
            daily_intk = self.bmr()*1.375
        elif self.activity == "high" or self.activity == 3:
            daily_intk = self.bmr()*1.5
        return round(daily_intk,2)
        
    
#Calculate the optimal calorie intake considering user's goals
    def opt_intake(self):
        if self.objectives == "maintenance":# and level of acivity
            optimal_amount = self.cal_intake()*1.02
        elif self.objectives == "cutting":
            optimal_amount = self.cal_intake()*0.91
        elif self.objectives == "bulking":
            optimal_amount = self.cal_intake()*1.16
        return round(optimal_amount,2)

#Printing out the result if every section was correctly logged    
    def __repr__(self) -> str:
        if self.name == "":
            self.name = "Customer"
        result = "Dear {name}, for a body weight of {weight} and a height of {height}m, your BMi is {bmi}.\n Considering your level of activity, your BMR at {bmr} your daily caloric need is {daily}. For {objective}, you should aim around {optimal} calories per day.\
                ".format(name = self.name, weight = self.weight, height=self.height, bmi = self.bmi(),\
                    bmr = self.bmr(), daily = self.cal_intake(), objective = self.objectives, optimal = self.opt_intake())
        return result

#Define a function that checks user input errors. This function is used for gender, level of activity and objectives inputs
#Since long words are involved, highly are chances for typo
# For each section, there is a margin of #3# errors (error_count). Once reached, NameError will raise
def checkError(err,condition,rep1,rep2,rep3="***"):
    for x in range(err):
        i=input(condition).lower()
        if i != rep1 and i != rep2 and i !=rep3:
            print("Your input was",i)
            print("Incorrect input. Try again!")
            err -=1
        else:
            return i
    if err <= 0:
            raise NameError("Too many errors!")

#userdt() func allows user to input data while answering to questions
# user inputs are passed to Bodybuilding class and then results are printed out with the last line.
def userdt():
    error_count = 3
    name = input("Enter your name: ").lower()
    age = input("What is your age? ")
    genre,male,female = "Male or Female: ","male","female"
    sex = checkError(error_count,genre,male,female)
    weight = input("What is your weight in kg? ")
    height = input("What is your height in centimeter? ")
    level, x1,x2,x3="How active are you? low, moderate or high? ","low","moderate","high"
    activity = checkError(error_count,level,x1,x2,x3)
    vision,y1,y2,y3 = "Are you maintaining? cutting? or bulking? ","maintaining","cutting","bulking"
    objectives = checkError(error_count,vision,y1,y2,y3)
    #********************************************************************************
     
    user_info = Bodybuilding(name,int(age), sex, float(weight), float(height), activity, objectives)
    return user_info

userdt()

#Improve the program with better precision calculation
#Potentially make a webpage of it 