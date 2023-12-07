import subprocess


def parse(query):
    data = subprocess.check_output(['nslookup', query]).decode('utf-8')
        
    ipv4s = list()
    ipv6s = list()
    
    for line in data.split('\n'):
        if line.startswith("Address"):
            address = line.split()[-1]
            if '#' in address: continue
            if any([x.isalpha() for x in address]):
                ipv6s += [address]
            else:
                ipv4s += [address]
                    
    return ipv4s, ipv6s
