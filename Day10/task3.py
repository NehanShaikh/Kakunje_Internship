import shutil
import os

# 1. Copy a file named "sample.txt"
source_file = "sample.txt"
destination_file = "copy_sample.txt"

# Check if source file exists
if os.path.exists(source_file):
    
    # 2. Paste it as "copy_sample.txt"
    shutil.copy(source_file, destination_file)
    print("File copied successfully.")

    # 3. Print disk usage
    total, used, free = shutil.disk_usage(os.getcwd())
    
    print("Disk Usage Information:")
    print("Total:", total // (1024**3), "GB")
    print("Used:", used // (1024**3), "GB")
    print("Free:", free // (1024**3), "GB")

else:
    print("Source file does not exist.")
