from bitstring import BitArray

def hextobit(hexstr):
	bitcode = ''
	intv = int(hexstr, base = 16)
	bitcode = str(bin(intv))[2:].zfill(32)
	return bitcode


def format_classifier(bitstr):

	if bitstr[-7:] == "0110011":
		instr = R_format(bitstr)
		return instr
	elif bitstr[-7:] == "0010011":
		instr = I1_format(bitstr)
		return instr
	elif bitstr[-7:] == "0000011":
		instr = I2_format(bitstr)
		return instr
	elif bitstr[-7:] == "0100011":
		instr = S_format(bitstr)
		return instr
	elif bitstr[-7:] == "1100011":
		instr = B_format(bitstr)
		return instr
	elif bitstr[-7:] == "1101111":
		instr = J_format(bitstr)
		return instr
	elif bitstr[-7:] == "1100111":
		instr = J1_format(bitstr)
		return instr
	elif bitstr[-7:] == "0110111":
	    instr = U_format(bitstr)
	    return instr
	else:
	    print("INVALID OPCODE")
	    return 0

def R_format(bitstr):

	if(bitstr[17:20] == '000' and bitstr[0:7] == '0000000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'add'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	elif(bitstr[17:20] == '000' and bitstr[0:7] == '0100000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'sub'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	elif(bitstr[17:20] == '100' and bitstr[0:7] == '0000000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'xor'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	elif(bitstr[17:20] == '110' and bitstr[0:7] == '0000000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'sub'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	elif(bitstr[17:20] == '111' and bitstr[0:7] == '0000000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'sub'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	elif(bitstr[17:20] == '001' and bitstr[0:7] == '0000000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'sub'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	elif(bitstr[17:20] == '101' and bitstr[0:7] == '0000000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'sub'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	elif(bitstr[17:20] == '101' and bitstr[0:7] == '0100000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'sub'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	elif(bitstr[17:20] == '010' and bitstr[0:7] == '0000000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'sub'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	elif(bitstr[17:20] == '011' and bitstr[0:7] == '0000000'):
		reg2 = 'x'+ str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		rd = 'x'+str(int(bitstr[20:25],2))
		inst = 'sub'
		output = inst + " " + rd + "," + reg1 + "," + reg2
		return output
	else:
		print("Invalid Hexcode")
		return 0


def I1_format(bitstr):

	if bitstr[17:20] == "000":
		imm = str(BitArray(bin = bitstr[:12]).int)
		rd = 'x' + str(int(bitstr[20:25],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = 'addi'
		output = inst + " " + rd + "," + reg1 + "," + imm
		return output
	elif bitstr[17:20] == "100":
		imm = str(BitArray(bin = bitstr[:12]).int)
		rd = 'x' + str(int(bitstr[20:25],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = 'xori'
		output = inst + " " + rd + "," + reg1 + "," + imm
		return output
	elif bitstr[17:20] == "110":
		imm = str(BitArray(bin = bitstr[:12]).int)
		rd = 'x' + str(int(bitstr[20:25],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = 'ori'
		output = inst + " " + rd + "," + reg1 + "," + imm
		return output
	elif bitstr[17:20] == "111":
		imm = str(BitArray(bin = bitstr[:12]).int)
		rd = 'x' + str(int(bitstr[20:25],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = 'andi'
		output = inst + " " + rd + "," + reg1 + "," + imm
		return output
	elif bitstr[17:20] == "001":
		imm = str(int(bitstr[:6],16))
		rd = 'x' + str(int(bitstr[20:25],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = 'slli'
		output = inst + " " + rd + "," + reg1 + ", " + imm
		return output
	elif bitstr[17:20] == "101" and bitstr[6:12] == "000000":
		imm = str(int(bitstr[:6],16))
		rd = 'x' + str(int(bitstr[20:25],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = 'srli'
		output = inst + " " + rd + "," + reg1 + ", " + imm
		return output
	elif bitstr[17:20] == "101" and bitstr[6:12] == "100000":
		imm = str(int(bitstr[:6],16))
		rd = 'x' + str(int(bitstr[20:25],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = 'srai'
		output = inst + " " + rd + "," + reg1 + ", " + imm
		return output
	elif bitstr[17:20] == "010":
		imm = str(BitArray(bin = bitstr[:12]).int)
		rd = 'x' + str(int(bitstr[20:25],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = 'slti'
		output = inst + " " + rd + "," + reg1 + ", " + imm
		return output
	elif bitstr[17:20] == "011":
		imm = str(BitArray(bin = bitstr[:12]).int)
		rd = 'x' + str(int(bitstr[20:25],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = 'sltiu'
		output = inst + " " + rd + "," + reg1 + ", " + imm
		return output
	else:
		print("Invalid Hexcode")
		return 0



def I2_format(bitstr):
	if bitstr[17:20] == "000":
		imm = str(BitArray(bin = bitstr[:12]).int)
		reg1 = '(x' + str(int(bitstr[12:17], 2)) + ')'
		rd = 'x' + str(int(bitstr[20:25], 2))
		inst = 'lb'
		output = inst + " " + rd + "," + imm + reg1
		return output
	elif bitstr[17:20] == "001":
		imm = str(BitArray(bin = bitstr[:12]).int)
		reg1 = '(x' + str(int(bitstr[12:17], 2)) + ')'
		rd = 'x' + str(int(bitstr[20:25], 2))
		inst = 'lh'
		output = inst + " " + rd + "," + imm + reg1
		return output
	elif bitstr[17:20] == "010":
		imm = str(BitArray(bin = bitstr[:12]).int)
		reg1 = '(x' + str(int(bitstr[12:17], 2)) + ')'
		rd = 'x' + str(int(bitstr[20:25], 2))
		inst = 'lw'
		output = inst + " " + rd + "," + imm + reg1
		return output
	elif bitstr[17:20] == "011":
		imm = str(BitArray(bin = bitstr[:12]).int)
		reg1 = '(x' + str(int(bitstr[12:17], 2)) + ')'
		rd = 'x' + str(int(bitstr[20:25], 2))
		inst = 'ld'
		output = inst + " " + rd + "," + imm + reg1
		return output
	elif bitstr[17:20] == "100":
		imm = str(BitArray(bin = bitstr[:12]).int)
		reg1 = '(x' + str(int(bitstr[12:17], 2)) + ')'
		rd = 'x' + str(int(bitstr[20:25], 2))
		inst = 'lbu'
		output = inst + " " + rd + "," + imm + reg1
		return output
	elif bitstr[17:20] == "101":
		imm = str(BitArray(bin = bitstr[:12]).int)
		reg1 = '(x' + str(int(bitstr[12:17], 2)) + ')'
		rd = 'x' + str(int(bitstr[20:25], 2))
		inst = 'lhu'
		output = inst + " " + rd + "," + imm + reg1
		return output
	elif bitstr[17:20] == "110":
		imm = str(BitArray(bin = bitstr[:12]).int)
		reg1 = '(x' + str(int(bitstr[12:17], 2)) + ')'
		rd = 'x' + str(int(bitstr[20:25], 2))
		inst = 'lwu'
		output = inst + " " + rd + "," + imm + reg1
		return output
	else:
		print("Invalid Hexcode")
		return 0






def S_format(bitstr):
	if bitstr[17:20] == "000":
		imm = bitstr[0:7] + bitstr[20:25]
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12], 2))
		reg1 = "(x" + str(int(bitstr[12:17], 2)) + ")"
		inst = 'sb'
		output = inst + " " + reg2 + "," + imm + reg1
		return output
	elif bitstr[17:20] == "001":
		imm = bitstr[0:7] + bitstr[20:25]
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12], 2))
		reg1 = "(x" + str(int(bitstr[12:17], 2)) + ")"
		inst = 'sh'
		output = inst + " " + reg2 + "," + imm + reg1
		return output
	elif bitstr[17:20] == "010":
		imm = bitstr[0:7] + bitstr[20:25]
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12], 2))
		reg1 = "(x" + str(int(bitstr[12:17], 2)) + ")"
		inst = 'sw'
		output = inst + " " + reg2 + "," + imm + reg1
		return output
	elif bitstr[17:20] == "011":
		imm = bitstr[0:7] + bitstr[20:25]
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12], 2))
		reg1 = "(x" + str(int(bitstr[12:17], 2)) + ")"
		inst = 'sd'
		output = inst + " " + reg2 + "," + imm + reg1
		return output
	else:
		print("Invalid Hexcode")
		return 0


def B_format(bitstr):
	if bitstr[17:20] == "000":
		imm = bitstr[0] + bitstr[24] + bitstr[1:7] + bitstr[20:24] + '0'
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = "beq"
		output = inst + " " + reg2 + "," + reg1 + "," + imm
		return output
	elif bitstr[17:20] == "001":
		imm = bitstr[0] + bitstr[24] + bitstr[1:7] + bitstr[20:24] + '0'
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = "bne"
		output = inst + " " + reg2 + "," + reg1 + "," + imm
		return output
	elif bitstr[17:20] == "100":
		imm = bitstr[0] + bitstr[24] + bitstr[1:7] + bitstr[20:24] + '0'
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = "blt"
		output = inst + " " + reg2 + "," + reg1 + "," + imm
		return output
	elif bitstr[17:20] == "101":
		imm = bitstr[0] + bitstr[24] + bitstr[1:7] + bitstr[20:24] + '0'
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = "bge"
		output = inst + " " + reg2 + "," + reg1 + "," + imm
		return output
	elif bitstr[17:20] == "110":
		imm = bitstr[0] + bitstr[24] + bitstr[1:7] + bitstr[20:24] + '0'
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = "bltu"
		output = inst + " " + reg2 + "," + reg1 + "," + imm
		return output
	elif bitstr[17:20] == "111":
		imm = bitstr[0] + bitstr[24] + bitstr[1:7] + bitstr[20:24] + '0'
		imm = str(BitArray(bin = imm).int)
		reg2 = 'x' + str(int(bitstr[7:12],2))
		reg1 = 'x' + str(int(bitstr[12:17],2))
		inst = "bgeu"
		output = inst + " " + reg2 + "," + reg1 + "," + imm
		return output

	else:
		print("Invalid Hexcode")
		return 0


def J_format(bitstr):
	imm = bitstr[0] + bitstr[12:20] + bitstr[11] + bitstr[1:11]
	imm = str(BitArray(bin = imm).int)
	rd = 'x' + str(int(bitstr[20:25], 2))
	inst = "jal"
	output = inst + " " + rd + "," + imm
	return output

def J1_format(bitstr):
	if bitstr[17:20] == "000":
		imm = str(BitArray(bin = bitstr[:12]).int)
		reg1 = '(x' + str(int(bitstr[12:17], 2)) + ')'
		rd = 'x' + str(int(bitstr[20:25], 2))
		inst = "jalr"
		output = inst + " " + rd + "," + imm + reg1
		return output
	else:
		print("invalid Hexcode")
		return 0


def U_format(bitstr):
	imm = str(hex(int(bitstr[:20], 2)))
	rd = 'x' + str(int(bitstr[20:25], 2))
	inst = 'lui'
	output = inst + " " + rd + "," + imm
	return output

# print("Enter number of Instructions:")
# n = int(input("Enter:"))
allhexcodes = input("Enter instructions:")
# print("Enter Hex codes:")
hexcodes = []
hexcodes = allhexcodes.split()
n = len(hexcodes)
bincodes = []
instructions = []
hexcode1 = []
i = n


for i in range(0, len(hexcodes)):
	hexstr = hexcodes[i]
	if(len(hexstr) != 8):
		print(" Instruction " + hexstr + " is invalid")
		continue
	else:
		binary = hextobit(hexstr)
		s = format_classifier(binary)
		if s:
			hexcode1.append(hexstr)
			bincodes.append(binary)
			instructions.append(s)



ount = 0
for i in range(0, len(instructions)):
    if instructions[i][0:4] == 'jal ':
        temp3 = instructions[i].split(",")
        temp2 = int(temp3[-1])
        temp2 = int(temp2/2)
        if(i + temp2 < len(instructions) and instructions[i + temp2][0:1] != 'L'):
            count = count + 1
            index = 'L' + str(count)
            instructions[i + temp2] = index + ": "+ instructions[i+temp2]
            temp3[-1] = index
            instructions[i] = temp3[0] + ", " + temp3[-1]
        elif(i + temp2 < len(instructions) and instructions[i + temp2][0:1] == 'L'):
            index = 'L' + str(count)
            temp3[-1] = index
            instructions[i] = temp3[0] + ", " + temp3[-1]
        else:
            instructions[i] = instructions[i] + " -- error invalid offset"
    elif(instructions[i][0:4] == 'beq '):
        temp3 = instructions[i].split(",")
        temp2 = int(temp3[-1])
        temp2 = int(temp2/4)
        if(i + temp2 < len(instructions) and instructions[i + temp2][0:1] != 'L'):
            count = count + 1
            index = 'L' + str(count)
            instructions[i + temp2] = index + ": "+ instructions[i+temp2]
            temp3[-1] = index
            instructions[i] = temp3[0] + ", " + temp3[-1]
        elif(i + temp2 < len(instructions) and instructions[i + temp2][0:1] == 'L'):
            index = 'L' + str(count)
            temp3[-1] = index
            instructions[i] = temp3[0] + ", " + temp3[-1]
        else:
            instructions[i] = instructions[i] + "-- error invalid offset"
        

for i in range(0, len(instructions)):
    print(instructions[i])


