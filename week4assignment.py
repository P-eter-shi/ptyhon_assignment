#file creation
def read_write_file():
    try:
        #allow user input of file name
        file_name=input("Enter the file name:")
        
        with open(file_name, "r") as file:
            modified_content=file.read().upper()
        
        #writting the modified version
        new_file="modifiedv"+file_name
        with open(new_file, "w") as file:
            file.write(modified_content)
        
        print(f"Modified content written to {new_file}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
read_write_file()