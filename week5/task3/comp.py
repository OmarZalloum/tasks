import hashlib, os, subprocess

def secret (name, outfile, infile):
    password = hashlib.md5(name.encode()).hexdigest()
    #you can uncomment the next line to view the passwords
    #print(f"{name}: {password}")
    cmd = ['zip', '--password', password, outfile, infile]
    devnul = open(os.devnull)
    subprocess.run(cmd, check=True, stdout=devnul, stderr=devnul)
    pass


file = open('myname.txt', 'r')
print(f"My Name is ==> {file.read()}")


secret_file= 'secret.txt'
file2 = open('names.txt', 'r')
line = file2.readline().strip()  
names = line.split()  
#print(names[1])
for name in names:
    zipf = f'{name}.zip'
    secret(name, zipf, secret_file)

    print(f"Compressed {secret_file} to {zipf}")
    secret_file= zipf  