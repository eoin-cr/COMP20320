# Note: I believe this is the way congestion windows are calculated, but I may have made a mistake.
# however, it lines up to the solution for question 6 from the problem set.

def calculator(i, num, transmission_size, mss):
    num_from_timeout = 1
    while i <= num + 1:
        if mss * 2 ** (num_from_timeout - 1) > threshold:
            if transmission_size < threshold:
                transmission_size = threshold
            else:
                transmission_size += mss
        else:
            transmission_size = mss * 2 ** (num_from_timeout - 1)
        if num_from_timeout != 1:
            print(f'Congestion Window is {i - 1}: {transmission_size}kB')
        if i != (num + 1):
            print(f'Transmission {i}: {transmission_size}kB,', end=" ")
        i += 1
        num_from_timeout += 1
    return transmission_size


print("For the inputs just enter the ints, do not enter the kB")

# Takes inputs
mss_inp = int(input("Enter the MSS: "))
threshold = int(input("Enter the threshold: "))
num_inp = int(input("Enter the number of transmissions: "))
timeout_inp = int(input("If there is a timeout, enter which transmission it occured on, otherwise enter -1: "))

transmission_size_outer = 0
if timeout_inp != -1:
    threshold = calculator(1, timeout_inp, transmission_size_outer, mss_inp) / 2
    calculator(timeout_inp + 1, num_inp, transmission_size_outer, mss_inp)
else:
    calculator(1, num_inp, transmission_size_outer, mss_inp)
