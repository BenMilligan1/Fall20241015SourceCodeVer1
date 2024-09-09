#Student Name:Ben Milligan    
#Program Title: Basic input output
#Description: This program is printing out to the console different messages   

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    # Input

    '''
    In the following lines, we are hardcoding the two variables.
    It means that, I am adding the input values for those two variables inside the editor, not getting them from the terminal
    '''

    firstName = "Ben" #This a variable to get the student name
    lastName = " Milligan" #This is a variable to get the student name

    # Processing
    studentName = firstName + lastName # It is a concatenation process

    # Output 
    print("New basic input output Program")
    print ("Welcome to our new program")
    print ("The student's name is: \t" + studentName)

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()