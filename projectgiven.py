import csv
import statistics

print("Here is a summary of the sales of iphones in 2018")
def read_data():
    data = []
    with open('../sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def run():
    data = read_data()
    sales = []
    months = []
    for row in data:
        sale = int(row['sales'])
        month = row['month']
        sales.append(sale)
        months.append(month)
    total = sum(sales)
    print('Total sales: {}'.format(total))
    sales_average = round(statistics.mean(sales), 2)
    print('The average of yearly sales is: {}'.format(sales_average))
    highest_sale = 0
    for i in range(len(months)):
        if highest_sale < sales[i]:
            highest_sale = sales[i]
            highest_sale_month = months[i]
    print('The highest sales month: {}'.format(highest_sale_month))
    lowest_sale = min(sales)
    for i in range(len(months)):
        if lowest_sale == sales[i]:
            lowest_sale_month = months[i]
            break
    print('The lowest sale month: {}'.format(lowest_sale_month))

    def percentage_change(month):
        for row in read_data():
            if row['month'] == month:
                return (row['sales'])

    first_month = input("which month do you want to look at?[jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]")
    second_month = input("which month do you want to compare it with?[jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]")
    perchange =round((int(percentage_change(second_month))-int(percentage_change(first_month)))/int(percentage_change(first_month))*100)
    print("The percentage change of sales between {} and {} was {}%".format(first_month, second_month, perchange))

    field_names = ['total', 'percentage_change', 'average', 'min_sales_month', 'max_sales_month']
    new_data = [
        {'total': total, 'percentage_change': perchange, 'average': sales_average, 'max_sales_month': highest_sale_month, 'min_sales_month': lowest_sale_month},
    ]
    with open('../extension.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames = field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(new_data)

run()



