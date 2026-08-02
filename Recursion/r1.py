def eat_mangoes(count):
    if count==0:
        print('Hand is empty')
        return
    print(f"I have {count} mangoes. Eating one ")
    eat_mangoes(count-1)

eat_mangoes(3)