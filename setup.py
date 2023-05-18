import os
import subprocess

# Check if the Data folder exists
data_folder = "Data"
if os.path.exists(data_folder):
    print("Data folder already exists.")
else:
    os.mkdir(data_folder)
    print("Data folder created.")

# Check if the Results folder exists
results_folder = "Results"
if os.path.exists(results_folder):
    print("Results folder already exists.")
else:
    os.mkdir(results_folder)
    print("Results folder created.")

# Create Cp.txt and Ok.txt files in the Results folder
cp_file = os.path.join(results_folder, "Cp.txt")
ok_file = os.path.join(results_folder, "Ok.txt")

if os.path.exists(cp_file):
    print("Cp.txt already exists.")
else:
    with open(cp_file, "w") as f:
        f.write("")

    print("Cp.txt created.")

if os.path.exists(ok_file):
    print("Ok.txt already exists.")
else:
    with open(ok_file, "w") as f:
        f.write("")

    print("Ok.txt created.")

# Run python3 Hunter.py command
subprocess.run(["python3", "Hunter.py"])
