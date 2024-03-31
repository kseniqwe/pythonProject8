with open('scratch.txt', encoding ='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.scratch ()
        ingredients = {}
        for p in range(int(ingredients_count)):
            recepie = file.scratch ().strip().split(' | ')
            product, quantity, word = recepie
        ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
file.readline()
cook_book[recepie_name] = ingredients_count