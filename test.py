from subprocess import PIPE, run
from os import listdir, path, system, stat
from sys import exit
import io

assert path.exists("./in_out")
for f in listdir("./in_out"):
  ext = ".txt"
  if f.endswith(ext):
    full_path = "./in_out/" + f
    expected_output_file = full_path[:-len(ext)] + ".out"
    assert path.exists(expected_output_file)
    myinput = open(full_path+".path", "a")
    myinput.write(full_path+"\n")
    myinput.close()
    myinput = open(full_path + ".path")
    p = run(["python3", "q3.py"], stdin=myinput, stdout=PIPE, stderr=PIPE)
    system("rm "+full_path+".path")
    out = (p.stdout + p.stderr).decode('ascii')
    myoutput=open("curr_out", "w+")
    myoutput.write(out)
    myoutput.close()
    system("diff curr_out " + expected_output_file + " > curr_diff")
    if stat("curr_diff").st_size != 0:
      print("MISMATCH IN:", full_path)
      exit()
    else:
      system("rm curr_diff curr_out")
print("!! SUCCESS !!")