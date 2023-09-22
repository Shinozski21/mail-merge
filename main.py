#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"



with open("./input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()

    #print(names)

with open("./input/letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    #print(letter_contents)

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        with open(f"./Output/ReadyToSend/letter for {stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)