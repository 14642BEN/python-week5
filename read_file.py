def modify_content(content):
    """Modify the content before writing to a new file (e.g., convert to uppercase)."""
    return content.upper()  # Example: Convert text to uppercase

# Ask the user for the filename
filename = input("Enter the filename to read: ")

try:
    # Attempt to open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content
    modified_content = modify_content(content)

    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"✅ Successfully modified the file! New file saved as '{new_filename}'.")

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"❌ Error: Permission denied while accessing '{filename}'.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
