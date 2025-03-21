def calculate_discount(price, discount_percentage):
    #price=price-(price*discount_percentage/100)
    if discount_percentage>=20:
       return price-(price*discount_percentage/100)
    else:
        return price

try:
    original_price=float(input("Enter the original price:"))#allow user input of original price
    discount_percentage=float(input("Enter the discount percentage:"))
    
    final_price = calculate_discount(original_price, discount_percentage)
    
    print(f"The final price after discount is: ksh{final_price:.2f}")#print the final price after discount
except ValueError:
    print("Please enter valid numbers only.")