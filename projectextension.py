import csv
import statistics
f = open('review.txt', 'w+')
print('Intro...\n')
f.write('Intro...\n\n')
# Read one month
def read_one_month(month):
    data = []
    with open('Sales_{}_2019.csv'.format(month), 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            if (row['Quantity Ordered'] != '') and (row['Quantity Ordered'] != 'Quantity Ordered'): # cleaning data
                data.append(row)
    return data
# Create a dictionary "Database" that stores data of 12 months
def read_all_months():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    database = {}
    for month in months:
        database[month] = read_one_month(month)
    return database
database = read_all_months()
# Output the total sale = for the whole year
def yearly_sales_counter():
    total_yearly = 0.0
    for month in database:
        month_data = database[month]
        total_monthly = 0.0
        for row in month_data:
            total_monthly += int(row['Quantity Ordered']) * float(row['Price Each'])
        total_yearly += total_monthly
    return total_yearly
total_yearly = yearly_sales_counter()
print('Total yearly sales are ${}.\n'.format(f'{round(total_yearly, 2):,}'))
f.write('Total yearly sales are ${}.\n\n'.format(f'{round(total_yearly, 2):,}'))
# Output the sale for one month (price * quantity)
def monthly_sales_counter(month):
    month_data = database[month]
    total_monthly = 0.0
    for row in month_data:
        total_monthly += int(row['Quantity Ordered']) * float(row['Price Each'])
    return total_monthly
month = input('Which total monthly sales data would you like to see? ').capitalize()
total_monthly = monthly_sales_counter(month)
print('Total sales for {} are ${}\n'.format(month, f'{round(total_monthly, 2):,}'))
# Total sales in each month
print('The number of sales in each month:')
f.write('The number of sales in each month:\n')
wholedata = {}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for month in months:
    wholedata[month] = monthly_sales_counter(month)
for m in wholedata.keys():
    print('Total sales in {}: ${}'.format(m, f'{round(wholedata[m], 2):,}'))
    f.write('Total sales in {}: ${}\n'.format(m, f'{round(wholedata[m], 2):,}'))
print('\nA summary of the annual sales data:')
f.write('\nA summary of the annual sales data:\n')
# Mean sales of the whole year
def year_mean(wholedata):
    mean = round(statistics.mean(wholedata.values()))
    return mean
print('Mean sales of the whole year: ${}'.format(f'{year_mean(wholedata):,}'))
f.write('Mean sales of the whole year: ${}\n'.format(f'{year_mean(wholedata):,}'))
# Max sales
def max_value(wholedata):
    key_max_value = max(wholedata.keys(), key=(lambda k: wholedata[k]))
    return wholedata[key_max_value]
def max_month(wholedata):
    key_max_month = max(wholedata.keys(), key=(lambda k: wholedata[k]))
    return key_max_month
print('Maximum Sales: ${} (in {})'.format(f'{round(max_value(wholedata), 2):,}', max_month(wholedata)))
f.write('Maximum Sales: ${} (in {})\n'.format(f'{round(max_value(wholedata), 2):,}', max_month(wholedata)))
# Min sales
def min_value(wholedata):
    key_min_value = min(wholedata.keys(), key=(lambda k: wholedata[k]))
    return wholedata[key_min_value]
def min_month(wholedata):
    key_min_month = min(wholedata.keys(), key=(lambda k: wholedata[k]))
    return key_min_month
print('Minimum Sales: ${} (in {})\n'.format(f'{round(min_value(wholedata), 2):,}', min_month(wholedata)))
f.write('Minimum Sales: ${} (in {})\n\n'.format(f'{round(min_value(wholedata), 2):,}', min_month(wholedata)))
# Monthly changes as a percentage for 2 given months of user
print("We can calculate the percentage change between two months of choice.")
first_month = input("Which month do you want to look at? ").capitalize()
second_month = input("Which month do you want to compare it with? ").capitalize()
perchange = round(((wholedata[second_month]) - wholedata[first_month]) / wholedata[first_month] * 100)
print("The percentage change of sales of {} compared to {} was {}%\n".format(first_month, second_month, perchange))
# Monthly changes as a percentage for the whole year
print("The percentage change of sales between two consecutive months:")
f.write("The percentage change of sales between two consecutive months:\n")
for i in range(11):
    perchange = round(((wholedata[months[i+1]]) - wholedata[months[i]]) / wholedata[months[i]] * 100)
    print(months[i]+'/'+months[i+1]+': '+str(perchange)+'%')
    f.write(months[i]+'/'+months[i+1]+': '+str(perchange)+'%\n')
# The most expensive product
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
print('\nThe most expensive product sold is {} which costs ${}.'.format(highest_price_item, f'{highest_price:,}'))
f.write('\nThe most expensive product sold is {} which costs ${}.\n'.format(highest_price_item, f'{highest_price:,}'))
# The cheapest product
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
print('The cheapest product sold is {} which costs ${}.\n'.format(lowest_price_item, f'{lowest_price:,}'))
f.write('The cheapest product sold is {} which costs ${}.\n\n'.format(lowest_price_item, f'{lowest_price:,}'))
# Which product was sold the most across chosen month
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
print('We can show you the stats for the most and least sold items of your chosen month.')
month = input('Which month would you like to look at? ').capitalize()
highest_quantity_item_month, highest_quantity_month = best_seller_month(database, month)
print('The most sold item in {} is {}. Quantity sold is {}.'.format(month, highest_quantity_item_month, f'{highest_quantity_month:,}'))
f.write('The most sold item in {} is {}. Quantity sold is {}.\n'.format(month, highest_quantity_item_month, f'{highest_quantity_month:,}'))
# Which product was sold the least across chosen month
def worst_seller_month(database, month):
    item_quantities = {}
    month_data = database[month]
    lowest_quantity = highest_quantity_month
    for row in month_data:
        if row['Product'] in item_quantities.keys():
            item_quantities[row['Product']] += int(row['Quantity Ordered'])
        else:
            item_quantities[row['Product']] = int(row['Quantity Ordered'])
    for item in list(item_quantities.keys()):
        if lowest_quantity > int(item_quantities[item]):
            lowest_quantity = int(item_quantities[item])
            lowest_quantity_item = item
    return lowest_quantity_item, lowest_quantity
lowest_quantity_item_month, lowest_quantity_month = worst_seller_month(database, month)
print('The least sold item in {} is {}. Quantity sold is {}.\n'.format(month, lowest_quantity_item_month, f'{lowest_quantity_month:,}'))
f.write('The least sold item in {} is {}. Quantity sold is {}.\n\n'.format(month, lowest_quantity_item_month, f'{lowest_quantity_month:,}'))
# Which product was sold the most across the year
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
print('The most sold item in 2019 is {}. Quantity sold is {}.'.format(highest_quantity_item_year, f'{highest_quantity_year:,}'))
f.write('The most sold item in 2019 is {}. Quantity sold is {}.\n'.format(highest_quantity_item_year, f'{highest_quantity_year:,}'))
# Which product was sold the least across the year
def worst_seller_year(database):
    item_quantities ={}
    lowest_quantity = highest_quantity_year
    for month in list(database.keys()):
       month_data = database[month]
       for row in month_data:
           if row['Product'] in item_quantities.keys():
               item_quantities[row['Product']] += int(row['Quantity Ordered'])
           else:
               item_quantities[row['Product']] = int(row['Quantity Ordered'])
    for item in list(item_quantities.keys()):
       if lowest_quantity > int(item_quantities[item]):
           lowest_quantity = int(item_quantities[item])
           lowest_quantity_item = item
    return lowest_quantity_item, lowest_quantity
lowest_quantity_item_year, lowest_quantity_year = worst_seller_year(database)
print('The least sold item in 2019 is {}. Quantity sold is {}.\n'.format(lowest_quantity_item_year, f'{lowest_quantity_year:,}'))
f.write('The least sold item in 2019 is {}. Quantity sold is {}.\n\n'.format(lowest_quantity_item_year, f'{lowest_quantity_year:,}'))
# Sales by city
def sales_by_city():
    cities = {}
    for month in database:
        for row in database[month]:
            city = row['Purchase Address'].split(', ')[1]
            if city not in cities:
                cities[city] = 0
            cities[city] += int(row['Quantity Ordered']) * float(row['Price Each'])
    return cities
print('Sales by city (from max to min):')
f.write('Sales by city (from max to min):\n')
# Rank sales by city from max to min
sales_by_city_ordered = sorted(sales_by_city().items(), key=lambda x: x[1], reverse=True)
for index, city in enumerate(sales_by_city_ordered):
    output = str(index+1)+'. '+city[0]+': '+'$'+f'{round(city[1], 2):,}'
    print(output)
    f.write(output+'\n')
f.close()