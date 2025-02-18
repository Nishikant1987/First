s1 = "subscribe this"
s2 = "this channel"
s3 = input("Enter a string: ")  # Take user input as a single string

# Split the input string into a list of words or phrases using commas or spaces
user_inputs = [item.strip(". ,") for item in s3.split(",")]

# Check if any of the spam phrases are in the user's input
if s1 in user_inputs or s2 in user_inputs:
    print("This is a spam")
else:
    print("It's not a spam")


    
