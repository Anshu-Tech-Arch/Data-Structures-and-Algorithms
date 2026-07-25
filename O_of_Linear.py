def find_paper(papers, name):
    for paper in papers:
        if paper==name:
            return True
    return False

papers=['Anita', 'Bharat', 'Pawan', 'Harsh', 'Lalit', 'Karan', 'Diya', 'Esha']
search_name='Karan'
result=find_paper(papers, search_name)

if result==True:
    print(f"Found!")
else:
    print('Not Found!')