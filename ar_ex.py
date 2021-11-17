import random


def calculate(expression, dif):
    # Calculates an easy expression passed as a string
    if dif == 1:
        expression = expression.split()

        if expression[1] == '+':
            output = int(expression[0]) + int(expression[2])
            return output
        elif expression[1] == '-':
            output = int(expression[0]) - int(expression[2])
            return output
        else:
            output = int(expression[0]) * int(expression[2])
            return output
    else:
        output = int(expression)**2
        return output


def generate_task(dif):
    # Generates a simple arithmetic task
    if dif == 1:
        a = str(random.randint(2, 9))
        b = str(random.randint(2, 9))
        operator = random.choice([' * ', ' + ', ' - '])

        task = a + operator + b
        return task
    else:
        task = str(random.randint(11, 29))
        return task


def difficulty():
    # Asks for difficulty level.
    while True:
        try:
            print("Which level do you want? Enter a number:")
            print("1 - simple operations with numbers 2-9\n"
                  "2 - integral squares of 11-29")
            dif = int(input())
            if dif not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Incorrect format.")
        else:
            break
    return dif


def save_mark(filename, score, dif):
    # Asks if user wants to save his mark to a file and saves it.
    dif1 = "simple operations with numbers 2-9"
    dif2 = "integral squares of 11-29"
    print("Would you like to save your result to the file? yes/no:")
    while True:
        """
        save = input().lower()
        if save in ['yes', 'y']:
            name = input("Username: ")
            with open(filename, 'a', encoding='utf-8') as file:
                line = f"{name}: {score} in level {dif} ("
                if dif == 1:
                    line = line + f"{dif1}).\n"
                else:
                    line = line + f"{dif2}).\n"
                file.write(line)
                print(f"The results are saved in {filename}.")
                file.close()
        else:
            exit()
        """
        try:
            save = input().lower()
            if save not in ['yes', 'no', 'y', 'n']:
                raise ValueError
        except ValueError:
            print("Incorrect format. Try again. yes/no:")
        else:
            if save in ['yes', 'y']:
                name = input("Username: ")
                with open(filename, 'a', encoding='utf-8') as file:
                    line = f"{name}: {score} in level {dif} ("
                    if dif == 1:
                        line = line + f"{dif1}).\n"
                    else:
                        line = line + f"{dif2}).\n"
                    file.write(line)
                    print(f"The results are saved in {filename}.")
                    file.close()
                    break

