#Jeremy Smith - 260948914

#declarining variables, represents the number coins in stock in the vending machine for each denomination
TOONIES = 5 #$10 = 5 toonies
LOONIES = 5 #$5 = 5 loonies
QUARTERS = 20 #$5 = 20 quarters (5/1=20/4)
DIMES = 30 #$3 = 30 dimes (3/1=30/10)
NICKELS = 40 #$2 = 40 nickels (2/1=40/20)

def display_welcome_menu(): #defining the display menu to save time if I must call on it more than once 
    print("Welcome to the COMP 202 vending machine menu\nHere are your options:\n1. Candy bar $2.95\n2. Cookies $3.90\n3. Soda $4.00\n4. Chips $3.90\n5. No snacks for me today")
    
def get_snack_price(choice): #defining a function to determine the cost in cents of the desired snack
    #choice is received by user under the operate machine function when get_snack_price is called on
    """
    (int)->str+int
    Returns the cost in cents associated with the user's selction (choice)
    >>get_snack_price(1)
    "This item costs 295 cents"
    295
    >>get_snack_price(7)
    0
    >>get_snack_price(4)
    "This item costs 390 cents"
    390
    """
    if choice == 1:
        print("This item costs ",295," cents") #shows the user the message
        return 295 #the actual value being returned from the function to be used elsewhjere when needed
    elif choice == 2: #using else if statements because there are more options than simply true or false
        print("This item costs ",390," cents")
        return 390
    elif choice == 3:
        print("This item costs ",400," cents")
        return 400
    elif choice == 4:
        print ("This item costs ",390," cents")
        return 390
    elif choice == 5:
        print("Goodbye!")
        return 0
    elif choice < 1:
        return 0
    else: #if the choice is an integer > 5, a float, a char or a string 0 will be returned
        return 0

def get_num_of_coins(money_needed, coin_value, coin_availability):
    """
    (int,int,int)->int
    Returns the maximum amount of coins of a certain denomination when giving change back to the customer
    >>>get_num_of_coins(500, 100, 20)
    5
    >>>get_num_of_coins(120, 25, 1)
    1
    >>>get_num_of_coins(800, 10, 100)
    80
    """
    num_of_coins = int(money_needed/coin_value) #determines the number of coins of a certain value to be returned
    if (num_of_coins<coin_availability): #when the amount of coins needed to be returned exceeds the amount in stock we return all of the highest denomination in stock and if more is still needed lower coins will be used
        return num_of_coins
    else:
        return coin_availability

def compute_and_display_change(change_to_give):#uses the change due to the user as input
    """
    (int)->string, bool
    Returns a string indicating the amount of change returned at the way it is broken up and True
    or False if the amount of change cannot be broken up into the available denominations
   
    >>>compute_and_display_change(150)
    
    Here is your change:
    toonies x  0
    loonies x  1 
    quarters x  2 
    dimes x   0
    nickels x  0
    
    True
    
    >>>compute_and_display_change(467)
    
    False
    
    >>>compute_and_display_change(5)
    
    Here is your change:
    toonies x  0
    loonies x  0 
    quarters x  0 
    dimes x   0
    nickels x  1
    
    True
    
    """
    toonies_returned = get_num_of_coins(change_to_give, 200, TOONIES) #the amount of coins of a certain value being returned is determined by the get_num_of_coins function
    #change_to_give is used initially because it is the initial amount of change due to the user
    #TOONIES is the initial stock of toonies stored in the machine
    remaining_change = change_to_give - toonies_returned*200
    #remaining_change is the amount of money still owed to the user after the last denomination(s) of coin was returned
    loonies_returned = get_num_of_coins(remaining_change,100,LOONIES)
    #remaining_change is used not change_to_give because it is the updated amount
    #the variable change_to_give is not altered to allow the user to go back and see the initial amount of change due at any time
    remaining_change = remaining_change - loonies_returned*100
    quarters_returned = get_num_of_coins(remaining_change,25,QUARTERS)
    remaining_change = remaining_change - quarters_returned*25
    dimes_returned = get_num_of_coins(remaining_change,10,DIMES)
    remaining_change = remaining_change - dimes_returned*10
    nickels_returned = get_num_of_coins(remaining_change,5,NICKELS)
    remaining_change = remaining_change - nickels_returned*5
    if (remaining_change > 0):
        return False
    elif (remaining_change < 0):
        return False
    else:
        print ("\nYou should receive back ",change_to_give," cents")
        print ("\nHere is your change:")
        print ("toonies x ", toonies_returned, "\nloonies x ", loonies_returned, "\nquarters x ", quarters_returned, "\ndimes x ",dimes_returned,"\nnickels x ",nickels_returned)
        return True
    #previous line shows the user how their change is being split up and given to them
    #the amount of coins will always be optimized since the first priority is always to maximize toonies then loonies then quarters and so on
    
def operate_machine(): #the fuction that includes everything being used
    """
    >>>operate_machine()
    
    Welcome to the COMP 202 vending machine menu
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today

    What would you like? Please enter the corresponding integer for the snack you would like. 3
    This item costs  400  cents

    Enter the amount of money being entered in dollars: $7

    You inserted  700  cents

    You should receive back  300  cents

    Here is your change:
    toonies x  1 
    loonies x  1 
    quarters x  0 
    dimes x  0 
    nickels x  0
    
    >>>operate_machine()
    
    Welcome to the COMP 202 vending machine menu
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today

    What would you like? Please enter the corresponding integer for the snack you would like. 4
    This item costs  390  cents

    Enter the amount of money being entered in dollars: $4

    You inserted  400  cents

    You should receive back  10  cents

    Here is your change:
    toonies x  0 
    loonies x  0 
    quarters x  0 
    dimes x  1 
    nickels x  0
    
    >>>operate_machine()
    
    Welcome to the COMP 202 vending machine menu
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today

    What would you like? Please enter the corresponding integer for the snack you would like. 5
    Goodbye!
    """
    display_welcome_menu() #calls on the display menu to show the options to the user
    snack_cost = get_snack_price(int(input("\nWhat would you like? Please enter the corresponding integer for the snack you would like. ")))
    #shows the input message and assigns the return value to a variable that will be used 
    dollars_entered = float(input("\nEnter the amount of money being entered in dollars: $"))
    #gets the input from the user in dollars - is a float since dollars may have decimals
    cents_entered = int(round(dollars_entered,2)*100)
    if (cents_entered < snack_cost):
        print("Sorry you did not enter enough money, come again :)")
    #rounds dollars to two decimal points and then converts to cents and to an integer
    print ("\nYou inserted ",cents_entered," cents") #tells the user how manby cents they have entered
    if (cents_entered %5 != 0): #assures that the machine only accepts multiples of 5cents as the smallest value coin offered is a nickel
        print ("We do not accept pennies. Come another time!")
    compute_and_display_change(cents_entered - snack_cost) #runs the function to determine what is owed to the user and how it will be split up
    
operate_machine()
#runs the vending machine program
#end of prog