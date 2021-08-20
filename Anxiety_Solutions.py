import webbrowser
import random
from pyfiglet import figlet_format
from colorama import init, Fore, Back, Style
init(autoreset=True)

# Url
url1 = 'https://www.nhs.uk/mental-health/nhs-voluntary-charity-services/charity-and-voluntary-services/get-help-from-mental-health-helplines/'
url2 = 'https://youtu.be/qvaB2d5yDf8'
url3 = 'https://www.netflix.com/gb/'
url4 = 'https://www.xbox.com/en-gb/xbox-game-pass?&ef_id=CjwKCAjwieuGBhAsEiwA1Ly_nQfpzvGpRa7OrEMI_9Sd4PKfkCoQ288KdiIqLryOM-TmdxH2JjIllxoCZ54QAvD_BwE:G:s&OCID=AID2100895_SEM_CjwKCAjwieuGBhAsEiwA1Ly_nQfpzvGpRa7OrEMI_9Sd4PKfkCoQ288KdiIqLryOM-TmdxH2JjIllxoCZ54QAvD_BwE:G:s&gclid=CjwKCAjwieuGBhAsEiwA1Ly_nQfpzvGpRa7OrEMI_9Sd4PKfkCoQ288KdiIqLryOM-TmdxH2JjIllxoCZ54QAvD_BwE'
url5 = 'https://www.nhs.uk/live-well/exercise/'
Nhs = 'https://www.nhs.uk/mental-health/nhs-voluntary-charity-services/charity-and-voluntary-services/get-help-from-mental-health-helplines/'

# Functions
def random_solution():
    solutions_list = [tv, game, exercise]
    random.choice(solutions_list)
    
def focus_present():
    print ('Remeber to focus in the present to get rid of anxiety')
    
    
def more_info():
    ans = None
    while ans != 'y' and ans != 'n':
                    ans = input('Do you want more information on getting rid of anxiety? (y/n)').lower()
                    if ans:
                        if ans == 'y':
                            webbrowser.open_new_tab(url2)
                        elif ans == 'n':
                            focus_present   

def tv():
    answer1 = None 
    while answer1 != 'y' and answer1 != 'n':
        answer1 = input(f"Do you want to watch tv (y/n)").lower() 
        if answer1:
            if answer1 == 'n':
                random_solution
                more_info
            elif answer1 == 'y':
                webbrowser.open_new_tab(url3)
            elif answer1 == 'n':
                random_solution
                more_info
            elif answer1 != 'y':
                print('Please enter y or n')
            elif answer1 != 'n':
                print('Please enter y or n')
            else: print('Please enter y or n')   
                                   
def game():
    answer1 = None 
    while answer1 != 'y' and answer1 != 'n':
        answer1 = input(f"Do you want to play video games? (y/n)").lower() 
        if answer1:
            if answer1 == 'n':
                random_solution
                more_info
            elif answer1 == 'y':
                webbrowser.open_new_tab(url4)
            elif answer1 == 'n':
                random_solution
                more_info
            elif answer1 != 'y':
                print('Please enter y or n')           
            elif answer1 != 'n':
                print('Please enter y or n')        
            else: print('Please enter y or n')  
            
def exercise():
    answer1 = None 
    while answer1 != 'y' and answer1 != 'n':
        answer1 = input(f"Do you want to find some exercises you can do? (y/n)").lower() 
        if answer1:
            if answer1 == 'n':
                random_solution
                more_info
            elif answer1 == 'y':
                webbrowser.open_new_tab(url5)
            elif answer1 == 'n':
                random_solution
                more_info
            elif answer1 != 'y':
                print('Please enter y or n')           
            elif answer1 != 'n':
                print('Please enter y or n')        
            else: print('Please enter y or n')    
                     
msg = 'Anxiety Solutions' 
ascii_art = figlet_format(msg)

# Print statements 
print(f"{Fore.LIGHTGREEN_EX}{ascii_art}")
print(f"Disclaimer this is NOT medical advise, if you suffering from mental health and you need help contact {Nhs}...\n")  
print("Anxiety is the uncertanty of 'the unkown'. What could happen in the future...?\n")
print('There are two ways to get rid of anxiety. Focusing in the present and dealing with unknown, this will help you get rid of anxiety\n')
print ('The best way to figth anxiety is by facing the issues that makes you anxious, this way you grown confident if your ability to face uncertnaty\n')
print('Following there are a few ways of focusing in the present to help you alleviate your anxiety\n')

# Function
def find_anxiety():
    anxiety_cause = ['job interview', 'exams', 'medical test', 'social anxiety']
    guess = None
    while guess != anxiety_cause:
        guess = input(f"Is {random.choice(anxiety_cause)} the cause of your anxiety? (y/n)").lower()
        if guess == 'y':
            print('Remeber to focus in the present to get rid of anxiety')
            return random_solution
        elif guess == 'n':
             guess = input(f"Is {random.choice(anxiety_cause)} the cause of your anxiety? (y/n)").lower()
        elif guess != 'y':
            print('Please enter y or n')
        elif guess != 'n':
            print('Please enter y or n')                     
        else: print('Please enter y or n')      

# Calling functions
find_anxiety()
tv()
game()
exercise() 
more_info()      



    


    
    



    
    
    
    
 










    


    
    



    
    
    
    
 








