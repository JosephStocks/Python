import pickle

def print_prompt():
    print("Electronic Phone Book\n=====================")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")

def get_user_input():
    return int(input("\nWhat do you want to do (1-5)? "))

def look_up_entry():
    print("Looking up an entry..")
    name = input("What is the name? ").strip().lower()
    if name in phonebook_dict:
        print(f"{name.capitalize()}'s phone number is {phonebook_dict[name]}.")
    else:
        print(f"{name.capitalize()} is not in the phone book.")

def set_entry():
    name = input("What is the name? ").strip().lower()
    number = input("What is the number? ").strip()
    phonebook_dict[name] = number

def delete_entry():
    name = input("What name would you like to delete? ").strip().lower()
    if name in phonebook_dict:
        print(f"{name.capitalize()}'s entry is deleted.")
    else:
        print(f"{name.capitalize()} is not in the phone book.")

def list_entries():
    print("Printing phonebook entries..")
    for name, number in phonebook_dict.items():
        print(f"{name.capitalize()}: {number}")

def load_pickled_dict():
    try:
        with open(dict_file_name, 'rb') as pickle_file:
            phonebook_dict = pickle.load(pickle_file)
        print (f"Loading {dict_file_name}...")
    except FileNotFoundError:
        phonebook_dict = {}
    return phonebook_dict

def dump_pickled_dict():
    with open(dict_file_name, 'wb') as pickle_file:
        pickle.dump(phonebook_dict, pickle_file)


dict_file_name = "phonebook_dict.pickle"
phonebook_dict = load_pickled_dict()
finished = False
while not finished:
    print_prompt()
    user_input = get_user_input()
    print()
    if user_input == 5:
        finished = True
        print("writing to disk...")
        dump_pickled_dict()
        print("Bye!")
        break
    if user_input == 1:
        look_up_entry()
    elif user_input == 2:
        set_entry()
    elif user_input == 3:
        delete_entry()
    elif user_input == 4:
        list_entries()
    else:
        print("The only options are 1 through 5. Please try again.")

    print('\n')
    