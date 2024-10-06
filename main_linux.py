import os
import shutil

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

def main():
    #Dichiara il percorso della cartella di steam contenente i giochi
    starting_directory = os.path.join(os.path.expanduser("~"), ".steam", "steam", "steamapps", "common")

    #Menu scelta tra installare e disinstallare il programma
    print("What do you want to do?")
    print("1. Install the DLL files")
    print("2. Uninstall the DLL files")
    choice = input("Select an option: ")
    if choice == "1":
        install = True
    elif choice == "2":
        install = False
    else:
        print("Invalid choice. Exiting the program.")
        return

    print("-----------------------------------------------------------------------------")

    #Mostra all'utente i giochi e chiede su quale lavorare
    print("Directories present in the initial folder:")
    directories = list_directories(starting_directory)
    for i, d in enumerate(directories, start=1):
        print(f"{i}. {d}")
    selected_index = int(input("Select the number of the folder of interest: "))

    #Imposta la direttoria del gioco su cui eseguire il lavoro
    selected_directory = directories[selected_index - 1]

    if install == True:
        find_and_rename_dll(os.path.join(starting_directory, selected_directory))
    else:
        find_and_reset_dll(os.path.join(starting_directory, selected_directory))

    #Fine
    print("Operation completed successfully!")


if __name__ == "__main__":
    main()
