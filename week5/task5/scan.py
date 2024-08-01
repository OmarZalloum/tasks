import socket, argparse, ipaddress

def check(ip, port):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False, f"Ip: {ip} is Invalid\nPlease enter a valid Ip address. "
    
    if not (0 <= port <= 65535):
        return False, f"Port {port} is invalid.\nPort must be between 0 and 65535. Please enter a valid port."
    
    return True, ""

def scanner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(e)
        return False

def output(ip, port, is_open, output_file =None):
    result = f"Ip: {ip} is {'open' if is_open else 'closed'} on port: {port}"
    if output_file:
        with open(output_file, 'a') as file:
            file.write(result+ '\n')
    else:
        print(result) 



par = argparse.ArgumentParser(description="port scanner")
par.add_argument('ip', type=str, help='IP address to scan')
par.add_argument('port', type=int, help="Port number to scan")
par.add_argument('-o', '--output', type=str, help="Output file to write the result", default=None)

args = par.parse_args()
ip = args.ip
port = args.port
output_file = args.output

print(f"Scanning {ip} on port: {port}")
valid, msg = check(ip, port)
if valid:
    is_open = scanner(ip, port)
    output(ip,port, is_open, output_file)
else:
    print(msg)


