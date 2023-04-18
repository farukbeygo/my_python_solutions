import math
import pandas as pd
import matplotlib.pyplot as plt


def create_sequence(length):
    sequence = []
    prime_sequence = []
    for num in range(1, length):
        sequence.append(2 ** num - 1)
        if is_prime(2 ** num - 1):
            prime_sequence.append("prime")
        else:
            prime_sequence.append("non-prime")

    return sequence, prime_sequence


def is_prime(number):
    if number >= 2:
        limit = round(math.sqrt(number))
        for num in range(2, limit):
            if number % num == 0:
                return False
        return True
    else:
        return False


data_raw = create_sequence(55)
data_sequence = {'number': data_raw[0],
                 'prime_value': data_raw[1]}

data_frame = pd.DataFrame(data_sequence)
data_frame.to_csv('sequence_data.csv', index=False)


plt.scatter(data_raw[0], data_raw[1], alpha=0.3)


plt.show()
