binary = input()  # The input string.
bins = ''.join(['0' if b == '?' else b for b in binary ])


for i in range(2**len(binary)):
    for i, d in enumerate(binary):
        inc = binary.count('?',i)
        bins = [str(n) for n in bins]
        if d != '?':
            print(d, end='')
        else:
            print(bins[inc-i-1], end='')
        bins = int(''.join(bins), 2)
        bins += 1
        bins = bin(bins)[2:]
    print()
        
