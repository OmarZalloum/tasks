import sys, requests
from datetime import datetime

def ip_info(api_key, ip_address):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"

    header = {
        "x-apikey": api_key
    }

    res = requests.get(url,headers=header)

    try:
        data = res.json()
    except:
        print("error here")
        return

    if 'data' in data:

        data_ip = data['data']
        attr = data_ip.get('attributes', {})
        owner = attr.get('as_owner', 'N/A')
        last_analysis_date = attr.get('last_analysis_date', 'N/A')
        last_analysis_date = datetime.utcfromtimestamp(last_analysis_date).strftime('%Y-%m-%d %H:%M:%S')
        last_analysis_stats = attr.get('last_analysis_stats', {})  


        print(f"IP Address: {ip_address}")
        print(f"Owner: {owner}")
        print(f"Last Analysis Date: {last_analysis_date}")
        print(f"Number of Rates: {last_analysis_stats}")
    else:
        print(f"{ip_address} not found please check agian")



key = "5a6408ea560248c52ae9331dd721d826b88ac7350b75556bee0180ba4ba94485"
ip = sys.argv[1]
ip_info(key, ip)
