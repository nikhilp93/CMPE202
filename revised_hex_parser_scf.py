"""Parser .tlv"""
import codecs

with open('/Users/nprathap/scfprogram/SCFFile.tlv', 'rb')as tlv:
    PARSED_OUT = tlv.read().hex()
    # print(parsed_out)
# function to call for converting hexadecimal length to decimal value
def hex_to_dec(hex1):
    out = int(hex1, 16)
    return out

print("####################################################################################\n")
print("####################################################################################\n")
print("####################################################################################\n")

# Parsing SCF header
for i in range(1, 17):
    if i == 3 or i == 7 or i == 9:
        stype = PARSED_OUT[:2]
        PARSED_OUT = PARSED_OUT[2:]
        print("stype" + str(i) + "is: ", stype)
        hex_length = PARSED_OUT[:4]
        # print(length1)
        dec_length = hex_to_dec(hex_length)
        # print(dec_length1)
        PARSED_OUT = PARSED_OUT[4:]
        print("length of" + str(i) + "is: ", dec_length)
    else:
        stype = PARSED_OUT[:2]
        PARSED_OUT = PARSED_OUT[2:]
        print("stype" + str(i) + "is: ", stype)

        if stype == "0d":
            print("We hit stype:0d, End of SCF header\n")
            parsed_out_body = PARSED_OUT
            # print('Rest of the output to be parsed for SCF body is: ', parsed_out_body)
        else:
            hex_length = PARSED_OUT[:4]
            # print(length1)
            dec_length = hex_to_dec(hex_length)
            # print(dec_length1)
            PARSED_OUT = PARSED_OUT[4:]
            print("length of" + str(i) + "is: ", dec_length)
        if stype == "04" or stype == "06" or stype == "0e":
            # if i ==4 or i==6 or i==13:
            value = PARSED_OUT[:dec_length*2]
            # print(value)
            PARSED_OUT = PARSED_OUT[dec_length*2:]
            print("value of" + str(i) + "is: ", value)
            print(codecs.decode(value, "hex").decode('utf-8'))

        else:
            value = PARSED_OUT[:dec_length*2]
            # print(value)
            PARSED_OUT = PARSED_OUT[dec_length*2:]
            print("value of" + str(i) + "is: ", value)

print("####################################################################################\n")
print("####################################################################################\n")
print("####################################################################################\n")

# Parsing SCF body
while parsed_out_body != "":
    print("Iterations")
    print("####################################################################################\n")
    print("####################################################################################\n")
    # import itertools
    # for i in itertools.count():
    # if time.time() - start >= timeout:
    # break
    for i in range(1, 11):
        stype = parsed_out_body[:2]
        parsed_out_body = parsed_out_body[2:]
        print("stype" + str(i) + "is: ", stype)

        hex_length = parsed_out_body[:4]
        # print(length1)
        dec_length = hex_to_dec(hex_length)
        # print(dec_length1)
        PARSED_OUT = PARSED_OUT[4:]
        print("length of" + str(i) + "is: ", dec_length)

        if stype == "0c":
            print("We hit stype:0c, End of SCF body\n")
            parsed_out_left = parsed_out_body
            print('Rest of the output not parsed is: ', parsed_out_left)
        else:

            hex_length = parsed_out_body[:4]
            # print(length1)
            dec_length = hex_to_dec(hex_length)
            # print(dec_length1)
            parsed_out_body = parsed_out_body[4:]
            print("length of" + str(i) + "is: ", dec_length)
        if stype == "02" or stype == "03" or stype == "04"or stype == "05":
            # or stype=="09":
            # if i ==4 or i==6 or i==13:
            value = parsed_out_body[:dec_length * 2]
            # print(value)
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", value)
            # print(codecs.decode(value, "hex").decode('utf-8'))
            if stype == "02":
                print(codecs.decode(value, "hex").decode('utf-8'), "--> Subject DNS name. ")
            elif stype == "03":
                print(codecs.decode(value, "hex").decode('utf-8'), "--> Subject name ")
            elif stype == "05":
                print(codecs.decode(value, "hex").decode('utf-8'),
                      "--> Subject certificate issuer name ")
            # elif stype=="09":
            # print(codecs.decode(value, "hex").decode('utf-8'),
            # "--> --> Subject X509.v3 certificate ")
        elif stype == "04":
            print("value of" + str(i) + "is:", value, "--> Subject function/role ")
        elif stype == "01":
            value = parsed_out_body[:dec_length * 2]
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", hex_to_dec(value), "--> record length")
        elif stype == "06":
            value = parsed_out_body[:dec_length * 2]
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", hex_to_dec(value),
                  "--> Subject certificate serial number")
        elif stype == "07":
            value = parsed_out_body[:dec_length * 2]
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", value, "--> Subject public key")
        elif stype == "08":
            value = parsed_out_body[:dec_length * 2]
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", value, "--> Subject certificate signature")
        elif stype == "09":
            value = parsed_out_body[:dec_length * 2]
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", value, "--> Subject X509.v3 certificate")
        elif stype == "0a":
            value = parsed_out_body[:dec_length * 2]
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", hex_to_dec(value), "--> Subject IP address")
        elif stype == "0b":
            value = parsed_out_body[:dec_length * 2]
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", hex_to_dec(value), "--> Hash of certificate")
        elif stype == "0c":
            value = parsed_out_body[:dec_length*2]
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", hex_to_dec(value), "--> Hash algorithm")
        else:
            value = parsed_out_body[:dec_length * 2]
            # print(value)
            parsed_out_body = parsed_out_body[dec_length * 2:]
            print("value of" + str(i) + "is: ", value)
