from smbus import SMBus
from pylogix import PLC
allenBradley = '192.168.1.3'
#with PLC() as comm:
#	comm.IPAddress = allenBradley
#	ret = comm.Read('MyTagName')
#	print(ret.TagName, ret.Value, ret.Status)

addr = 0x8 # Jakes bus address
#addr2 = 0xF # Zachs bus address
bus = SMBus(1) # indicates /dev/ic2-1

numb = 1

print ("Enter a hex 1 to B to designate what position you wish to move to ")
while numb == 1:

	jakesStepper = input(">>>>   ")

	if jakesStepper == "0":
		bus.write_byte(addr, 0x0) # move from 0 - 1
	elif jakesStepper == "1":
		bus.write_byte(addr, 0x1) # move from 0 - 2
	elif jakesStepper == "2":
		bus.write_byte(addr, 0x2) # move from 0 - 3
	elif jakesStepper == "3":
		bus.write_byte(addr, 0x3) # move from 1 - 0
	elif jakesStepper == "4":
		bus.write_byte(addr, 0x4) # move from 1 - 2
	elif jakesStepper == "5":
		bus.write_byte(addr, 0x5) # move from 1 - 3
	elif jakesStepper == "6":
		bus.write_byte(addr, 0x6) # move from 2 - 0
	elif jakesStepper == "7":
		bus.write_byte(addr, 0x7) # move from 2 - 1
	elif jakesStepper == "8":
		bus.write_byte(addr, 0x8) # move from 2 - 3
	elif jakesStepper == "9":
		bus.write_byte(addr, 0x9) # move from 3 - 0
	elif jakesStepper == "A":
		bus.write_byte(addr, 0xA) # move from 3 - 1
	elif jakesStepper == "B":
		bus.write_byte(addr, 0xB) # move from 3 - 2
	else:
		numb = 0






