import os

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Successfully created {folder_name} folder.")
    else:
        print(f"{folder_name} folder already exists.")

# Create Data folder
create_folder("Data")

# Create Results folder
create_folder("Results")

# Run the command
os.system("python3 Hunter.py")
