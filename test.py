import hashlib
import os
import subprocess

def read_name_from_file(filename):
    with open(filename, 'r') as file:
        name = file.readline().strip()  # Read the first line and strip the newline character
    return name

def compress_file(input_filename, output_filename, password):
    # Use the zip command to create a password-protected zip file
    cmd = ['zip', '--password', password, output_filename, input_filename]
    subprocess.run(cmd, check=True)

def main():
    # Step 1: Read and print your name
    my_name = read_name_from_file('myname.txt')
    print(f"My Name is ==> {my_name}")

    # Step 2: Read names from names.txt and compress secret file
    secret_filename = 'secret.txt'
    with open('names.txt', 'r') as names_file:
        line = names_file.readline().strip()  # Read the single line and strip the newline character
        names = line.split()  # Split the line into individual names based on spaces

    for name in names:
        md5_password = hashlib.md5(name.encode()).hexdigest()
        output_filename = f'{name}.zip'
        compress_file(secret_filename, output_filename, md5_password)
        print(f"Compressed {secret_filename} to {output_filename} with password {md5_password}")
        secret_filename = output_filename  # Next iteration uses the previous output

if __name__ == '__main__':
    main()
