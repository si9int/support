import requests
import sys
import os


API = 'https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data'
HOME = os.getenv('HOME')


def perform_lookup(ip):
    res = requests.get(API, headers={'X-Forwarded-For': ip}).text
    with open(HOME + '/Recon/tmp/location/{}.json'.format(ip), 'w') as output:
        output.write(res)


if __name__ == '__main__':
    try:
        ip = sys.argv[1]
        perform_lookup(ip)
    except IndexError:
        print('[X] Usage: python3 geoip.py <ip-address>')
        exit(0)