hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]



total_price = 0
for x in prices:
    total_price += x


average_price = total_price / len(prices)
print("Average price", average_price)

new_prices = [ z - 5 for z in prices ]
print("New discounted prices", new_prices)

for i in range(len(hairstyles)):
    total_price += prices[i]
    last_week[i]
print("Total revenue", total_price)

average_daily_revenue = total_price / 7

haircuts_under_30 = [ hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print("Cuts under $30", haircuts_under_30)