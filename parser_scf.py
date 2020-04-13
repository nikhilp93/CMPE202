import codecs
import os

with open('/Users/nprathap/scfprogram/CMPE202/SCFFile.txt', 'r') as file1:
    out1=file1.read()
    out2 = out1.replace(" ","")
    parsed_out = out2.replace("\n","")

#print(parsed_out)

#function to call for converting hexadecimal length to decimal value
def hex_to_dec(hex1): 
	out = int(hex1,16)
	return out

#Parsing SCF header
for i in range(1,17):
	if i==3 or i==7 or i==9:
		type=parsed_out[:2]
		parsed_out=parsed_out[2:]
		print("type"+str(i)+"is: ",type)

		hex_length=parsed_out[:4]
		#print(length1)
		dec_length= hex_to_dec(hex_length)
		#print(dec_length1)
		parsed_out=parsed_out[4:]
		print("length of"+str(i)+"is: ", dec_length)

	else:
		
		
		type=parsed_out[:2]
		parsed_out=parsed_out[2:]
		print("type"+str(i)+"is: ",type)

		if type=="0d":
			print("We hit type:0d, End of SCF header\n")
			parsed_out_body = parsed_out
			print('Rest of the output to be parsed for SCF body is: ', parsed_out_body)
			break

		else:

			hex_length=parsed_out[:4]
			#print(length1)
			dec_length= hex_to_dec(hex_length)
			#print(dec_length1)
			parsed_out=parsed_out[4:]
			print("length of"+str(i)+"is: ", dec_length)
		
		if type=="04" or type=="06" or type=="0e":
		#if i ==4 or i==6 or i==13:
			value=parsed_out[:dec_length*2]
			#print(value)
			parsed_out=parsed_out[dec_length*2:]
			print("value of"+str(i)+"is: ", value)
			print(codecs.decode(value, "hex").decode('utf-8'))
		else:
			value=parsed_out[:dec_length*2]
			#print(value)
			parsed_out=parsed_out[dec_length*2:]
			print("value of"+str(i)+"is: ", value)
"""
#Parsing SCF body
for i in range(1,13):
	if i==3 or i==7 or i==9:
		type=parsed_out[:2]
		parsed_out=parsed_out[2:]
		print("type"+str(i)+"is: ",type)

		hex_length=parsed_out[:4]
		#print(length1)
		dec_length= hex_to_dec(hex_length)
		#print(dec_length1)
		parsed_out=parsed_out[4:]
		print("length of"+str(i)+"is: ", dec_length)

	else:
		
		
		type=parsed_out[:2]
		parsed_out=parsed_out[2:]
		print("type"+str(i)+"is: ",type)

		if type=="0d":
			print("We hit type:0d, End of SCF header\n")
			parsed_out_body = parsed_out
			print('Rest of the output to be parsed for SCF body is: ', parsed_out_body)
			break

		else:

			hex_length=parsed_out[:4]
			#print(length1)
			dec_length= hex_to_dec(hex_length)
			#print(dec_length1)
			parsed_out=parsed_out[4:]
			print("length of"+str(i)+"is: ", dec_length)
		
		if type=="04" or type=="06" or type=="0e":
		#if i ==4 or i==6 or i==13:
			value=parsed_out[:dec_length*2]
			#print(value)
			parsed_out=parsed_out[dec_length*2:]
			print("value of"+str(i)+"is: ", value)
			print(codecs.decode(value, "hex").decode('utf-8'))
		else:
			value=parsed_out[:dec_length*2]
			#print(value)
			parsed_out=parsed_out[dec_length*2:]
			print("value of"+str(i)+"is: ", value)
"""

