def get_name(prompt):
    name = input(prompt)
    return name

player_name = get_name("What is your name? ")
print(f"Welcome to pong, {player_name}")

def show_menu():
    print("""
1. Start Game \n 
2. Quit \n 
Choose an option:""")
    try:
        option = int(input())
        return option
    except ValueError:
            return None
    

playing = True
while playing:
    option = show_menu()
    if option == 1:
        print("Starting game ...")
        #show_menu()
    elif option == 2:
        print(f"Goodbye, {player_name}")
        playing = False
    else:
        print("Invalid option, please choose 1 or 2")
     