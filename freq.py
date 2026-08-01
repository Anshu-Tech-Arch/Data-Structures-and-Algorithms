todays_orders=["Biryani", "Dosa", "Biryani", "Burger", "Dosa", "Biryani", "Burger", "Dosa", "Birynai"]

def count_order(orders):
    freq={}
    for dish in orders:
        if dish in freq:
            freq[dish]=freq[dish]+1
        else:
            freq[dish]=1
    return freq

print(count_order(todays_orders))