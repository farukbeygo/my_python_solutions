import random


def calculate_ticket_number(student_number):
    total_ticket = 0
    total_ticket += (student_number * (30/100) * 4)
    total_ticket += (student_number * (25/100) * 3)
    total_ticket += (student_number * (25/100) * 2)
    total_ticket += (student_number * (15/100) * 1)
    return total_ticket


number_of_simulation = 10000
satisfied_number = 0

for i in range(number_of_simulation):
    capacity = random.randint(150, 410)
    if capacity > calculate_ticket_number(150):
        satisfied_number += 1

prob = (satisfied_number/number_of_simulation)

