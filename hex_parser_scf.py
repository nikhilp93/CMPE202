import codecs
import os

with open ( '/Users/nprathap/scfprogram/SCFFile.tlv','rb') as tlv:
	parsed_out = tlv.read().hex()
	#print(parsed_out)
#function to call for converting hexadecimal length to decimal value
def hex_to_dec(hex1): 
	out = int(hex1,16)
	return out

print("####################################################################################\n")
print("####################################################################################\n")
print("####################################################################################\n")

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
			#print('Rest of the output to be parsed for SCF body is: ', parsed_out_body)
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

print("####################################################################################\n")
print("####################################################################################\n")
print("####################################################################################\n")

#Parsing SCF body
while parsed_out_body!="":
	print("Iterations")
	print("####################################################################################\n")
	print("####################################################################################\n")


	for i in range(1,11):

		type=parsed_out_body[:2]
		parsed_out_body=parsed_out_body[2:]
		print("type"+str(i)+"is: ",type)

		hex_length=parsed_out_body[:4]
		#print(length1)
		dec_length= hex_to_dec(hex_length)
		#print(dec_length1)
		parsed_out=parsed_out[4:]
		print("length of"+str(i)+"is: ", dec_length)

		if type=="0c":
			print("We hit type:0c, End of SCF body\n")
			parsed_out_left = parsed_out_body
			print('Rest of the output not parsed is: ', parsed_out_left)
			break

		else:

			hex_length=parsed_out_body[:4]
			#print(length1)
			dec_length= hex_to_dec(hex_length)
			#print(dec_length1)
			parsed_out_body=parsed_out_body[4:]
			print("length of"+str(i)+"is: ", dec_length)
		
		if type=="02" or type=="03" or type=="04"or type=="05":
		#or type=="09":
		#if i ==4 or i==6 or i==13:
			value=parsed_out_body[:dec_length*2]
			#print(value)
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", value)
			#print(codecs.decode(value, "hex").decode('utf-8'))
			if type == "02":
				print(codecs.decode(value, "hex").decode('utf-8'),"--> Subject DNS name. ")
			elif type == "03":
				print(codecs.decode(value, "hex").decode('utf-8'),"--> Subject name ")
			elif type == "04":
				print(codecs.decode(value, "hex").decode('utf-8'),"--> Subject function/role ")
			elif type == "05":
				print(codecs.decode(value, "hex").decode('utf-8'),"--> Subject certificate issuer name ")
			#elif type=="09":
			#	print(codecs.decode(value, "hex").decode('utf-8'),"--> --> Subject X509.v3 certificate ")
			
			
		elif type=="01":
			value=parsed_out_body[:dec_length*2]
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", hex_to_dec(value), "--> record length")
		elif type=="06":
			value=parsed_out_body[:dec_length*2]
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", value, "--> Subject certificate serial number")
		elif type=="07":
			value=parsed_out_body[:dec_length*2]
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", value, "--> Subject public key")
		elif type=="08":
			value=parsed_out_body[:dec_length*2]
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", value, "--> Subject certificate signature")
		elif type=="09":
			value=parsed_out_body[:dec_length*2]
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", value, "--> Subject X509.v3 certificate")
		elif type=="0a":
			value=parsed_out_body[:dec_length*2]
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", hex_to_dec(value), "--> Subject IP address")
		elif type=="0b":
			value=parsed_out_body[:dec_length*2]
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", hex_to_dec(value), "--> Hash of certificate")
		elif type=="0c":
			value=parsed_out_body[:dec_length*2]
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", hex_to_dec(value), "--> Hash algorithm")
		else:
			value=parsed_out_body[:dec_length*2]
			#print(value)
			parsed_out_body=parsed_out_body[dec_length*2:]
			print("value of"+str(i)+"is: ", value)

