# Vending_Machine
McGill Comp202 A1 - Winter2020

Question 1: Vending Machine (60 points)
For this part of the assignment you will write a program that simulate a virtual vending machine. Your program must retrieve inputs from a user interacting with the vending machine. The purpose of the program is to compute the amount of change to be returned by the machine given the amount of money inserted by the user and the cost of the item they have chosen. Assume that the change will be composed of toonies ($2), loonies ($1), quarters ($0.25), dimes ($0.10), and nickels ($0.05).
Note that, to be considered correct, your program must provide the user with the most convenient exact change (i.e. the exact amount with the fewest coins).
To achieve this, create a file called vending_machine.py. At the beginning of the file create five global variables indicating the amount of coins available in the vending machine. The machine has a total of $25 distributed as follows:
• $10 in toonies • $5 in loonies • $5 in quarters • $3 in dimes
• $2 in nickels
The five global variables must be called with the following names: TOONIES, LOONIES, QUARTERS, DIMES, and NICKELS.
Page 4
For full marks, all the following functions must be part of your program:
• display_welcome_menu: This function takes no input and displays a welcoming message as well as a list with all the options available to the customer. That is,
        >>> display_welcome_menu()
        Welcome to the COMP 202 virtual Vending Machine.
        Here are your options:
        1. Candy bar $2.95
        2. Cookies $3.90
        3. Soda $4.00
        4. Chips $3.90
        5. No snacks for me today!
You can personalize the welcome message, but the options available must be exactly the same as listed above.
• get_snack_price: This function takes an integer and input representing the choice of the customer after seeing the menu. The function returns the price (in cents) associated to the choice made. If the input is not a number between 1 and 4 (both included) then the function returns 0. For example:
        >>> get_snack_price(2)
        390
        >>> get_snack_price(21)
        0
• get_num_of_coins: This function takes three positive integers as input, the first indicating the amount of money needed (in cents), the second indicating the value of a coin (in cents), and the third indicating the number of coins of the given value available in the machine. The function returns the maximum number of coins of the given value that can be used to work toward achieving the target amount. For example:
        >>> get_num_of_coins(1000, 100, 8)
        8
        >>> get_num_of_coins(550, 200, 4)
        2
        >>> get_num_of_coins(234, 30, 20)
        7
• compute_and_display_change: This function takes as input one non-negative integer representing the change (in cents) that the vending machine should give back to the customer. Using the coins available in the machine, the method computes the most convenient exact change. If the machine has enough coins to make the change, then the function displays the corresponding information on the screen and returns True. Otherwise, the function must not display anything and returns False. For example:
        >>> b = compute_and_display_change(185)
        Here is your change:
         toonies x 0
         loonies x 1
         quarters x 3
         dimes x 1
         nickels x 0
>>> b True
Page 5

      >>> b = compute_and_display_change(40)
      Here is your change:
       toonies x 0
       loonies x 0
       quarters x 1
       dimes x 1
       nickels x 1
>>> b True
      >>> b = compute_and_display_change(590)
      Here is your change:
       toonies x 2
       loonies x 1
       quarters x 3
       dimes x 1
       nickels x 1
>>> b True
      >>> b = compute_and_display_change(2600)
      >>> b
      False
      >>> b = compute_and_display_change(123)
      >>> b
      False
• operate_machine: This function takes no inputs and returns no value. The function performs the following tasks in this following order:
– It displays the menu of the vending machine
– It retrieves an integer from the user indicating their choice
– If no snack item was chosen, then it displays a goodbye message and terminate its execution. Otherwise, it displays the price (in cents) of the chosen item and continues to the next step.
– It retrieves the cash (in dollars) provided by the user.
– It rounds the amount provided by the user to two decimals and displays it (in cents).
– If the amount provided if not a multiple of 5 then it displays a message indicating that no pennies are accepted and terminates its execution.
– If the amount provided is not enough to cover the price of the snack, then it displays a messages indicating that the cash is not enough and terminates its execution.
– It displays the change (in cents) that the user should expect from the machine
– It computes and displays the change to be provided. If it was not possible to provide the change needed, it displays a message indicating that the machine does not have enough coins. Otherwise, it displays a message indicating the order was successfully processed.
As long as you maintain the correct meaning, you are free to personalize the messages displayed by your vending machine. Below you can find a couple of examples of interactions with the vending machine. Note that the inputs provided from the user appear in a different font and in blue.
Page 6

>>> operate_machine()
Welcome to the COMP 202 virtual Vending Machine.
Here are your options:
1. Candy bar $2.95
2. Cookies $3.90
3. Soda $4.00
4. Chips $3.90
5. No snacks for me today!
Please select your choice: 5
Nothing for you today. Thank you for stopping by!
>>> operate_machine()
Welcome to the COMP 202 virtual Vending Machine.
Here are your options:
1. Candy bar $2.95
2. Cookies $3.90
3. Soda $4.00
4. Chips $3.90
5. No snacks for me today!
Please select your choice: 2
The item of your choice costs 390 cents
Enter your money: $3.45555 You inserted 346 cents
We do not accept pennies. Come by another time!
>>> operate_machine()
Welcome to the COMP 202 virtual Vending Machine.
Here are your options:
1. Candy bar $2.95
2. Cookies $3.90
3. Soda $4.00
4. Chips $3.90
5. No snacks for me today!
Please select your choice: 2
The item of your choice costs 390 cents
Enter your money: $3.4999999 You inserted 350 cents
You do not have enough money. Come by another time!
Page 7

>>> operate_machine()
        Welcome to the COMP 202 virtual Vending Machine.
        Here are your options:
        1. Candy bar $2.95
        2. Cookies $3.90
        3. Soda $4.00
        4. Chips $3.90
        5. No snacks for me today!
Please select your choice: 2
The item of your choice costs 390 cents
Enter your money: $7.55 You inserted 755 cents
        You should receive back 365 cents
        Here is your change:
         toonies x 1
         loonies x 1
         quarters x 2
         dimes x 1
         nickels x 1
        It was a pleasure doing business with you!
        >>> operate_machine()
        Welcome to the COMP 202 virtual Vending Machine.
        Here are your options:
        1. Candy bar $2.95
        2. Cookies $3.90
        3. Soda $4.00
        4. Chips $3.90
        5. No snacks for me today!
Please select your choice: 2
The item of your choice costs 390 cents
Enter your money: $29.80 You inserted 2980 cents
        You should receive back 2590 cents
        The machine does not have enough coins for your change. Come by another time!
For full credit you should never be repeating code, but rather calling helper functions! You are welcome to add additional functions if you think this can increase the readability of your code.
Page 8
