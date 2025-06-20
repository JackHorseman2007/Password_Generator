import random #Imports the random module so that random characters can be selected for the password

print("Welcome to the password generator!") #Outputs a welcome message to the user

password_use = input("What website/application is this password for?") #Asks the user what the password is for, so that it can be saved with the password 

length = int(input("Enter desired length of password:")) #Asks the user how long they want the password to be, and converts it to an integer

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%^&*()_+-=[]{}#:@;',.<>?/~`" #Defines all of the characters that can be used in the passwords
password = ''.join(random.choice(characters)for i in range(length)) #Generates a random password by selecting characters from the defined string, based on the desired length
print("Your password is:",password) #Outputs the generated password to the user

save = input("Do you want to save this password? (y/n):").lower().strip() #Asks the user if they want to save the password, and converts the input to lowercase and removes any whitespaces before or after the input
while save != 'y' and save != 'n': #Checks if the input is not 'y' or 'n'
     save = input("Please enter 'y' or 'n':").lower().strip() #If the input is not 'y' or 'n', it will keep asking until a valid input is given
if save == 'y': #If the user wants to save the password
        file_decision = input("Do you want to save this password in a new file or an existing file? (new/existing):").lower().strip() #Asks the user if they want to save the password in a new file or an existing file, and converts the input to lowercase and removes any whitespaces before or after the input
        while file_decision != 'existing' and file_decision != 'new': #Checks if the input is not 'existing' or 'new'
            file_decision = input("Please enter 'new' or 'existing':").lower().strip() #If the input is not 'existing' or 'new', it will keep asking until a valid input is given
        if file_decision == 'existing': #If the user wants to save the password in an existing file
            filename = input("What is the name of the existing file?") #Asks the user for the name of the existing file
            filepath = filename + ".txt" #Defines the file path by adding .txt to the filename
            mode = "a" #Sets the mode to append, so that the new password can be added to the existing file without overwriting it
        else: #If the user wants to save the password in a new file
            filename = input("What do you want to name the file?") #Asks the user for the name of the new file
            filepath = filename + ".txt" #Defines the file path by adding .txt to the filename
            mode = "w" #Sets the mode to write, so that a new file can be created with the new password
        with open(filepath, mode) as file: #Opens the file in the defined mode
            file.write(f"{password_use}: {password}\n") #Writes the website/application and the password to the file}
else: #If the user does not want to save the password
     print("Password not saved. You better remember it!") #Outputs an exit message to the user

again = input("Do you want to generate another password? (y/n):").lower().strip() #Asks the user if they want to generate another password, and converts the input to lowercase and removes any whitespaces before or after the input
while again != 'y' and again != 'n': #Checks if the input is not 'y' or 'n'
    again = input("Please enter 'y' or 'n':").lower().strip() #If the input is not 'y' or 'n', it will keep asking until a valid input is given
if again == 'y': #If the user wants to generate another password
    exec(open("password_generator.py").read()) #Executes the password generator script again
else: #If the user does not want to generate another password
    print("Thank you for using the password generator!") #Outputs a thank you message to the user