# -*- coding: utf-8 -*-
import hashlib
import json
import random
import requests
import socket
import struct
import time
from datetime import datetime

class NEONAPI(object):
	def __init__(self):
		self.s=requests.Session()
		self.s.headers.update({'fp':'46c76e34e0d5fc1575688d27ea81822c45f29681','X-PmangPlus-Platform':'iOS','locale':'en_GB','Accept-Language':'en-gb','Content-Type':'application/x-www-form-urlencoded','ver':'5','User-Agent':'PmangPlus SDK 1.8 190326 (iOS,10.2,iPad Air2/WiFi/Cellular,Apple,Viettel,(null))','ts':'1554649030478'})
		self.s.verify=False
		self.udid=self.rndDeviceId()
		self.appkey='Y2NjMjYwMzg5MjE1ZWVmZWI4NzUxNzllYWU5ODNiZjg'
		self.os_ver=self.getOS()
		self.device_cd=self.getDevice()
		
	def setUdid(self,udid):
		self.udid=udid
		
	def getOS(self):
		return random.choice(['10.2','11.1','12.1'])
		
	def getDevice(self):
		return random.choice(['IPAD','IPHONE'])
		
	def getTs(self):
		return str(long(time.time()*1000))
		
	def genRandomIP(self):
		return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		
	def rndHex(self,n):
		return ''.join([random.choice('0123456789ABCDEF') for x in range(n)])
		
	def rndDeviceId(self):
		return '%s-%s-%s-%s-%s'%(self.rndHex(8),self.rndHex(4),self.rndHex(4),self.rndHex(4),self.rndHex(12))
		
	def digest(self,ts):
		hash_object = hashlib.sha1('%s%s'%(ts,self.appkey))
		return hash_object.hexdigest()
		
	def auto_login(self):
		ts=self.getTs()
		r=self.s.post('http://www.neonapi.com/api/accounts/v3/global/connect/auto_login',data='locale=en_GB&app_id=653&app_ver=1.0&os_ver=%s&jailbreak_yn=N&udid=%s&app_key=bea72cd3561b8b59447ac0333212faba&device_cd=%s&app_secret=Y2NjMjYwMzg5MjE1ZWVmZWI4NzUxNzllYWU5ODNiZjg&local_cd=ENG'%(self.os_ver,self.udid,self.device_cd),headers={'ts':ts,'fp':self.digest(ts)})
		return json.loads(r.content)
		
	def login(self):
		ts=self.getTs()
		r=self.s.post('http://www.neonapi.com/api/accounts/v3/global/login',data='privacy_yn=Y&app_id=653&callTime=%s&provider=&ad_night_yn=Y&ad_yn=Y&mob_svc_yn=Y&thread_name=%s.537&app_key=bea72cd3561b8b59447ac0333212faba&locale=en_GB&device_cd=%s&app_secret=Y2NjMjYwMzg5MjE1ZWVmZWI4NzUxNzllYWU5ODNiZjg&local_cd=ENG&os_ver=%s&app_ver=1.0&jailbreak_yn=N&udid=%s'%(ts,datetime.now().strftime('%Y%m%d%H%M.%S'),self.device_cd,self.os_ver,self.udid),headers={'ts':ts,'fp':self.digest(ts)})
		if 'error_message_detail' in r.content:
			self.log('banned')
			exit(1)
		return json.loads(r.content)
		
if __name__ == "__main__":
	n=NEONAPI()
	n.auto_login()
	n.login()