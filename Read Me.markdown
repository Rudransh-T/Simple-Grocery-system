🛒 Simple Grocery Billing System

## Introduction

This is a simple project made in Python for a basic grocery billing

system. The program takes the items purchased by the user along with
their quantities, allows to add or remove items, use coupons and

calculates the total bill. The project is primarily focused on
practicing basic Python concepts and understanding of how they can be
used in a trivial real-life like application. \## What the Program Can
Do The program has following core features: - Display available grocery
items and their prices - Take the purchased items from the user - Take
the quantity of each item - Add items - Remove items - Coupon codes
specific to an item - Generate coupon code upon a valid 10-digit phone
number - Accept general discount coupons - Add 5% tax to the total
bill - Display the final list of items purchased along with their
quantities \## Grocery Items and Prices Currently the program utilizes
the following items: No.Item Price ----- ------------ ------- 1 Bread
₹20 2 Butter ₹50 3 Cheese ₹80 4 Chicken ₹300 5 Chips ₹10 6 Candy ₹5 7
Toothpaste ₹40 8 Kurkure ₹20 \## Entering Purchased Items First, the
user has to enter the names of the items that they want to purchase. For
example:

``` text
bread butter cheese
```

These item names will be temporarily stored in a NumPy array. After
that, the user has to enter the quantities of each item. For example:

``` text
2 1 3
```


## Item-Specific Coupons

The program also contains some item specific coupon codes. Coupon Code
Intended Use ------------------ -------------- `riseup` Butter
`clockadoodledo` Chicken `smoothlike` Cheese These coupons are meant to
reduce the price of the related item. \## Calculating the Item Price The
basic calculation used for an item is:

``` text
Item Price × Quantity
```

For example, if the quantity of bread is 2:

``` text
₹20 × 2 = ₹40
```

The cost of the purchased items is then summed together to get the total
before the final tax calculation. \## Phone Number Coupon The program
asks the user for a phone number:

``` text
TO GET COUPON ENTER YOUR PHONE NUMBER
```

If the entered value has exactly 10 characters, the program displays the
coupon:

``` text
MONEYHEIST
```

Otherwise, it displays a message that no coupon is available. \##
General Coupon Codes The program also accepts these general coupon
codes: Coupon Code Discount -------------- ---------- `money` 30%
`moneyheist` 20% `father` 40% The user can enter the coupon code at the
end of the purchase process. \## Tax Calculation After calculating the
total, the program adds 5% tax. The calculation is:

``` text
Grand Total = Total Price + 5% Tax
```

The code used for this is:

``` python
a1 = a 0.05 + a
```

## Final Bill

At the end, the program prints the purchased items along with their
quantities. After which it displays:

``` text
The Total price before tax
The Grand Total
```

Finally, a thank-you message is displayed for the purchase. \##
Requirements To run this project, you will need: - Python 3.x - NumPy
NumPy can be installed with:

``` bash
pip install numpy
```

## How to Run the Program

1.  Save the Python code in a file named:

``` text
grocery_system.py
```

2.  Open Command Prompt or a terminal in the same directory.
3.  Run the program using:

``` bash
python grocery_system.py
```

4.  Enter the information whenever the program asks for it. \## Example
    Input For example, the user can enter:

``` text
bread butter cheese
```

For quantities:

``` text
2 1 1
```

## Project Structure

The project can be kept simple with these two files:

``` text
Grocery-Billing-System/
│
├── grocery_system.py
└── README.md
```

## Python Concepts Used

This project utilizes a number of basic Python concepts. \### NumPy
Arrays The entered items and quantities are stored in arrays:

``` python
l1 = array(p.split(), str)
l2 = array(q.split(), int)
```

### Taking Input

The `input()` function is used to take information from the user:

``` python
p = input()
```

### If-Else Statements

The program uses conditions to make decisions. For example:

``` python
if add.lower() == "yes":
...
```

### For Loops

Loops are used to iterate on the items:

``` python
for m in l1:
...
```

### Converting Arrays to Lists

When adding or removing items, the arrays are converted to lists:

``` python
l1 = l1.tolist()
l2 = l2.tolist()
```

## Important Points About the Current Code

The supplied program has a few issues in the code that should be
addressed if the program is to be used as a proper billing system. For
example, the code currently contains:

``` python
if m.lower == 'bread':
```

Here, `lower` is being referenced but not called. It should be:

``` python
if m.lower() == 'bread':
```

The same issue appears for the coupon checks. For example:

``` python
if k.lower == 'riseup':
```

should be:

``` python
if k.lower() == 'riseup':
```

One more thing to keep in mind is the use of `list` as a variable name:

``` python
list = (...)
```

`list` is already a built-in Python function. It would be better to use
something like:

``` python
item_list = (...)
```

to avoid issues when the `list()` function is needed. 
### Ideas for Improving the Project
The project can be improved upon by adding features such as: - Better input 
checking - Price auto selection - Stock/available-quantity management - Proper 
receipt printing - GST/tax details - More coupon options - Coupon expiry - Different
payment options - GUI - Saving the bill - Separate functions for adding,
removing, calculating and coupons 
### Learning Purpose
This project is useful for beginners who are learning Python, especially for basic BTech
CSE programming practice. It brings together simple concepts such as
arrays, lists, loops, conditions, strings, user input and arithmetic
calculations in one small project.
### License
This project is made for educational and learning purposes.
