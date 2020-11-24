from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# Podriamos usar dos o una linea, como?
in_file = open(from_file)
indata = in_file.read()

print(f"El input file es {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ahora, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Muy bien, bien echo.")

out_file.close()
in_file.close()
