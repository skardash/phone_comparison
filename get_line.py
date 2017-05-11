# get map of code -> state
codes = {}
with open("area_code.csv", "r") as ins:
	for line in ins:
		splt = line.split()
		txt = splt[1]
		for i in range(2,len(splt)):
			txt += " " + splt[i]
		codes[splt[0]] = txt

# print codes
# deal with phone formatting

def format_phone(ph):
	return ph.replace("+","").replace("-","").replace("(","").replace(")","").replace(" ", "").replace("\n", "")

def get_code(ph):
	phf = format_phone(ph)
	if (phf[0] == "1"):
		return phf[1:4]
	else:
		return phf[0:3]


ph1 = "+1-541-754-3010"
ph2 = "1-541-754-3010"
ph3 = "(541)   754-3010"

# print codes[get_code(ph1)]

with open("list.csv", "r") as ins:
	cnt = 1
	found = False
	for line in ins:
		# print "line is " + line
		# print "cnt = " + str(cnt)
		splt = line.split(",")
		if (len(splt) >= 3):
			cdA = get_code(splt[0])
			cdB = get_code(splt[1])
			cdC = get_code(splt[2])
	        # print cdA + "/" + cdB + "/" + cdC
			if (codes[cdA] != codes[cdB]):
				if (codes[cdA] == codes[cdC]): 
					print("row # is " +  str(cnt) + ", phones A and C belong to " + codes[cdC] + " state.")
					found = True
					break
				elif (codes[cdB] == codes[cdC]):
					print("row # is " +  str(cnt) + ", phones B and C belong to " + codes[cdC] + " state.")
					found = True
					break
		cnt += 1

	if (not found):
		print("no such row in the file")
	# print "cnt = " + str(cnt)