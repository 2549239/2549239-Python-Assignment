def read_letter_values(file): # File reading #
    letter_values = {}
    with open(file, 'r') as values_file:
        for line in values_file:
            letter, value = line.split()
            letter_values[letter] = int(value)
    return letter_values

def compute_score(position, letter, letter_values): # computing the score#
    if position == 'first':
        return 0
    elif position == 'last':
        return 20 if letter == 'E' else 5
    else:
        position_value = {'second': 1, 'third': 2}.get(position, 3)
        commonness_values = {
            'Q': 1, 'Z': 1, 'J': 3, 'X': 3, 'K': 6, 'F': 7, 'H': 7, 'V': 7, 'W': 7, 'Y': 7,
            'B': 8, 'C': 8, 'M': 8, 'P': 8, 'D': 9, 'G': 9, 'L': 15, 'N': 15, 'R': 15, 'S': 15, 'T': 15,
            'O': 20, 'U': 20, 'A': 25, 'I': 25, 'E': 35
        }
        return position_value + commonness_values.get(letter, 0)

def generate_abbreviations(name, letter_values): #Generating the abbreviations#
    words = [word.upper() for word in name.split() if word.isalpha()]
    abbreviations = set()

    for word in words:
        if len(word) >= 3:
            abbreviation = word[:3]  # Start with the first three letters
            score = compute_score('first', abbreviation[1], letter_values)
            abbreviations.add((abbreviation, score))
            
    return abbreviations


def choose_best_abbreviations(abbreviations): # Selecting the best abbreviations#
    best_abbreviations = {}
    for abbreviation, score in abbreviations:
        if abbreviation not in best_abbreviations:
            best_abbreviations[abbreviation] = score
        else:
            best_abbreviations[abbreviation] = min(score, best_abbreviations[abbreviation])
    
    return best_abbreviations

def generate_output(file_name, input_file, letter_values): #Generating output file #
    output_file_name = f"ike_trees_abbrevs.txt"

    with open(input_file, 'r') as input_file:
        names = input_file.read().splitlines()

    with open(output_file_name, 'w') as output_file:
        for name in names:
            output_file.write(name + "\n")
            abbreviations = generate_abbreviations(name, letter_values)
            best_abbreviations = choose_best_abbreviations(abbreviations)
            best_abbrevs = [abbr for abbr, score in best_abbreviations.items() if score == min(best_abbreviations.values())]
            formatted_abbrevs = ' '.join([f"{abbr}({score})" for abbr, score in best_abbreviations.items()])
            output_file.write(formatted_abbrevs + "\n" if formatted_abbrevs else "\n")

def main(): # Main function#
    input_file = input("Enter the name of the input file (with .txt extension): ")
    file_name = input_file.split('.')[0]
    values_file = 'values.txt'

    letter_values = read_letter_values(values_file)
    generate_output(file_name, input_file, letter_values)

if __name__ == "__main__":
    main()



# def read_letter_values(file):
#     letter_values = {}
#     with open(file, 'r') as values_file:
#         for line in values_file:
#             letter, value = line.split()
#             letter_values[letter] = int(value)
#     return letter_values

# def compute_score(position, letter, letter_values):
#     if position == 'first':
#         return 0
#     elif position == 'last':
#         return 20 if letter == 'E' else 5
#     else:
#         position_value = {'second': 1, 'third': 2}.get(position, 3)
#         commonness_values = {
#             'Q': 1, 'Z': 1, 'J': 3, 'X': 3, 'K': 6, 'F': 7, 'H': 7, 'V': 7, 'W': 7, 'Y': 7,
#             'B': 8, 'C': 8, 'M': 8, 'P': 8, 'D': 9, 'G': 9, 'L': 15, 'N': 15, 'R': 15, 'S': 15, 'T': 15,
#             'O': 20, 'U': 20, 'A': 25, 'I': 25, 'E': 35
#         }
#         return position_value + commonness_values.get(letter, 0)

