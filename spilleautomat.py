from random import randint
from time import sleep

#variabler
teller = 1
total_gevinst = 0
total_tap = 0 
premie = {
	0 : 0, 
	1 : 0, 
	2 : 0, 
	3 : 0, 
	4 : 0, 
	5 : 0.5, 
	6 : 0.5, 
	7 : 1, 
	8 : 2, 
	9 : 5 }

def gevinst(kode, innsats): 
	return innsats * premie [kode];

def spill(innsats): 
	tall = randint (0,9)
	return gevinst(tall, innsats)



penger = int(input("Hvor mye penger har du? "))
innsats = int(input("Hvor mye onsker du å satse per spill? "));

while (penger >= innsats):  
	penger = penger - innsats
	vant = spill(innsats)
	print("Spill nr: ", teller)
	print ("Du vant: ", vant)
	penger = penger + vant
	print ("du har nå: ", penger)
	total_gevinst = total_gevinst + vant
	total_tap = total_tap + innsats
	print ("total gevinst: ", total_gevinst)
	print ("total tap: ", total_tap)
	#tilbakebetalingsprosent = innsats / vant
	if total_gevinst != 0:
		tilbakebetalingsprosent = ((total_gevinst / teller) / innsats) * 100
		print("Tilbakebetalingsprosent: ", int(tilbakebetalingsprosent), " % ")
	else:
		print("Tilbakebetalingsprosent: 0 %")
	print()
	teller = teller + 1
	if (total_tap - total_gevinst) >= 600:
		print("Du har nå tapt det maksimale beløpet for i dag som er 600")
		break
	sleep(3)

	