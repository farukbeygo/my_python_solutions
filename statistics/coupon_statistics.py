import math
import random
import numpy as np


def mean(coupon_number):
    h_number = 0
    for num in range(1, coupon_number + 1):
        h_number += (1/num)
    coupon_mean = coupon_number * h_number
    return coupon_mean


def variance(coupon_number):
    series_number = 0
    for num in range(1, coupon_number + 1):
        series_number += (1 / num**2)
    coupon_variance = coupon_number**2 * series_number
    return coupon_variance


def standart_deviation(coupon_number):
    return math.sqrt(variance(coupon_number))


def error(coupon_number):
    try:
        return standart_deviation(coupon_number)/coupon_number
    except ZeroDivisionError:
        print("Coupon number cannot be zero.")


def find_coupon(coupon_number):
    coupon_list = []
    for coupon in range(1, 1 + coupon_number):
        coupon_list.append(coupon)

    prob_list = []
    trail = 0
    while len(prob_list) < coupon_number:
        trail += 1
        chosen_coupon = random.choice(coupon_list)
        if chosen_coupon not in prob_list:
            prob_list.append(chosen_coupon)
    return trail


num_of_simulations = 200000
trail_numbers = []

for i in range(num_of_simulations):
    trail = find_coupon(20)
    trail_numbers.append(trail)


mean_X = np.mean(trail_numbers)
sd_X = np.std(trail_numbers)
se_mean = sd_X / num_of_simulations

print("Estimated expected value of X:", mean_X)
print("Estimated standard deviation of X:", sd_X)
print("Estimated standard error of the sample mean:", se_mean)


print(mean(20))
print(standart_deviation(20))

print(29.294 - 29.289)
print(11.238 - 12.448)