 ##################################################################################
# Name: Ugyen Lhendup
# Course: First Year B.E in ECE
# Student ID Number: 02230116
##################################################################################
# REFERENCES:
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://codereview.stackexchange.com/questions/281633/calculate-score-of-rock-paper-scissors-advent-of-code-2022-day-2
# https://chat.openai.com/
#####################################################################################
# SOLUTION
# Solution Score: 50023
######################################################################################

# Firstly I defined the function named read_input. 
# The parameter  f_name was passed to take the name of the file
def read_input(f_name):
    # In order to store the results of the given file, I initialize an empty list named round_results
    round_results = []
    # This opens the the file when file name is passed as the argument of the function for the parameter f_name
    # If the file is not in the directory of the python file, we have to give specific location of the file
    with open(f_name, 'r') as rps_file:
        # For reading every line in the file, I used for loop to iterates over each line
        for line in rps_file:
            # As the file contain two letters in a line, first for the shape (rock,paper or scissor) and
            # second for outcome i.e whether to lose, win or draw, I splited it and assigned them to 
            # the variable named shape and outcome 
            shape, outcome = line.split()
            # Here round_result is been updated by appending the splitted line. I appeneded splitted lines i.e
            # shape and outcome in list. Therefore, round_result will have nested list which becomes 2 column array
            round_results.append([shape, outcome])
    # This returns the final items stored in round_results. 
    return round_results
#As a whole, read_input function will return the array stored in round_result


# Then I defined calculate_score function having parameter results to calculate the score of the game.
# Here I have to pass the results form above function to calculate the scores
def calculate_score(results):
    # The variable t_score was initialized to 0 to store the total score.
    t_score = 0
    # To calculate the score, the result array is iterated and following comparison are done to update
    # the score accordingly in t_score variable
    # |shape|        |score|           |outcome|    |score|
    #  A (Rock)        +1               X (Lose)      +0       
    #  B (Paper)       +2               Y (Draw)      +3
    #  C (Scissor)     +3               Z (Win)       +6
    for shape, outcome in results:
        #shape scores
        if shape == "A":
            shape_score = 1
        elif shape == "B":
            shape_score = 2
        elif shape == "C":
            shape_score = 3

        #outcome scores
        if outcome == "X":
            outcome_score = 0
        elif outcome == "Y":
            outcome_score = 3
        elif outcome == "Z":
            outcome_score = 6
        
        # Here the score is updated till the end of the loop
        t_score += shape_score   + outcome_score
    # Then final total score is returned
    return t_score
# In sumarry, the calculate_score function returns the total sum of the score

# The variable result declared here stores the value of the function called by passing the 
# name of the file as the argument
results = read_input("input_6_cap1.txt")
# The variable score stores the score by calling the calculate_score function and passing
# result as the argument
score = calculate_score(results)
# Finally score is printed
print(f"Total Score: {score}")


