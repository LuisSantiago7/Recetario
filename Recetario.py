from pathlib import Path, PureWindowsPath
import os
list_recipes = []
count_recipes = []
list_categories = []
count_categories = []


#Function of welcome
def welcome():
    os.system('cls')
    print('''                               RECETARIO

¡Bienvenido!, en este recetario encontrás reetas de todo tipo y de todas las categorias... desde ensaladas, hasta cortes de carne.
¡Disfrutalo!.\n''')
    
    
#function rut acces
def rut_acces():
    rut_home = Path('C:/Recetas')
    print(f'''Este recetario se encuentra en la ruta "{rut_home}" de tu PC.''')
    return rut_home
    
    
#function to enumerate categories and recipes (just amount)
def enumerate_categories_recipes(rut_home):
    count_category = 0
    count_recipes = 0
    rut_home_iter = os.listdir(rut_home)
    for i in rut_home_iter:
        count_category += 1
    for j in Path(rut_home).glob('**/*.txt'):
        count_recipes +=1
    print(f'''
En este recetario hay {count_category} categorias, y {count_recipes} recetas disponibles de las cuales puedes leerlas, crearlas, y eliminarlas! al igual que a las categorias.''')
    
#function for inform categories aviable
def inform_categories(rut_home):
   
    dictionary_categories = {}
    count = 0
    rut_home_iter = Path.iterdir(rut_home)
    for i in rut_home_iter:
        count +=1
        list_categories.append(i.name)
        count_categories.append(count)
        print(f'{count} .- {i.name}')
    
    
    for count, catego in zip(count_categories, list_categories):
        dictionary_categories[count] = catego
    return dictionary_categories

#function to inform recipies
def inform_recipes(value, rut_home):
    
    dictionary_recipes = {}
    count = 0
    new_rut = Path(rut_home, value)
    for txt in new_rut.glob('*.txt'):
        count += 1
        print(f'{count}.- {txt.stem}')
        list_recipes.append(txt)
        count_recipes.append(count)
        
        
    for count, recipie in zip(count_recipes, list_recipes):
        dictionary_recipes[count] = recipie
    return dictionary_recipes
        
 #function de main menu, aks to user what to do:
def main_menu():
    option = int(input('''
    ¿Que quieres hacer?
            
[1] -Leer una Receta
[2] -Crear una Receta
[3] -Crear una categoria
[4] -Eliminar una Receta
[5] -Eliminar una Categoria
[6] -Finalizar el programa\n
Elige una opcion: '''))
    os.system('cls')
    return option
    
    
#function for choose a category
def choose_category(dictionary_categories): #i delete arg rut_home
    choose_option_category = int(input('Elige una categoria: '))
    os.system('cls')
    for key, value in dictionary_categories.items():
        if choose_option_category == key:
            print(f'      {value.upper()}       ')
            return value #(choosen_category)
        
#function for choose a recipies
def choose_recipes(dictionary_recipes):
    choose_option_recipes = int(input('Elige una rectea: '))
    os.system('cls')
    for key_recipe, value_recipe in dictionary_recipes.items():
        if choose_option_recipes == key_recipe:
            return value_recipe
    
        
#function to read recipes
def read_recipe(value_recipe):
    print(Path.read_text(value_recipe))
    
         
#function to make recipie
def make_recipie(rut_home, value):
    exist = False
    while not exist:
        name_recipe = input('¿Nombre de receta?: ') + '.txt'
        content_recipe = input('Contenido de la receta')
        new_rut = Path(rut_home, value, name_recipe)
        if not os.path.exists(new_rut):
            with open(new_rut, 'w') as file:
                file.write(content_recipe)
            print('Receta creada con exito ✅')
            list_recipes.append(name_recipe)
            exist = True
        else:
            print('La receta ya existe ❌')

           
#function to make category
def make_category(rut_home):
    exist = False
    while not exist:
        name_category = input('¿Nombre de la categoria?: ')
        new_rut = Path(rut_home, name_category)
        if not os.path.exists(new_rut):
            os.mkdir(new_rut)
            print('Categoria creada con exito ✅')
            list_categories.append(name_category)
            exist = True
        else:
            print('La receta ya existe ❌')
            
#function to emove recipe
def rm_recipe(value_recipe):
    Path(value_recipe).unlink()
    print('Receta eliminada con exito ✅')
            
            
#function to remove category
def rm_category(value):
    Path(value).rmdir()
    print('Categoría eliminada con exito ✅')


#Funcion para finalizar programa
def return_main_menu():
    input("\nPresiona Enter para regresar al menú principal...")
        

        

#Cicle of the program
while True:
    #Function of welcome
    welcome()
    #function rut acces
    rut_home = rut_acces()
    #function to enumerate categories and recipes (just amount)
    enumerate_categories_recipes(rut_home)
    #function de main menu, aks to user what to do:
    option = main_menu()
    if option == 1:#Read a Recipe
        #function for inform categories aviable
        dictionary_categories = inform_categories(rut_home)
        #function for choose a category
        value = choose_category(dictionary_categories)
        #function to inform recipes
        dictionary_recipes = inform_recipes(value,rut_home)
        #function to choose recipes
        value_recipe = choose_recipes(dictionary_recipes)
        #function to read recipes
        read_recipe(value_recipe)
        return_main_menu()
    elif option == 2:#Make a Recipe
        #function for inform categories aviable
        dictionary_categories = inform_categories(rut_home)
        #function for choose a category
        value = choose_category(dictionary_categories)
        #function to inform recipes
        make_recipie(rut_home, value)
        return_main_menu()
    elif option == 3:#Make a category
        #function to make category
        make_category(rut_home)
        return_main_menu()
    elif option == 4:#Remove a recipe
        #function for inform categories aviable
        dictionary_categories = inform_categories(rut_home)
        #function for choose a category
        value = choose_category(dictionary_categories)
         #function to inform recipes
        dictionary_recipes = inform_recipes(value,rut_home)
         #function to choose recipes
        value_recipe = choose_recipes(dictionary_recipes)
        #function to emove recipe
        rm_recipe(value_recipe)
        return_main_menu()
    elif option == 5:#Remove a Category
         #function for inform categories aviable
        dictionary_categories = inform_categories(rut_home)
        #function for choose a category
        value = choose_category(dictionary_categories)
        return_main_menu()
    elif option ==6:#Finish the program
        print('Gracias por probar mi codigo'.upper())
        return_main_menu()
        
        
        
        
        
   
    
    



    
    
