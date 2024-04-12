with open (‘scratch.txt’) as file:
       cook_book = {}
 for line in file:
    ingredient_name = line.strip()
    num_ing = int(file.readline())
    ing_dish = []
 for _ in range(num_ing):
    num = file.readline().strip()
    ingredient_name, quantity, measure = num.split(’ | ')
    ing_dish.append(
 for(for ingradient in file.readlines(): )
    ‘quantity’: quantity,
    ‘measure’: measure}
    cook_book[ingredient_name] = ing_dish
    ile.readline()

    print(cook_book)