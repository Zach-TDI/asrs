from smbus import SMBus
from pylogix import PLC
allenBradley = '192.168.1.3'
#with PLC() as comm:
#	comm.IPAddress = allenBradley
#	ret = comm.Read('MyTagName')
#	print(ret.TagName, ret.Value, ret.Status)

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

numb = 1

#print ("Enter a hex 1 to B to designate what position you wish to move to ")
while numb == 1:

	jakesStepper = input(">>>>   ")

	if jakesStepper == "0":
		bus.write_byte(addr, 0x0) # move to position home
	elif jakesStepper == "1":
		bus.write_byte(addr, 0x1) # move to Red
	elif jakesStepper == "2":
		bus.write_byte(addr, 0x2) # move to Green
	elif jakesStepper == "3":
		bus.write_byte(addr, 0x3) # move to Blue
	elif jakesStepper == "0":
		bus.write_byte(addr, 0x4) # move to position home
	elif jakesStepper == "1":
		bus.write_byte(addr, 0x5) # move to Red
	elif jakesStepper == "2":
		bus.write_byte(addr, 0x6) # move to Green
	elif jakesStepper == "3":
		bus.write_byte(addr, 0x7) # move to Blue
	elif jakesStepper == "0":
		bus.write_byte(addr, 0x8) # move to position home
	elif jakesStepper == "1":
		bus.write_byte(addr, 0x9) # move to Red
	elif jakesStepper == "2":
		bus.write_byte(addr, 0xA) # move to Green
	elif jakesStepper == "3":
		bus.write_byte(addr, 0xB) # move to Blue
	else:
		numb = 0






