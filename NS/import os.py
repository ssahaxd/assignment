import os
import copy
import numpy as np


# key_len = 256

Plain_lens = [2**i for i in range(2, 9)]

for key_len in k_lens:
    keys = open(f"key_{key_len}", 'wb')

    # Generate a random key of size 256 bye
    key = bytearray(os.urandom(key_len))
    # print(key)
    keys.write(key)

    with open("key", "wb") as f:
        f.write(key)

    os.system(f"./a.out key {key_len} plain_text")

    br = bytearray()

    with open("bytes", "rb") as f:
        # print(f.read())
        br = bytearray(f.read())

    R = []

    key2 = copy.copy(key)
    j = k = 0

    for i in range(20):
        # Filp 19rd (say) bit in the key to get a new key
        key2[j] = key2[j] ^ (1 << k)
        keys.write(key2)

        print(key_len, j, k, sep="\t")
        k = (k+1) % 8
        j = (j+1) % (key_len-1)

        with open("key2", "wb") as f:
            f.write(key2)

        # # key2 = copy.copy(key)
        # with open("key2", "rb") as f:
        #     # f.write(key2)
        #     key2 = bytearray(f.read())
        # key2[2] = key2[2] ^ ((1 << 5) | 1<<3)

        # with open("key2", "wb") as f:
        #     f.write(key2)

        os.system(f"./a.out key2 {key_len} plain_text")

        br2 = bytearray()

        with open("bytes", "rb") as f:
            # print(f.read())
            br2 = bytearray(f.read())

        bin_str = ''
        for i in range(len(br)):
            br2[i] = br[i] ^ br2[i]
            bin_str += format(br2[i], '08b')

        count = [0 for i in range(256)]

        # print(bin_str)
        for i in range(len(bin_str)-7):
            # print(bin_str[i:i+8], end=" ")
            # print(int(bin_str[i:i+8], 2), end=" ")
            count[int(bin_str[i:i+8], 2)] += 1

        # print(count)
        # print(len(count) - count.count(0))
        r = (np.std(count) * len(count))/len(bin_str)
        # print(f'sd = {np.std(count)}\t r = {r}')
        R.append(r)

    # print(R)
    with open("result/"+str(key_len), "w") as f:
        f.write(",".join(str(l) for l in R))
    f.close()
