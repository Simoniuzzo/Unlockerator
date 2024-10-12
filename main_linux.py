import os
import shutil
import argparse
import main_native_linux

#Permette di inserire un percorso della cartella di steam custom
parser = argparse.ArgumentParser()
parser.add_argument('--manual', help='Manual path for Steam common folder')
args = parser.parse_args()

if args.manual:
    starting_directory = args.manual
else:
    starting_directory = os.path.join(os.path.expanduser("~"), ".steam", "steam", "steamapps", "common")

def find_and_rename_dll(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".dll"):
                if file.startswith("steam_api."):
                    new_name = os.path.join(root, "steam_api_o.dll")
                    os.rename(os.path.join(root, file), new_name)
                    data_dir = os.path.join(os.path.dirname(__file__), "data")
                    shutil.copy(os.path.join(data_dir, "steam_api.dll"), root)
                    shutil.copy(os.path.join(data_dir, "SmokeAPI.config.json"), root)
                    return
                elif file.startswith("steam_api64."):
                    new_name = os.path.join(root, "steam_api64_o.dll")
                    os.rename(os.path.join(root, file), new_name)
                    data_dir = os.path.join(os.path.dirname(__file__), "data")
                    shutil.copy(os.path.join(data_dir, "steam_api64.dll"), root)
                    shutil.copy(os.path.join(data_dir, "SmokeAPI.config.json"), root)
                    return

def find_and_reset_dll(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".dll"):
                if file.startswith("steam_api_o."):
                    os.remove(os.path.join(root, "steam_api.dll"))
                    os.remove(os.path.join(root, "SmokeAPI.config.json"))
                    new_name = os.path.join(root, "steam_api.dll")
                    os.rename(os.path.join(root, file), new_name)
                    return
                elif file.startswith("steam_api64_o."):
                    os.remove(os.path.join(root, "steam_api64.dll"))
                    os.remove(os.path.join(root, "SmokeAPI.config.json"))
                    new_name = os.path.join(root, "steam_api64.dll")
                    os.rename(os.path.join(root, file), new_name)
                    return

def list_directories(directory):
    directories = []
    for entry in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, entry)):
            directories.append(entry)
    return directories

def menu():
    install = 0

    #Menu scelta tra installare e disinstallare il programma
    print("Welcome to Unlockerator Installer!")
    print("Please choose an option:")
    print("1. Install for Native games")
    print("2. Install/Uninstall for Proton games")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        main_native_linux.main()
        install = 0

    elif choice == '2':
        print("Please choose an option:")
        print("1. Install for Proton games")
        print("2. Uninstall for Proton games")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            install = 1
        else:
            install = 2

    else:
        print("Invalid choice. Exiting...")
        exit(1)

    return install

def print_directories(directories):
    directories = list_directories(starting_directory)
    print("Directories present in the initial folder:")
    for i, d in enumerate(directories, start=1):
        print(f"{i}. {d}")
    selected_index = int(input("Select the number of the folder of interest: "))

    #Imposta la direttoria del gioco su cui eseguire il lavoro
    selected_directory = directories[selected_index - 1]
    return selected_directory

def main():
    #Stampa il menu e assegna la scelta nella variabile install
    install = menu()

    #Mostra all'utente i giochi e chiede su quale lavorare
    if install == 1:
        #Array contenente tutte le cartelle presenti al percorso di steamapps/common
        directories = list_directories(starting_directory)

        #Mostra le direttorie e chiede all'utente quale selezionare
        selected_directory = print_directories(directories)

        find_and_rename_dll(os.path.join(starting_directory, selected_directory))
    elif install == 2:
        #Array contenente tutte le cartelle presenti al percorso di steamapps/common
        directories = list_directories(starting_directory)

        #Mostra le direttorie e chiede all'utente quale selezionare
        selected_directory = print_directories(directories)

        find_and_reset_dll(os.path.join(starting_directory, selected_directory))
    #Fine
    print("Operation completed successfully!")

if __name__ == "__main__":
    main()