# def generate_abbreviations(name, letter_values):
#     words = [word.upper() for word in name.split() if word.isalpha()]
#     abbreviations = set()

#     for word in words:
#         if len(word) >= 3:
#             for i in range(len(word) - 2):
#                 abbreviation = word[i:i+3]
#                 if len(set(abbreviation)) == 3:  # Ensure distinct letters in the abbreviation
#                     score = compute_score(
#                         'first' if i == 0 else 'other' if i + 2 < len(word) - 1 else 'last',
#                         abbreviation[1], letter_values)
#                     abbreviations.add((abbreviation, score))

#     return abbreviations

# def choose_best_abbreviations(abbreviations):
#     best_abbreviations = {}
#     for abbreviation, score in abbreviations:
#         if abbreviation[1:] not in best_abbreviations or best_abbreviations[abbreviation[1:]] > score:
#             best_abbreviations[abbreviation[1:]] = score

#     return {abbr: score for abbr, score in abbreviations if best_abbreviations[abbr[1:]] == score}

# def generate_output(file_name, input_file, letter_values):
#     output_file_name = f"ikee_trees_abbrevs.txt"

#     with open(input_file, 'r') as input_file:
#         names = input_file.read().splitlines()

#     with open(output_file_name, 'w') as output_file:
#         for name in names:
#             output_file.write(name + "\n")
#             abbreviations = generate_abbreviations(name, letter_values)
#             best_abbreviations = choose_best_abbreviations(abbreviations)
#             formatted_abbrevs = ' '.join([f"{abbr}({score})" for abbr, score in best_abbreviations.items()])
#             output_file.write(formatted_abbrevs + "\n" if formatted_abbrevs else "\n")

# def main():
#     input_file = input("Enter the name of the input file (with .txt extension): ")
#     file_name = input_file.split('.')[0]
#     values_file = 'values.txt'

#     letter_values = read_letter_values(values_file)
#     generate_output(file_name, input_file, letter_values)

# if __name__ == "__main__":
# main()


# from ogee import main, read_letter_values


# def compute_score(position, letter, letter_values):
#     if position == 'first':
#         return 0
#     elif position == 'last':
#         return 20 if letter == 'E' else 5
#     else:
#         position_value = {'second': 1, 'third': 2}.get(position, 3)
#         commonness_values = {
#             'Q': 1, 'Z': 1, 'J': 3, 'X': 3, 'K': 6, 'F': 7, 'H': 7, 'V': 7, 'W': 7, 'Y': 7,
#             'B': 8, 'C': 8, 'M': 8, 'P': 8, 'D': 9, 'G': 9, 'L': 15, 'N': 15, 'R': 15, 'S': 15, 'T': 15,
#             'O': 20, 'U': 20, 'A': 25, 'I': 25, 'E': 35
#         }
#         return position_value + commonness_values.get(letter, 0)

# def generate_abbreviations(name, letter_values):
#     words = [word.upper() for word in name.split() if word.isalpha()]
#     abbreviations = set()

#     for word in words:
#         if len(word) >= 3:
#             for i in range(len(word) - 2):
#                 abbreviation = word[i:i+3]
#                 if len(set(abbreviation)) == 3:  # Ensure distinct letters in the abbreviation
#                     score = compute_score(
#                         'first' if i == 0 else 'other' if i + 2 < len(word) - 1 else 'last',
#                         abbreviation[1], letter_values)
#                     abbreviations.add((abbreviation, score))

#     return abbreviations


# def choose_best_abbreviations(abbreviations):
#     best_abbreviations = {}
#     for abbreviation, score in abbreviations:
#         if abbreviation[1:] not in best_abbreviations or best_abbreviations[abbreviation[1:]] > score:
#             best_abbreviations[abbreviation[1:]] = score

#     return {abbr: score for abbr, score in abbreviations if best_abbreviations[abbr[1:]] == score}

