def count_and_replace_terrible(file_to_read, file_to_write):
    # Read the file
    with open(file_to_read, 'r') as file:
        text = file.read()

    # Count the occurrences of "terrible"
    count = text.count("terrible")

    # Replace every even occurrence of "terrible" with "pathetic"
    text = text.replace("terrible", "pathetic", count // 2)

    # Replace every odd occurrence of "terrible" with "marvellous"
    text = text.replace("terrible", "marvellous", count - (count // 2))

    # Write the new text to the result file
    with open(file_to_write, 'w') as file:
        file.write(text)

    # Return the count of "terrible" occurrences
    return count

# File paths
file_to_read = "file_to_read.txt"
file_to_write = "result.txt"

# Call the function and display the count
terrible_count = count_and_replace_terrible(file_to_read, file_to_write)
print(f"The word 'terrible' appears {terrible_count} times.")