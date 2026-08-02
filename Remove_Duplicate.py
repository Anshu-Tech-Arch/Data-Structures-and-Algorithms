signups=[
    "ravi@gmail.com",
    "priya@gmail.com",
    "ravi@gmail.com",
    "sneha@gmail.com",
    "priya@gmail.com",
    "karan@gmail.com",
    "ravi@gmail.com"
]

emails=set(signups) # 1st method but the order might not be the same 
print(emails)

def remove_dup(emails):   #2nd method (manual)
    seen=set()
    unique=[]

    for email in emails:
        if email not in seen:
            unique.append(email)
            seen.add(email)
    return unique


print(list(dict.fromkeys(emails))) # new pythonic way 