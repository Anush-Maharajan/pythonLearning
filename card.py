card = input("K card ho tapai ko?\n")
if card == "gold":
	print("YOu have 30% dis")
elif card == "silver":
	age = int(input("Tapai ko age k ho ni?\n"))
	if age > 60:
		print("25% dis")
	else:
		print("20% dis")
else:
	print("5% ids")

	