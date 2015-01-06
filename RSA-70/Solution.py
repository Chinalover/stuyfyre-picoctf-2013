import math

p = 9648423029010515676590551740010426534945737639235739800643989352039852507298491399561035009163427050370107570733633350911691280297777160200625281665378483
q = 11874843837980297032092405848653656852760910154543380907650040190704283358909208578251063047732443992230647903887510065547947313543299303261986053486569407
e = 65537
c = 83208298995174604174773590298203639360540024871256126892889661345742403314929861939100492666605647316646576486526217457006376842280869728581726746401583705899941768214138742259689334840735633553053887641847651173776251820293087212885670180367406807406765923638973161375817392737747832762751690104423869019034

#Public key:

N = p * q

print("Modulus acquired. Public Exponent = " + str(e))

r = (p - 1) * (q - 1)

ticker = 1
mults = 3
occurences = 0

print("r = " + str(r))
print("Cracking multiples of r...")

while (ticker * r + 1) % e != 0 and occurences != mults:
	ticker += 1
	if (ticker * r + 1) % e == 0:
		occurences += 1

print("Cracked!")
print(str(ticker))
print("K = " + str(ticker * r + 1))

d = (ticker * r + 1) / e

#M = (c ** d) % N

M = pow(c , d , N)

print("M retrieved in decimal encoding!")

MESSAGE = hex(M).replace("L" , "").replace("0x" , "").decode('hex')

print MESSAGE