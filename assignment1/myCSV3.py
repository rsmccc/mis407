import csv

with open('myData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    prices = []
    for row in readCSV:
        color = row[3]
        date = row[0]
        price = row[4]
        
        dates.append(date)
        colors.append(color)
        prices.append(price)

    print(dates)
    print(colors)
    print(prices)

    # now, remember our lists?

    whatColor = input('What color do you wish to know the date of?:')
    coldex = colors.index(whatColor)
    theDate = dates[coldex]
    print('The date of ' + whatColor + ' is: ' + theDate)
    thePrice = prices[coldex]
    print('The price of the ' + whatColor + ' shirt is: $' + thePrice)
