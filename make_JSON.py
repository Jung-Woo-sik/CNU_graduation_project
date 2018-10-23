from idaapi import *
import md5
import json

#CopyRight jhy7185	2016.9.08 20:00

#get Mnemonic value at current ea	
def getMnemString(ea):
	mtempString = GetDisasm(ea)
	mtempString = mtempString.split()
	checkString = mtempString[0]
	if checkString == "call" or checkString == "jmp":
		checkString = "nop"
	
	return checkString

#get Hex value at current ea	
def getHexStirng(ea):
	htempString = hex(GetOriginalByte(ea))
	htempString = htempString[2:]
	if len(htempString) == 1:
		htempString = "0" + htempString
	
	return htempString
	

def getHash(funcea,endea):
	i = 0
	asmString = ""
	mnemString = ""
	hexString = ""
		
	#get Strings from idb
	while funcea + i < endea :
		#gather current function's asm, mnemonic, hex value
		asmString += GetDisasm(funcea+i)
		mnemString += getMnemString(funcea+i)+ " "
		hexString += getHexStirng(funcea+i)
		i += 1
	
	#MD5 incoding
	input_asm_hash = md5.md5(asmString).hexdigest()
	input_mnemonic_hash = md5.md5(mnemString).hexdigest()
	input_hex_hash = md5.md5(hexString).hexdigest()
	
	return input_asm_hash,input_mnemonic_hash,input_hex_hash


def make_json():
	func_Name =""
	input_asm_hash = ""
	input_mnemonic_hash = ""
	input_hex_hash = ""
	
	exe_fname = get_input_file_path()
	
	#pgm =dict();
	
	#try:
	#	pgm['OpenSource'] = raw_input("OpenSource Name : ")
	#except EOFError:
	#	print ('Write your OpenSource Name')
	#try:
	#	pgm['version'] = raw_input("OpenSource version : ")
	#except EOFError:
	#	print ('Write your OpenSource version')
	
	data_list = list()	
	
	# Get current ea
	ea = get_screen_ea()
	
	# Get segment class
	seg = getseg(ea)
	
	# Loop from segment start to end
	func = get_next_func(seg.startEA)
	seg_end = seg.endEA
	
	
	
	
	while func is not None and func.startEA < seg_end:
		
		funcea = func.startEA
		endea = func.endEA
		func_Name = GetFunctionName(funcea)
		
		#get current function's mnemonic & hex hash value
		input_asm_hash,input_mnemonic_hash,input_hex_hash=getHash(funcea,endea)
				
		#next function 
		func = get_next_func(funcea)
		
		data_list.append({'name':func_Name,'asm':input_asm_hash, 'mnem':input_mnemonic_hash,'hex':input_hex_hash})
	
	#pgm['list']= data_list
	
	with open(exe_fname + '_info.json', 'w') as f:
		json.dump(data_list, f)		
make_json()