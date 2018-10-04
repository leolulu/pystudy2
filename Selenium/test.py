import requests

headers = {
    "Cookie": "PHPSESSID=d4hpo7ichjm4q32csdnjh41lt3; kt_ips=144.34.159.126; kt_tcookie=1; kt_is_visited=1; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1538636347; _ga=GA1.2.1826467013.1538636349; _gid=GA1.2.566159732.1538636349; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1538636364",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

r = requests.get(
    'http://pornscum.com/get_file/1/668c9882189990e9a237ab52baa31c87aab9fb712e/17000/17169/17169.mp4/?rnd=1538636358266',
    headers = headers

)

print(r.content)