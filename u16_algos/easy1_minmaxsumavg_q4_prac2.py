#################################################################
# Question 4: 
# A bookstore keeps track of their sales figures each day 
# for the month of June. The sales for the 30 days are provided 
# in the list below. 
# 
# Find the days with the highest and lowest sales. 
# Assume that the first item in the list corresponds to Day 1.

# Find the total sales figure for the month.
# 
# Find the average sales rounded to 2 decimal points.

daily_sales = [120, 98, 135, 105, 150, 112, 80, 130, 95, 110, 
               102, 85, 140, 99, 123, 145, 78, 90, 136, 145, 
               132, 108, 75, 88, 142, 115, 97, 121, 89, 100]


# Find the days with the highest and lowest sales. 
# Assume that the first item in the list corresponds to Day 1.

high_sales = daily_sales[0]
low_sales = daily_sales[0]
h_sales_day = 0
l_sales_day = 0

for i in range(len(daily_sales)):
    if daily_sales[i] > high_sales:
        high_sales = daily_sales[i]
        h_sales_day = i + 1
    if daily_sales[i] < low_sales:
        low_sales = daily_sales[i]
        l_sales_day = i + 1

print(f"Day {h_sales_day} has the highest sales and Day {l_sales_day} has the lowest sales.")


# Find the total sales figure for the month.

thesum = sum(daily_sales)

print(f"The total sales figure for the month is ${thesum}.")


# Find the average sales rounded to 2 decimal points.

avg_sales = sum(daily_sales) / len(daily_sales)
formatted_avg = f"{avg_sales:.2f}"

print(f"The average sales for the month of June is ${formatted_avg}.")


