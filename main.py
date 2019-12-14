#!/usr/bin/python3
import sys
import os
import re
import subprocess
import datetime
autorun = "True"
compiler = "g++"
files = []
flags = []
streaks_compile = []
output = "output.o"
rm_after_run = "true"
arguments = []
banner = "Kevin Agusto. Program for automating compile and run c++/c/dll"
filetemp0 = "run.command"
filetemp1 = "run.format"
time_measure=False
show_command = False
if (len(sys.argv) <= 1):
 print(banner)
 sys.exit(0)

def ltos(listnya):
 to_return = ""
 for i in listnya:
  to_return += i + " "
 return to_return

def compile():
	to_exec = "{compiler} {flags} {files} -o {output}".format(compiler=compiler, flags = ltos(flags), files=ltos(files), output = output)
	os.system(to_exec)
	os.system("chmod 777 %s" %(output))
	os.system("./%s %s" %(output, ltos(arguments)))
	if (rm_after_run=="true"):
		try: 
			os.system("rm %s" %(output[0]))
		except FileNotFoundError:
			pass

def streaks(angka):
 output = []
 with open(filetemp0, "r+") as reader:
  dataa = reader.read()
  data = dataa.split("\n\n\n")[angka].split("\t")
  for i in range(len(data)-1):
   os.system(data[i])
   output.append(data[i].split(" -o ")[1].split(" ")[0])
  os.system("chmod 777 %s" %(output[-1]))
  if (autorun=="True"):
   os.system("./%s %s" %(output[-1], ltos(arguments)))
  try:
   if (rm_after_run=="false"):
    os.system("rm %s" %(output[0]))
  except FileNotFoundError:
   pass 
def rmstreaks(angka):
 if angka=="all":
  os.remove(filetemp0)
  return
 angka = int(angka)
 with open(filetemp0, "r+") as reader:
  data = reader.read().strip("\n\n\n").split("\n\n\n")
  with open(filetemp0, "w+") as writer:
   for i in range(len(data)):
    if (i==angka):
     continue
    writer.write(data[i] + "\n\n\n")

def printstreaks():
 with open(filetemp0, "r+") as reader:
  print(reader.read())

def formatted_run(f, c):
 if (not len(c)):
  print("Need replacement...")
  return
 if (len(c)!=f.count("{}")):
  d = []
  for i in range(f.count("{}")):
   d.append(c[0])
  c = d	
 #f = f.replace("{}", "'{}'")
 x = 'global y;y = "{f}";y=y.format('.format(f=f)
 for i in range(len(c)):
  x+='\''+str(c[i])+'\''
  if (i==len(c)-1):
   break
  x+=", "
 x+=")"
 exec(x)
 if (show_command):
  print("command: %s"%(y))
 try:
  a = datetime.datetime.now()
  os.system(y)  
  #i dont want newline addtion
  # o = (subprocess.check_output(y, shell=True)).decode("utf-8").split("\n")
  # for i in range(len(o)):
  #  print(o[i], end="")
  #  if (i!=(len(o)-1)):
  #   print("\n", end="")
 except Exception as error:
  pass
  #print(error)
 b = datetime.datetime.now()
 if (time_measure):
  print("%s%s%s%s"%("-"*5, "Time Measuring", "-"*5, "\nTime Eplased: %s\nStart Time: %s\nEnd Time: %s\n"%(str(b-a), str(a), str(b) )))
 

def formatted_run_list(i, c):
 i = int(i)
 with open(filetemp1, "r") as baca:
  formatted_run(baca.read().strip("\n\n\n").split("\n\n\n")[i], c)

def add_formatted_run(f):
 with open(filetemp1, "a+") as yay:
  yay.write(f+"\n\n\n")

for i in range(len(sys.argv)):
 if (sys.argv[i]=="-as"):
  with open(filetemp0, "a+") as writer:
   writer.write(commands + "\n\n\n")
 elif (sys.argv[i]=="-s"):
  show_command=True
 elif (sys.argv[i]=="-t"):
  time_measure=True
 elif (sys.argv[i]=="-fr"):
  formatt = sys.argv[i+1]
  core = sys.argv[i+2:]
  formatted_run(formatt, core)
  sys.exit(0)
 elif (sys.argv[i]=="-afr"):
  add_formatted_run(sys.argv[i+1])
  sys.exit(0)
 elif (sys.argv[i]=="-frl"):
  num = sys.argv[i+1]
  core = sys.argv[i+2:]
  formatted_run_list(num, core)
  sys.exit(0)
 elif (sys.argv[i]=="-ps"):
  printstreaks()
  sys.exit(0)
 elif (sys.argv[i]=="-rms"):
  rmstreaks((sys.argv[i+1]))
  sys.exit(0)
 elif (sys.argv[i]=="-ar"):
  autorun = (sys.argv[i+1])
  continue
 elif (sys.argv[i]=="-s"):
  streaks(int(sys.argv[i+1]))
  sys.exit(0)
 elif (sys.argv[i]=="-f"):
  files.append(sys.argv[i+1])
  continue
 elif (sys.argv[i]=="-c"):
  compiler = sys.argv[i+1]
  continue
 elif (sys.argv[i]=="-o"):
  output = sys.argv[i+1]
  continue
 elif (sys.argv[i]=="-rm"):
  rm_after_run = sys.argv[i+1]
  continue
 elif (sys.argv[i]=="-a"):
  arguments.append(sys.argv[i+1])
  continue
 elif (sys.argv[i]=="-fl"):
  flags.append(sys.argv[i+1])
  continue

compile()
