users={}

users["ravi@gmail.com"]='Ravi Sharma'
users["priya@gmail.com"]='Priya Patel'
users["chirag@gmail.com"]='Chirag Babu'

print(users["ravi@gmail.com"])

print("ravi@gmail.com" in users)

del users["chirag@gmail.com"]
print(users)