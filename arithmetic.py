import ar_ex
import sys


file_name = "results.txt"
limit = 5
mark = 0
counter = 0
level = ar_ex.difficulty()

while counter < limit:
    task = ar_ex.generate_task(level)
    print(task)
    while True:
        try:
            user_answer = float(input())
        except ValueError:
            print("Incorrect format.")
            print(task)
        else:
            counter += 1
            if user_answer == ar_ex.calculate(expression=task, dif=level):
                print("Right!")
                mark += 1
            else:
                print("Wrong!")
            break

print(f"Your mark is {mark}/{limit}.")
scr = f"{mark}/{limit}"
ar_ex.save_mark(filename=file_name, score=scr, dif=level)
sys.exit()
