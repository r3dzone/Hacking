#hexview_ELF_PE.py
import sys 
import os

file_name = sys.argv[1] 
f = open(file_name,"r") 
opened = f.read() 

count = 0 
line = "" 
orig = "" 
garo = 16 
sero = 30 

view = garo * sero 

FileSig = [ #file MagicNumbers DB
	"CAFEBABE" ,
	"CAFED00D",
	"474946383961",
	"474946383761",
	"FFD8",
	"89504E470D0A1A0A",
	"4D546864",
	"2321",
	"7f454c46",
	"2521",
	"25504446"
	"4D5A",
	"5A4D",
	"19540119",
	"011954",
	"55AA",
	"4A6F7921",
	"49492A00",
	"4D4D002A",
	"FEFF",
	"FFFE",
	"EFBBBF",
	"D0CF11E0",
	"504B",
	"377ABCAF271C"
]

SigName = [ #signature name DB
	"Compiled Java class files OR Mach-O binaries",
	"Compiled Java class file with Pack200",
	"GIF image files",
	"GIF image files",
	"JPEG image file",
	"PNG image file ",
	"Standard MIDI audio files",
	"Unix or Linux scripts",
	"ELF executables",
	"PostScript files",
	"PDF Document files",
	"DOS MZ,Windows PE Executable files",
	"dosZMXP, a non-PE EXE Executable files",
	"The Berkeley Fast File System superblock format",
	"The Berkeley Fast File System superblock format",
	"The Master Boot Record of bootable storage devices",
	"PEF(Preferred Executable Format) the classic Mac OS and BeOS for PowerPC executable file",
	"TIFF(tagged Image File Format) image file",
	"Unicode text files",
	"Unicode text files",
	"Unicode text files",
	"Microsoft Compound File Binary Format",
	"ZIP lossless data compression files",
	"7z data compression files"

	
]
def header(): 

	headhex = "" 
	print "="*garo*5 
	print "["+" "*(garo*2)+"UT's HEX_VIEWER"+" "*(garo*2)+"]" 
	for i in range(16):
		headhex += str(hex(i))+" " 
		
	print " "*8 + "\t" + headhex 
	print "="*garo*5 

def helper(): 
	print "="*garo*5 
	msg = "" 
	msg += "ENTER:binary_down\t" 
	msg += "u:binary_up\t" 
	msg += "s:search_address\n"
	msg += "f:file_information\t"
	print msg 

def signature(): 
	global opened 
	msg = "" 

	for i in range(8): 
		msg += opened[i].encode("hex")  
	
	for i in range(len(FileSig)):
		if FileSig[i] in msg: #ELF
			print SigName[i]
			showObject(getSignatureDB(FileSig[i])) 

def showObject(obj):

	for val in obj.keys():
		print val+": " + str(obj[val])


def getSignatureDB(magicnum): 
	
	db = { "Bit": None, "Endian" : None, "Machine" : None, } 
	
	if magicnum == "7f454c46": #ELF

		bit = subviewer(4,1) 
		endian = subviewer(5,1)
		machine = subviewer(18,1) 

		#bit
		if bit == "01": 
			db['Bit'] = 32 
	
		elif bit == "02":
			db['Bit'] = 64 
	
		#endian 
		if endian == "01": 
			db['Endian'] = "little" 
		elif endian == "02": 
			db['Endian'] = "big" 

		#machine 
		if machine == "00": 
			db['Machine'] = "NULL" 
		elif machine == "02": 
			db['Machine'] = "SPARC" 
		elif machine == "03": 
			db['Machine'] = "x86" 
		elif machine == "08": 
			db['Machine'] = "MIPS" 
		elif machine == "14": 
			db['Machine'] = "POWER-PC" 
		elif machine == "2a": 
			db['Machine'] = "super-H"
		elif machine == "32": 
			db['Machine'] = "IA-64" 
		elif machine == "3e": 
			db['Machine'] = "x86-64" 
		elif machine == "b7": 
			db['Machine'] = "ARM-64" 
		elif 1 :
			db['Machine'] = "unknown" 
	
	return db 

def viewer(count): 
	global opened 
	global line 
	global orig 
#	os.system('cls') # windows
	os.system('clear') # linux, mac
	header()

	for i in range(view): 
		line += opened[count].encode("hex") + "  " 

		if (ord(opened[count]) > 33) and (ord(opened[count]) < 126): 
			orig += opened[count] 
		else: 
			orig += "." 
	
		count += 1
 
		if count % garo == 0 and count != 0 : 
			print "%8s\t" %str(hex(count-16))+str(line) + "|" + str(orig) 
			line = "" 
			orig = "" 

def subviewer(start,size): 

	global opened 
	msg = "" 

	for i in range(start, start+size): 
		msg += opened[i].encode("hex") 

	return msg 
	viewer(0) 
	count += 1 

	
#main================================================================================================
while 1 : 
	helper() 
	inchr = raw_input() 

	if inchr == "u": 
		count -= 2 
		viewer(count * view) 
		count += 1 

	if inchr == "f": 
		signature() 

	if inchr == "" :
		viewer(count * view) 
		count += 1 

	if inchr == "s":
		count = input("input address what want to searach! : ") 
		viewer(int(count)) 
		count /= view 
		count += 1