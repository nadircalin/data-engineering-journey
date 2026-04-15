# ----------------------------
# Function to clean data
# ----------------------------
def clean_data(data):

    # This list will store cleaned rows
    clean_data_list = []

    # Loop through each line of raw data
    for item in data:

        # Remove hidden spaces/newlines and fix bad characters
        parts = item.strip().replace("\\", "").split(",")

        # Extract values
        name = parts[0]
        age = parts[1]
        salary = parts[2]

        # ----------------------------
        # Clean age
        # ----------------------------
        if age == "":
            age = 0
        else:
            age = int(age)

        # ----------------------------
        # Clean salary
        # ----------------------------
        if salary == "":
            salary = 0
        else:
            salary = int(salary)

        # Add cleaned row to list
        clean_data_list.append([name, age, salary])

    return clean_data_list


# ----------------------------
# Read data from file
# ----------------------------

file = open("data.txt", "r")

data = file.read().splitlines()

file.close()


# ----------------------------
# Run cleaning function
# ----------------------------

result = clean_data(data)

# ----------------------------
# Output result
# ----------------------------

print(result)