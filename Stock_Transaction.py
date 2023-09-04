print(f"***** Welcome to the stock profit calculator *****\n" )
stock_commission_bought = float(input("Enter the commission for the bought shares: "))
number_of_shares_purchased = int(input("Enter the number of shares purchased: "))
share_price =  float(input("Enter the buy price per share: "))
stock_commission_sold = float(input("Enter the commission percentage for the sold shares: "))
number_of_shares_sold = int(input("Enter the number of shares sold: "))
share_sold = float(input("Enter the sell price per share: "))


price_paid = number_of_shares_purchased * share_price
commission_bought = stock_commission_bought / 100
commission_bought_total = price_paid * commission_bought
price_paid = number_of_shares_purchased * share_price + commission_bought_total


price_sold = number_of_shares_sold * share_sold
commission_sold = stock_commission_sold / 100
commission_sold_total = price_sold * commission_sold
price_sold = number_of_shares_sold * share_sold + commission_sold_total


total_paid = price_paid + commission_bought_total
total_sold = price_sold + commission_sold_total


profit = total_sold - total_paid


print(f"Commission paid: ${commission_bought_total:,.2f}\n")
print(f"Price paid: ${price_paid:,.2f}\n")
print(f"Commission paid: ${commission_sold_total:,.2f}\n")
print(f"Sell amount: ${price_sold:,.2f}\n")


if profit < 1:
    print(f"Your loss is ${profit:,.2f}")
else:
    print(f"Your profit is: ${profit:,.2f}")