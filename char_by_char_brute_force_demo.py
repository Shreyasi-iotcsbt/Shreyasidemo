import os
from random import randint
import time

pas = input("Send the password:")

keys = list("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=~`[]{}|;:',.<>?/")

pwg = ["_"] * len(pas)
attempts = 0
start_time = time.time()

for i in range(len(pas)):
    while pwg[i] != pas[i]:
        pwg[i] = keys[randint(0, len(keys) - 1)]
        attempts += 1
        if attempts % 500 == 0:  # only redraw occasionally, avoids slowdown
            os.system("cls")
            print("".join(pwg))
            print("attacking....pls wait!")

os.system("cls")
end_time = time.time()
total_time = end_time - start_time

print(f"Password found: {''.join(pwg)}")
print(f"Total attempts: {attempts}")
print(f"Time taken: {total_time:.2f} seconds")