import os
import copy
import math
import numpy as np


def toggle_bits(key, b, i):
    if b <= 8:
        key[i] = key[i] ^ int("1"*b, 2)
        return key
    else:
        num_byte = math.ceil(b/8)
        t = b
        for j in range(num_byte):
            if(t>8):
                mask = '1'*8
                t -= 8
            else:
                mask = '1'*t
                
            key[i+j] = key[i+j] ^ int(mask, 2)

        return key


p_lens = [2**i for i in range(1, 9)]

for plain_text_len in p_lens:

    # Generate a random key of size 256 bye
    # key = bytearray(os.urandom(key_len))
    # print(key)

    with open("key", "rb") as f:
        key = bytearray(f.read())

    os.system(f"./a.out key {plain_text_len}")

    br = bytearray()

    with open("bytes", "rb") as f:
        # print(f.read())
        br = bytearray(f.read())

# Toggle 1 bit
    for b in range(1, 33):
        R = []
        # key2 = copy.copy(key)
        

        for t in range(20):
            key2 = copy.copy(key)
            
            # print(key2[t])
            # print()

            # toggle b bits in key
            toggle_bits(key2, b, t)
            
            with open("key2", "wb") as f:
                f.write(key2)
            
            # print(key2[t])
            # exit(0)
            
            os.system(f"./a.out key2 {plain_text_len}")

            br2 = bytearray()

            with open("bytes", "rb") as f:
                # print(f.read())
                br2 = bytearray(f.read())

            bin_str = ''
            for i in range(len(br)):
                # br2[i] = br[i] ^ br2[i]
                bin_str += format(br[i] ^ br2[i], '08b')

            count = [0 for i in range(256)]

            # print(bin_str)
            for i in range(len(bin_str)-7):
                # print(bin_str[i:i+8], end=" ")
                # print(int(bin_str[i:i+8], 2), end=" ")
                count[int(bin_str[i:i+8], 2)] += 1

            # print(count)
            # print(len(count) - count.count(0))
            r = (np.std(count) * len(count))/(len(bin_str)-7)
            # print(f'sd = {np.std(count)}\t r = {r}')
            R.append(r)
            
        # print(R)
        with open("result/data", "a") as f:
            f.write(f'{b},{np.mean(R)}\n')


# # ------------------------------------
#             for i in range(16):
#                 # Filp 19rd (say) bit in the key to get a new key
#                 key2[j] = key2[j] ^ (1 << k)

#                 print(key_len, j, k, sep="\t")
#                 k = (k+1) % 8
#                 j = (j+1) % (key_len-1)

#                 with open("key2", "wb") as f:
#                     f.write(key2)

#                 # # key2 = copy.copy(key)
#                 # with open("key2", "rb") as f:
#                 #     # f.write(key2)
#                 #     key2 = bytearray(f.read())
#                 # key2[2] = key2[2] ^ ((1 << 5) | 1<<3)

#                 # with open("key2", "wb") as f:
#                 #     f.write(key2)

#                 os.system(f"./a.out key2 {key_len} plain_text")

#                 br2 = bytearray()

#                 with open("bytes", "rb") as f:
#                     # print(f.read())
#                     br2 = bytearray(f.read())

#                 bin_str = ''
#                 for i in range(len(br)):
#                     br2[i] = br[i] ^ br2[i]
#                     bin_str += format(br2[i], '08b')

#                 count = [0 for i in range(256)]

#                 # print(bin_str)
#                 for i in range(len(bin_str)-7):
#                     # print(bin_str[i:i+8], end=" ")
#                     # print(int(bin_str[i:i+8], 2), end=" ")
#                     count[int(bin_str[i:i+8], 2)] += 1

#                 # print(count)
#                 # print(len(count) - count.count(0))
#                 r = (np.std(count) * len(count))/len(bin_str)
#                 # print(f'sd = {np.std(count)}\t r = {r}')
#                 R.append(r)

#             # print(R)
#             with open("result/"+str(key_len), "w") as f:
#                 f.write(",".join(str(l) for l in R))
