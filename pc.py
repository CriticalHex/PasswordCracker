import time

u_in = list(input("Enter a PIN: "))
pin_range = range(len(u_in))
for i, c in enumerate(u_in):
    u_in[i] = ord(c)
guess = list((32 for val in pin_range))
start = time.perf_counter()
while 1:
    if guess == u_in:
        end = time.perf_counter()
        break
    guess[0] += 1
    for i in pin_range:
        if guess[i] % 127 == 0:
            guess[i+1] += 1
            guess[i] = 32
pin = ""
for c in u_in:
    pin += chr(c)
print(end-start, pin)