from pathlib import Path

path = Path("salary.txt")

def total_salary(path):
    try:
        with open(path, "r") as sal:
            total_salary = 0
            count = 0
            for person in sal:
                salary = person.split(",")[-1]
                count += 1
                total_salary += int(salary)
    except FileNotFoundError:
        return None, None
    average = total_salary / count
    return total_salary, average

print(total_salary(path))