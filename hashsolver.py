def MD5(hsh):
	with open("MD5_hashed.txt", "r", errors = "ignore") as f:
		count = 0
		for line in f.readlines():
			count+=1
			line = line.strip()
			if hsh == line:
				break
		f.close()

	with open("passwords.txt.", "r", errors = "ignore") as f:
		print("password: ")
		passw = f.readlines()
		print(passw[count])
def SHA1(hsh):
	count = 0
	with open("SHA1_hashed.txt", "rb") as f:
		for line in f.readlines():
			print(line)
			count+=1
			line = line.strip()
			x = int(hsh, 16)
			y = int(line, 16)
			if x == y:
				break
	with open("passwords.txt", "r", errors = "ignore") as f:
		print ("password : ")
		passw = f.readlines()
		print(passw[count])




def menu():

	hshtext = input("Hash: ")
	print("""
	1.MD5
	2.SHA1


		""")
	menu_ = int(input(": "))
	if menu_ == 1:
		MD5(hshtext)
	elif menu_ == 2:
		SHA1(hshtext)

while True:
	menu()
