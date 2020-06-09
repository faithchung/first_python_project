import csv
# reading one month
def read_data(month):
    data = []
    with open('Sales_{}_2019.csv'.format(month), 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            if (row['Quantity Ordered'] != '') and (row['Quantity Ordered'] != 'Quantity Ordered'): # cleaning data
                data.append(row)
    return data
# one big dictionary called 'Database' that stores 12 different keys (months) i.e. 'January', 'February' etc
# Each key (month) has a list of smaller dictionaries
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
database = {}
for month in months:
    database[month] = read_data(month)
# Output the sale for one month (price * quantity)
def monthly_sales_counter(database, month):
    month_data = database[month]
    total_monthly = 0.0
    for row in month_data:
        total_monthly += int(row['Quantity Ordered']) * float(row['Price Each'])
    return total_monthly
month1 = input('Which total monthly sales data would you like to see? ')
total_monthly = monthly_sales_counter(database, month1)
print('Total sales for {} are ${}'.format(month1, round(total_monthly, 2)))
# Output the total sale = for the whole year
def yearly_sales_counter(database):
    total_yearly = 0.0
    for month in list(database.keys()):
        month_data = database[month]
        total_monthly = 0.0
        for row in month_data:
            total_monthly += int(row['Quantity Ordered']) * float(row['Price Each'])
        total_yearly += total_monthly
    return total_yearly
total_yearly = yearly_sales_counter(database)
print('Total yearly sales are ${}'.format(round(total_yearly, 2)))
# Should: A summary: mean, min, max, monthly changes as a percentage
# Total sales in each month start#
import statistics
print(' ')
print('The number of sales in each month:')
def monthly_sales_counter(month):
    month_data = database[month]
    total_monthly = 0.0
    for row in month_data:
        total_monthly += int(row['Quantity Ordered']) * float(row['Price Each'])
    return total_monthly
total_monthly = monthly_sales_counter(month)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
wholedata = {}
for month in months:
    wholedata[month] = monthly_sales_counter(month)
for m in wholedata.keys():
    print ('Total sales in {}: ${}'.format(m, round(wholedata[m], 2)))
#total sales in each month end#
print(' ')
print('A summary of the annual sales data:')
#mean sales of the whole year start#
def year_mean(wholedata):
    mean = round(statistics.mean(wholedata.values()))
    return mean
print('Mean sales of the whole year: ${}'.format(year_mean(wholedata)))
#mean sales of the whole year end#
#max sales start#
def max_value(wholedata):
    key_max_value = max(wholedata.keys(), key=(lambda k: wholedata[k]))
    return wholedata[key_max_value]
def max_month(wholedata):
    key_max_month = max(wholedata.keys(), key=(lambda k: wholedata[k]))
    return key_max_month
print('Maximum Sales: ${} (in {})'.format(round(max_value(wholedata), 2), max_month(wholedata)))
#max sales end#
#min sales start#
def min_value(wholedata):
    key_min_value = min(wholedata.keys(), key=(lambda k: wholedata[k]))
    return wholedata[key_min_value]
def min_month(wholedata):
    key_min_month = min(wholedata.keys(), key=(lambda k: wholedata[k]))
    return key_min_month
print('Minimum Sales: ${} (in {})'.format(round(min_value(wholedata), 2), min_month(wholedata)))
#min sales end#
#monthly changes as a percentage start#
print(' ')
print("We can calculate the percentage change between two months of choice")
first_month = input("which month do you want to look at?['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']")
second_month = input(
    "which month do you want to compare it with?['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']")
perchange = round(((wholedata[second_month]) - wholedata[first_month]) / wholedata[first_month] * 100)
print("The percentage change of sales of {} compared to {} was {}%".format(first_month, second_month, perchange))
#monthly changes as a percentage end#
# The most expensive/cheapest product
def most_expensive_product(database):
    highest_price = 0.0
    for month in list(database.keys()):
        month_data = database[month]
        for row in month_data:
            if highest_price < float(row['Price Each']):
                highest_price = float(row['Price Each'])
                highest_price_item = row['Product']
    return highest_price_item, highest_price
highest_price_item, highest_price = most_expensive_product(database)
print('The most expensive product sold is {} which costs {}$.'.format(highest_price_item, highest_price))
def cheapest_product(database):
    firstProduct = True
    for month in list(database.keys()):
        month_data = database[month]
        for row in month_data:
            if firstProduct:
                lowest_price = float(row['Price Each'])
                lowest_price_item = row['Product']
                firstProduct = False
            elif lowest_price > float(row['Price Each']):
                lowest_price = float(row['Price Each'])
                lowest_price_item = row['Product']
    return lowest_price_item, lowest_price
lowest_price_item, lowest_price = cheapest_product(database)
print('The cheapest product sold is {} which costs {}$.'.format(lowest_price_item, lowest_price))
# Which product was sold the most across each month/the year
def best_seller_month(database, month):
    item_quantities = {}
    month_data = database[month]
    highest_quantity = 0
    for row in month_data:
        if row['Product'] in item_quantities.keys():
            item_quantities[row['Product']] += int(row['Quantity Ordered'])
        else:
            item_quantities[row['Product']] = int(row['Quantity Ordered'])
    for item in list(item_quantities.keys()):
        if highest_quantity < int(item_quantities[item]):
            highest_quantity = int(item_quantities[item])
            highest_quantity_item = item
    return highest_quantity_item, highest_quantity
month = input('Which month would you like to see? ')
highest_quantity_item_month, highest_quantity_month = best_seller_month(database, month)
print('The most sold item in {} is {}. Quantity sold is {}'.format(month, highest_quantity_item_month, highest_quantity_month))
def best_seller_year(database):
    item_quantities ={}
    highest_quantity = 0
    for month in list(database.keys()):
       month_data = database[month]
       for row in month_data:
           if row['Product'] in item_quantities.keys():
               item_quantities[row['Product']] += int(row['Quantity Ordered'])
           else:
               item_quantities[row['Product']] = int(row['Quantity Ordered'])
       for item in list(item_quantities.keys()):
           if highest_quantity < int(item_quantities[item]):
               highest_quantity = int(item_quantities[item])
               highest_quantity_item = item
    return highest_quantity_item, highest_quantity
highest_quantity_item_year, highest_quantity_year = best_seller_year(database)
print('The most sold item in 2019 is {}. Quantity sold is {}'.format( highest_quantity_item_year, highest_quantity_year))
# Sales by city by ranking
def sales_by_city():
    cities = {}
    for month in months:
        for row in database[month]:
            city = row['Purchase Address'].split(', ')[1]
            if city not in cities:
                cities[city] = 0
            cities[city] += int(row['Quantity Ordered']) * float(row['Price Each'])
    return cities
print('')
print('Sales by city (from max to min):')
sales_by_city_ordered = sorted(sales_by_city().items(), key=lambda x: x[1], reverse=True)
for index, city in enumerate(sales_by_city_ordered):
    print(str(index+1)+'.',city[0]+':','$'+str(round(city[1],2)))