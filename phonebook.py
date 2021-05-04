#!/usr/bin/env python3
import requests, json, sys, os


HOME = os.getenv('HOME')


def get_mails(target):
	data = '{"term":"' + target + '","maxresults":10000,"media":0,"target":2,"terminate":[null],"timeout":20}'

	f = json.loads(requests.post('https://public.intelx.io/phonebook/search?k=c7ca2255-89d1-4b9f-bc88-97fe781dd631', data=data).text)['id']
	res = json.loads(requests.get('https://public.intelx.io/phonebook/search/result?k=c7ca2255-89d1-4b9f-bc88-97fe781dd631&id={}&limit=50000'.format(f)).text)

	with open(HOME + '/Recon/tmp/mail_pb.txt', 'w') as output:
		for r in res['selectors']:
			output.write(r['selectorvalue'] + '\n')


if __name__ == '__main__':
	get_mails(sys.argv[1])