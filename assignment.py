def read_and_modify_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ")
        
        # Open the file and read its contents
        with open(filename, 'r') as file:
            contents = file.read()
        
        # Modify the file content (example: convert to uppercase)
        modified_content = contents.upper()
        
        # Write the modified content to a new file
        new_filename = 'modified_' + filename
        with open(new_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Success! Modified content has been written to {new_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while trying to read '{filename}'.")

# Call the function
read_and_modify_file()