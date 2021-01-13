"""Generate sales report showing total melons each salesperson sold."""

#two empty lists: salespeople and melons_sold
salespeople = []
melons_sold = []

name = 0
total_price = 1
total_melons = 2
column_set = [name, total_price, total_melons]
#I've eliminated magic numbers, which gets rid of, in this file, indices out of context.
# f is a bad name for a variable changing it to something sensicle
filename = open('sales-report.txt')

for line in filename:  # changed f to filename
    line = line.rstrip() # this is stripping trailing white space
    # changed |'s to commas because that's an actual standard. 
    entry = line.split(',') # split by comma delimiter. changes "entries" to entry because it makes more sense
    
    if len(entry) != len(column_type): #added check on data to make sure items in list are 3
        continue #continue this if items != 3
    salesperson = entry[name]
    price = float(entry[total_price]) # added in price because it was omitted
    melons = int(entry[total_melons])

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        
        #melons_sold[position] = melons_sold[position] + melons
        melons_sold[position] += melons  # reads # of melons sold out,and adds number of melons to the postition index
    else:
        #adds the salesperson to salespeople list and melons sold if not already in list
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