# def generate_output(file_name, input_file, letter_values):
#     output_file_name = f"ikeee_trees_abbrevs.txt"
#     with open(input_file, 'r') as input_file:
#         names = input_file.read().splitlines()

#     with open(output_file_name, 'w') as output_file:
#         for name in names:
#             output_file.write(name + "\n")
#             abbreviations = generate_abbreviations(name, letter_values)
#             best_abbreviations = choose_best_abbreviations(abbreviations)
#             formatted_abbrevs = ' '.join([f"{abbr}({score})" for abbr, score in best_abbreviations.items()])
#             output_file.write(formatted_abbrevs + "\n" if formatted_abbrevs else "\n")

#     def main():
#         input_file = input("Enter the name of the input file (with .txt extension): ")
#     file_name = input_file.split('.')[0]
#     values_file = 'values.txt'

#     letter_values = read_letter_values(values_file)
#     generate_output(file_name, input_file, letter_values)

# if __name__ == "__main__":
#     main()



# def read_letter_values(file):
#     letter_values = {}
#     with open(file, 'r') as values_file:
#         for line in values_file:
#             letter, value = line.split()
#             letter_values[letter] = int(value)
#     return letter_values

# def compute_score(position, letter, letter_values):
#     positions = {'first': 0, 'second': 1, 'third': 2}
#     values = {'Q': 1, 'Z': 1, 'J': 3, 'X': 3, 'K': 6, 'F': 7, 'H': 7, 'V': 7, 'W': 7, 'Y': 7,
#               'B': 8, 'C': 8, 'M': 8, 'P': 8, 'D': 9, 'G': 9, 'L': 15, 'N': 15, 'R': 15, 'S': 15, 'T': 15,
#               'O': 20, 'U': 20, 'A': 25, 'I': 25, 'E': 35}
    
#     score = 0
#     if position == 'first':
#         return 0
#     elif position == 'last':
#         return 20 if letter == 'E' else 5
#     else:
#         return positions.get(position, 3) + values.get(letter, 0)

# def generate_abbreviations(name, letter_values):
#     words = [word.upper() for word in name.split() if word.isalpha()]
#     abbreviations = set()

#     for word in words:
#         if len(word) >= 3:
#             for i in range(len(word) - 2):
#                 abbreviation = word[i:i+3]
#                 if len(set(abbreviation)) == 3:  
#                     score = compute_score(
#                         'first' if i == 0 else 'second' if i == 1 else 'third',
#                         abbreviation[1], letter_values)
#                     abbreviations.add((abbreviation, score))

#     return abbreviations

# def choose_best_abbreviations(abbreviations):
#     best_abbreviations = {}
#     for abbreviation, score in abbreviations:
#         if abbreviation[1:] not in best_abbreviations or best_abbreviations[abbreviation[1:]] > score:
#             best_abbreviations[abbreviation[1:]] = score

#     return {abbr: score for abbr, score in abbreviations if best_abbreviations[abbr[1:]] == score}

# def generate_output(file_name, input_file, letter_values):
#     output_file_name = f"ikeee_trees_abbrevs.txt"
#     with open(input_file, 'r') as input_file:
#         names = input_file.read().splitlines()

#     with open(output_file_name, 'w') as output_file:
#         for name in names:
#             output_file.write(name + "\n")
#             abbreviations = generate_abbreviations(name, letter_values)
#             best_abbreviations = choose_best_abbreviations(abbreviations)
#             formatted_abbrevs = ' '.join([f"{abbr}({score})" for abbr, score in best_abbreviations.items()])
#             output_file.write(formatted_abbrevs + "\n" if formatted_abbrevs else "\n")

# def main():
#     input_file = 'trees.txt'  
#     values_file = 'values.txt'  
#     letter_values = read_letter_values(values_file)
#     generate_output('ikeee', input_file, letter_values)  

# if __name__ == "__main__":
#     main()

