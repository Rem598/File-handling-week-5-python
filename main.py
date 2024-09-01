
# File Creation and Writing
try:
    with open("my_file.txt", "w") as file:
        file.write("This is the first line of text.\n")
        file.write("Python is fun\n")
        file.write("These are numbers: 0123456789.\n")
    print("File created and initial content written successfully.")
except Exception as e:
    print(f"An error occurred during file creation: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("\nReading from the file:")
    print(content)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred during file reading: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending another line.\n")
        file.write("456789\n")
        file.write("Final line with more text and numbers: 654321888.\n")
    print("Additional content appended successfully.")
except Exception as e:
    print(f"An error occurred during file appending: {e}")

# Final Error Handling Example (to catch and handle any unexpected errors)
try:
    # Assuming some risky operation here for demonstration purposes
    with open("my_file.txt", "r") as file:
        # Simulate risky operation
        content = file.read()
        print("\nFinal read to ensure content is updated:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operation completed.")
