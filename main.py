# -*- coding: utf-8 -*-
import sys
from crypter import RijndaelEncryptor
from neonapi import NEONAPI
from db import Database
import inspect
import json
import random
import requests
import time
import units
from collections import OrderedDict

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class API(object):
	def __init__(self):
		self.s=requests.Session()
		self.s.headers.update({'Content-Type':'text/json','User-Agent':'global/434 CFNetwork/808.2.16 Darwin/16.3.0','Accept-Language':'en-gb','X-Unity-Version':'2017.4.17f1'})
		self.s.verify=False
		if 'win' in sys.platform:
			self.s.proxies.update({'http': 'http://127.0.0.1:8888','https': 'https://127.0.0.1:8888',})
		self.crypter=RijndaelEncryptor()
		self.key='abcdefghijkrstuv024680wxyzlmnopq'
		self.seq=2
		self.version='1.43.12'
		self.db=Database()
		
	def reroll(self):
		n=NEONAPI()
		n.auto_login()
		token=n.login()
		if 'access_token' in token['value']:
			self.setAccess_token(token['value']['access_token'])
			self.log(token['value']['access_token'])

	def setAccess_token(self,access_token):
		self.access_token=access_token
	
	def setUdid(self,udid):
		n=NEONAPI()
		n.setUdid(udid)
		self.udid=udid
		token=n.login()
		if 'access_token' in token['value']:
			self.setAccess_token(token['value']['access_token'])
			self.log(token['value']['access_token'])
	
	def setRegion(self,region):
		self.region={'global':600,'sg':400,'jp':300,'tw':500,'eu':700}[region.lower()]
		
	def decrypt(self,data):
		return self.crypter.decrypt(data,self.key)
		
	def encrypt(self,data):
		return self.crypter.encrypt(data,self.key)
		
	def getUnitStars(self,id):
		id=str(id)
		return int(units.data[id]['stars'])

	def getUnitName(self,id):
		id=str(id)
		return units.data[id]['name']

	def getUnitType(self,id):
		id=str(id)
		return int(units.data[id]['type'])

	def callAPI(self,data=None,url=None):
		jdata=json.loads(data,object_pairs_hook=OrderedDict)
		if 'version' in jdata:	jdata['version']=self.version
		if 'access_token' in jdata:	jdata['access_token']=self.access_token
		if 'seq' in jdata:	jdata['seq']=str(self.seq)
		if 'pmang_usn' in jdata:	jdata['pmang_usn']=self.access_token.split('|')[0]
		data=json.dumps(jdata,separators=(',', ':'))
		if url:
			r=self.s.post('%s/%s'%(url,inspect.stack()[1][3]),data=self.encrypt(data))
		else:
			r=self.s.post('%s/%s'%(self.game_url,inspect.stack()[1][3]),data=self.encrypt(data))
		self.seq+=1
		decoded_data=self.decrypt(r.content)
		res= json.loads(decoded_data)
		if 'result' in res and res['result'] <>0:
			self.log('%s(): %s'%(inspect.stack()[1][3],res['result']))
		if 'user_id' in res:
			self.log('hello %s:%s'%(res['user_id'],res['owner_index']))
		return res
		
	def log(self,msg):
		try:
			print '[%s] %s'%(time.strftime('%H:%M:%S'),msg.decode().encode('utf-8'))
		except:
			print '[%s] %s'%(time.strftime('%H:%M:%S'),msg.encode('utf-8', 'ignore'))

	def ownerGuildInfo(self,data):
		return self.callAPI(data)

	def mailInvenAllRecv(self,data):
		return self.callAPI(data)

	def itemInvenRandomBoxUse(self,data):
		return self.callAPI(data)

	def userCampaignSeason2List(self,data):
		return self.callAPI(data)

	def userDuelData(self,data):
		return self.callAPI(data)

	def selectFriendList(self,data):
		return self.callAPI(data)

	def connectEventCheck(self,data):
		return self.callAPI(data)

	def selectFriendRequestList(self,data):
		return self.callAPI(data)

	def selectActiveItem(self,data):
		return self.callAPI(data)

	def newStarDuelSwordCheck(self,data):
		return self.callAPI(data)

	def selectBillingDataBasic(self,data):
		return self.callAPI(data)

	def selectPartyRaidHistoryDataList(self,data):
		return self.callAPI(data)

	def userCampaignData(self,data):
		return self.callAPI(data)

	def requestGuildwarDateInfo(self,data):
		return self.callAPI(data)

	def updateCharInvenState(self,data):
		return self.callAPI(data)

	def userCampaignSeason2Data(self,data):
		return self.callAPI(data)

	def loginUser(self,data):
		res= self.callAPI(data)
		if not self.db.getAccount(self.udid):
			self.db.addAccount(self.udid,res['gold'],res['jewelry'],res['level'],res['owner_index'])
		else:
			self.db.updateAccount(self.udid,res['gold'],res['jewelry'],res['level'],res['owner_index'])
		return res

	def userCampaignList(self,data):
		return self.callAPI(data)

	def arenaPhaseInfo(self,data):
		return self.callAPI(data)

	def selectGuildInvitation(self,data):
		return self.callAPI(data)

	def selectHotdeal(self,data):
		return self.callAPI(data)

	def globalDate(self,data):
		return self.callAPI(data)

	def userCampaignStageClear(self,data):
		return self.callAPI(data)

	def userNewStarDuelData(self,data):
		return self.callAPI(data)

	def enterChannel(self,data):
		return self.callAPI(data)

	def missionReward(self,data):
		return self.callAPI(data)

	def userArenaData(self,data):
		return self.callAPI(data)

	def selectItemInven(self,data):
		return self.callAPI(data)

	def checkAttendanceReward(self,data):
		return self.callAPI(data)

	def selectTerritoryUserInfo(self,data):
		return self.callAPI(data)

	def mailInvenRecv(self,data):
		return self.callAPI(data)

	def announce(self,data):
		return self.callAPI(data)

	def webViewEventCheck(self,data):
		return self.callAPI(data)

	def eventDate(self,data):
		return self.callAPI(data)

	def joinUser(self,data):
		return self.callAPI(data)

	def selectBuyLimit(self,data):
		return self.callAPI(data)

	def selectCharInven(self,data,makedeck=False):
		res= self.callAPI(data)
		self.deck_list=set([])
		used=set([])
		forbidden=set([4])
		for unit in res:
			if len(unit)<=2:
				if makedeck:
					if res[unit]['code'] not in used:
						if self.getUnitType(res[unit]['code']) in forbidden:	continue
						if 'Slime Girl' in self.getUnitName(res[unit]['code']):	continue
						print self.getUnitStars(res[unit]['code']),self.getUnitName(res[unit]['code']),self.getUnitType(res[unit]['code']),res[unit]['code']
						self.deck_list.add(res[unit]['inven_index'])
						used.add(res[unit]['code'])
				if self.getUnitStars(res[unit]['code'])>4:
					self.log('%s with: %s*'%(self.getUnitName(res[unit]['code']),self.getUnitStars(res[unit]['code'])))
					if self.getUnitStars(res[unit]['code'])>4:
						if not hasattr(self,'five_stars'):	self.five_stars=0
						self.five_stars+=1
		return res

	def movementCheck(self,data):
		return self.callAPI(data)

	def worldbossUserInfo(self,data):
		return self.callAPI(data)

	def selectFirstPackage(self,data):
		return self.callAPI(data)

	def changeDeviceCertificateCancel(self,data):
		return self.callAPI(data)

	def selectMailInven(self,data):
		return self.callAPI(data)

	def selectModeBeforeSeasonTopInfo(self,data):
		return self.callAPI(data)

	def userCampaignStageStart(self,data):
		return self.callAPI(data)

	def scoutShopBuy(self,data):
		return self.callAPI(data)

	def missionInvenUpdate(self,data):
		return self.callAPI(data)

	def requestSelectImportantNotice(self,data):
		return self.callAPI(data)

	def userRuneModeData(self,data):
		return self.callAPI(data)

	def missionInvenInsert(self,data):
		return self.callAPI(data)

	def changeDeviceCertificate(self,data):
		return self.callAPI(data)

	def selectMissionInven(self,data):
		return self.callAPI(data)

	def selectEquipInven(self,data):
		return self.callAPI(data)

	def selectSoulItemDictionary(self,data):
		return self.callAPI(data)

	def selectSoulItemInven(self,data):
		return self.callAPI(data)

	def selectTerritoryInven(self,data):
		return self.callAPI(data)

	def selectDailyData(self,data):
		return self.callAPI(data)

	def selectDictionary(self,data):
		return self.callAPI(data)

	def selectSavedUserDeckList(self,data):
		return self.callAPI(data)

	def arenaUsableCharSelect(self,data):
		return self.callAPI(data)

	def arenaTournamentInfo(self,data):
		return self.callAPI(data)

	def arenaTournamentCheerInfo(self,data):
		return self.callAPI(data)

	def selectCastleList(self,data):
		return self.callAPI(data)

	def selectLevelUpPackage(self,data):
		return self.callAPI(data)

	def selectReservation(self,data):
		return self.callAPI(data)

	def selectRepeatBuyList(self,data):
		return self.callAPI(data)

	def requestCostumeInvenInfo(self,data):
		return self.callAPI(data)

	def selectShopDiscount(self,data):
		return self.callAPI(data)

	def selectModeTurnCountRecord(self,data):
		return self.callAPI(data)

	def backgroundBattleAllStop(self,data):
		return self.callAPI(data)

	def selectRecoveryLimitList(self,data):
		return self.callAPI(data)

	def checkPmangUsn(self,data):
		return self.callAPI(data)

	def selectVersion(self,data):
		return self.callAPI(data,url='http://mbrowng-glb-maintenance.pmang.cloud')

	def selectServerInfoRequest(self,data):
		res= self.callAPI(data,url='http://mbrowng-glb-maintenance.pmang.cloud')
		for s in res:
			if self.region==res[s]['region']:
				self.game_url=res[s]['game_server_info'][:-1]
				self.log('self.game_url:%s'%(self.game_url))
				break
		return res

	def login(self):
		self.selectVersion('{"seq":"2","market_type":"1"}')
		self.selectServerInfoRequest('{"seq":"3"}')
		self.loginUser('{"seq":"4","market_type":"1","version":"1.38.10","access_token":"251737673|653|IPAD|KR|23a2e656f121dee33353f5d7ec0eb66b729291d6|1554649259248"}')
		self.userCampaignData('{"seq":"5"}')
		self.userCampaignSeason2Data('{"seq":"6"}')
		self.userRuneModeData('{"seq":"7"}')
		self.userCampaignList('{"seq":"8"}')
		self.userCampaignSeason2List('{"seq":"9"}')
		self.selectMissionInven('{"seq":"10"}')
		self.userArenaData('{"seq":"11"}')
		self.userDuelData('{"seq":"12"}')
		self.userNewStarDuelData('{"seq":"13"}')
		self.selectItemInven('{"seq":"14"}')
		self.selectActiveItem('{"seq":"15"}')
		self.selectEquipInven('{"seq":"16"}')
		self.selectSoulItemDictionary('{"seq":"17"}')
		self.selectSoulItemInven('{"seq":"18"}')
		self.selectTerritoryInven('{"seq":"19"}')
		self.selectTerritoryUserInfo('{"seq":"20"}')
		self.selectDailyData('{"seq":"21"}')
		self.enterChannel('{"seq":"22","channel":"0"}')
		self.selectBuyLimit('{"seq":"23"}')
		self.selectDictionary('{"seq":"24"}')
		self.selectSavedUserDeckList('{"seq":"25"}')
		self.arenaPhaseInfo('{"seq":"26"}')
		self.arenaUsableCharSelect('{"seq":"27"}')
		self.arenaTournamentInfo('{"seq":"28"}')
		self.arenaTournamentCheerInfo('{"seq":"29"}')
		self.selectCastleList('{"seq":"30"}')
		self.selectLevelUpPackage('{"seq":"31"}')
		self.selectReservation('{"seq":"32"}')
		self.selectFirstPackage('{"seq":"33"}')
		self.selectRepeatBuyList('{"seq":"34"}')
		self.selectBillingDataBasic('{"seq":"35"}')
		self.requestCostumeInvenInfo('{"seq":"36"}')
		self.selectPartyRaidHistoryDataList('{"seq":"37"}')
		self.selectShopDiscount('{"seq":"38"}')
		self.selectModeTurnCountRecord('{"seq":"39"}')
		self.backgroundBattleAllStop('{"seq":"40"}')
		self.selectRecoveryLimitList('{"seq":"41"}')
		self.selectCharInven('{"seq":"42"}')
		self.globalDate('{"seq":"43"}')
		self.eventDate('{"seq":"44"}')
		self.ownerGuildInfo('{"seq":"45"}')
		self.selectFriendRequestList('{"seq":"46"}')
		self.selectFriendList('{"seq":"47"}')
		self.requestSelectImportantNotice('{"seq":"48","last_index":"0","language_type":"1"}')
		self.selectPartyRaidHistoryDataList('{"seq":"49"}')
		self.worldbossUserInfo('{"seq":"50"}')
		self.checkAttendanceReward('{"seq":"51"}')
		self.selectGuildInvitation('{"seq":"52"}')
		self.requestGuildwarDateInfo('{"seq":"53"}')
		self.selectModeBeforeSeasonTopInfo('{"seq":"54"}')
		self.selectMailInven('{"seq":"55","last_index":"0","request_count":"100"}')
		self.connectEventCheck('{"seq":"56","lang_type":"1"}')
		self.selectMailInven('{"seq":"57","last_index":"0","request_count":"100"}')
		self.webViewEventCheck('{"seq":"58"}')
		self.announce('{"seq":"59"}')
		self.selectBillingDataBasic('{"seq":"60"}')
		self.selectHotdeal('{"seq":"61","hotdeal_index":"8"}')

	def generateUsername(self):
		return 'Rain%s'%(random.randint(10000,90000))
	
	def finishTutorial(self):		
		self.loginUser('{"seq":"4","market_type":"1","version":"1.38.10","access_token":"251702245|653|IPAD|KR|4805c07b21284817069e4016a76ed8783cc7ab57|1554637238658"}')
		self.checkPmangUsn('{"seq":"5","pmang_usn":"251702245"}')
		self.joinUser('{"seq":"6","market_type":"1","user_id":"Rain","access_token":"251702245|653|IPAD|KR|4805c07b21284817069e4016a76ed8783cc7ab57|1554637238658"}')
		self.joinUser('{"seq":"7","market_type":"1","user_id":"%s","access_token":"%s"}'%(self.generateUsername(),self.access_token))
		self.selectItemInven('{"seq":"8"}')
		self.selectCharInven('{"seq":"9"}')
		self.enterChannel('{"seq":"10","channel":"0"}')
		self.selectBuyLimit('{"seq":"11"}')
		self.selectBillingDataBasic('{"seq":"12"}')
		self.userCampaignData('{"seq":"13"}')
		self.userCampaignSeason2Data('{"seq":"14"}')
		self.userCampaignList('{"seq":"15"}')
		self.userCampaignSeason2List('{"seq":"16"}')
		self.userRuneModeData('{"seq":"17"}')
		self.selectFirstPackage('{"seq":"18"}')
		self.selectTerritoryUserInfo('{"seq":"19"}')
		self.arenaPhaseInfo('{"seq":"20"}')
		self.userArenaData('{"seq":"21"}')
		self.userDuelData('{"seq":"22"}')
		self.userNewStarDuelData('{"seq":"23"}')
		self.newStarDuelSwordCheck('{"seq":"24"}')
		self.globalDate('{"seq":"25"}')
		self.eventDate('{"seq":"26"}')
		self.ownerGuildInfo('{"seq":"27"}')
		self.selectFriendRequestList('{"seq":"28"}')
		self.selectFriendList('{"seq":"29"}')
		self.requestSelectImportantNotice('{"seq":"30","last_index":"0","language_type":"1"}')
		self.selectPartyRaidHistoryDataList('{"seq":"31"}')
		self.worldbossUserInfo('{"seq":"32"}')
		self.checkAttendanceReward('{"seq":"33"}')
		self.selectGuildInvitation('{"seq":"34"}')
		self.requestGuildwarDateInfo('{"seq":"35"}')
		self.selectModeBeforeSeasonTopInfo('{"seq":"36"}')
		self.missionInvenInsert('{"seq":"37","0":{"code":"9001","value":"1"},"list_count":"1"}')
		self.missionInvenInsert('{"seq":"38","0":{"code":"9301","value":"1"},"list_count":"1"}')
		self.missionInvenInsert('{"seq":"39","0":{"code":"9308","value":"1"},"list_count":"1"}')
		self.missionInvenInsert('{"seq":"40","0":{"code":"9701","value":"0"},"list_count":"1"}')
		self.missionInvenInsert('{"seq":"41","0":{"code":"1001","value":"0"},"1":{"code":"1002","value":"0"},"2":{"code":"1003","value":"0"},"3":{"code":"1004","value":"0"},"4":{"code":"1005","value":"0"},"5":{"code":"1006","value":"0"},"6":{"code":"1007","value":"0"},"7":{"code":"1008","value":"0"},"8":{"code":"1009","value":"0"},"9":{"code":"1010","value":"0"},"10":{"code":"1018","value":"0"},"11":{"code":"1019","value":"0"},"12":{"code":"1020","value":"0"},"13":{"code":"1021","value":"0"},"14":{"code":"1022","value":"0"},"15":{"code":"1023","value":"0"},"16":{"code":"1024","value":"0"},"17":{"code":"1017","value":"0"},"18":{"code":"1516","value":"0"},"19":{"code":"1517","value":"0"},"20":{"code":"1518","value":"0"},"21":{"code":"1519","value":"0"},"22":{"code":"1520","value":"0"},"23":{"code":"1831","value":"0"},"list_count":"24"}')
		self.missionInvenUpdate('{"seq":"42","code":"1520","value":"50000"}')
		self.selectBuyLimit('{"seq":"43"}')
		self.connectEventCheck('{"seq":"44","lang_type":"1"}')
		mails=self.selectMailInven('{"seq":"45","last_index":"0","request_count":"100"}')
		last_index=mails['5']['inven_index']
		self.webViewEventCheck('{"seq":"46"}')
		self.announce('{"seq":"47"}')
		self.selectBillingDataBasic('{"seq":"48"}')
		self.selectHotdeal('{"seq":"49","hotdeal_index":"8"}')
		self.selectActiveItem('{"seq":"50"}')
		self.selectMailInven('{"seq":"51","last_index":"%s","request_count":"94"}'%(last_index))
		self.webViewEventCheck('{"seq":"52"}')
		self.mailInvenAllRecv('{"seq":"53","inven_index_list":{"0":{"index":"52142457"},"1":{"index":"52142458"},"2":{"index":"52142460"},"3":{"index":"52142461"},"list_count":"4"}}')
		self.missionInvenUpdate('{"seq":"54","code":"1520","value":"75000"}')
		self.mailInvenRecv('{"seq":"55","inven_index":"52142456"}')
		self.missionInvenInsert('{"seq":"56","0":{"code":"3046","value":"1"},"list_count":"1"}')
		self.missionInvenInsert('{"seq":"57","0":{"code":"3066","value":"1"},"list_count":"1"}')
		self.updateCharInvenState('{"seq":"58","inven_index":"133211225","inven_state":"1"}')
		self.webViewEventCheck('{"seq":"59"}')
		self.mailInvenRecv('{"seq":"60","inven_index":"52142459"}')
		self.missionInvenUpdate('{"seq":"61","code":"3046","value":"2"}')
		self.missionInvenUpdate('{"seq":"62","code":"3066","value":"2"}')
		self.updateCharInvenState('{"seq":"63","inven_index":"133211268","inven_state":"1"}')
		self.webViewEventCheck('{"seq":"64"}')
		self.itemInvenRandomBoxUse('{"seq":"65","inven_index":"125745425"}')
		self.missionInvenInsert('{"seq":"66","0":{"code":"3041","value":"1"},"list_count":"1"}')
		self.missionInvenInsert('{"seq":"67","0":{"code":"3061","value":"1"},"list_count":"1"}')
		self.webViewEventCheck('{"seq":"68"}')
		self.itemInvenRandomBoxUse('{"seq":"69","inven_index":"125745426"}')
		self.missionInvenUpdate('{"seq":"70","code":"3041","value":"2"}')
		self.missionInvenInsert('{"seq":"71","0":{"code":"3056","value":"1"},"list_count":"1"}')

	def getMail(self):
		mails=self.selectMailInven('{"seq":"57","last_index":"0","request_count":"100"}')
		collectmail={}
		i=0
		if len(mails)>1:
			for m in mails:
				if len(m)>2:	continue
				if mails[m]['item_type']==5:
					self.mailInvenRecv('{"seq":"62","inven_index":"%s"}'%(str(mails[m]['inven_index'])))
					continue
				collectmail[str(i)]={}
				collectmail[str(i)]={"index":str(mails[m]['inven_index'])}
				i+=1
			collectmail['list_count']=len(collectmail)
			collectmail=json.dumps(collectmail,separators=(',', ':'))
			self.mailInvenAllRecv('{"seq":"60","inven_index_list":%s}'%(collectmail))

	def getPermanent(self):
		mails=self.selectItemInven('{"seq":"14"}')
		if len(mails)>1:
			for m in mails:
				if len(m)>2:	continue
				if mails[m]['code']<1000:	continue
				self.webViewEventCheck('{"seq":"70"}')
				self.itemInvenRandomBoxUse('{"seq":"67","inven_index":"%s"}'%(str(mails[m]['inven_index'])))
		
	def useScroll(self,goods_index=29,create_index=338,count=10,free_scout=0):
		res= self.scoutShopBuy('{"seq":"84","goods_index":"%s","create_index":"%s","count":"%s","free_scout":"%s"}'%(goods_index,create_index,count,free_scout))
		for unit in res:
			if len(unit)==1:
				self.log('%s with: %s*'%(self.getUnitName(res[unit]['code']),self.getUnitName(res[unit]['code'])))
		return res

	def getReward(self,rwd):
		for r in rwd:
			if len(r)<=2:
				self.missionReward('{"seq":"72","inven_index":"%s"}'%(rwd[r]['inven_index']))

	def getRandomBox(self,rwd):
		for r in rwd:
			if len(r)<=2:
				self.log('getRandomBox() reward:%s type:%s'%(r,rwd[r]['type']))
				self.itemInvenRandomBoxUse('{"seq":"61","inven_index":"%s"}'%(rwd[r]['index']))

	def fakerewards(self,id):
		if id ==1:
			pass
		else:
			pass

	def finishQuest(self,campaign_level,campaign_number):
		self.log('doing campaign_level:%s campaign_number:%s'%(campaign_level,campaign_number))
		#self.selectCharInven('{"seq":"42"}',makedeck=True)
		deck=list(self.deck_list)
		if campaign_number<=5:
			data='{"seq":"71","campaign_level":"%s","campaign_number":"%s","dummy_code":"0","friend_index":"0","friend_table_index":"0","deck_list":{"0":{"index":"%s","position":"0","sequence":"1"},"1":{"index":"%s","position":"1","sequence":"2"},"2":{"index":"%s","position":"2","sequence":"3"},"3":{"index":"%s","position":"3","sequence":"4"},"4":{"index":"%s","position":"4","sequence":"5"},"list_count":"5"}}'%(campaign_level,campaign_number,deck[0],deck[1],deck[2],deck[3],deck[4])
		else:
			data='{"seq":"61","campaign_level":"%s","campaign_number":"%s","dummy_code":"0","friend_index":"0","friend_table_index":"0","deck_list":{"0":{"index":"%s","position":"1","sequence":"7"},"1":{"index":"%s","position":"3","sequence":"8"},"2":{"index":"%s","position":"5","sequence":"9"},"3":{"index":"%s","position":"7","sequence":"4"},"4":{"index":"%s","position":"9","sequence":"5"},"5":{"index":"%s","position":"10","sequence":"2"},"6":{"index":"%s","position":"11","sequence":"6"},"7":{"index":"%s","position":"13","sequence":"3"},"8":{"index":"%s","position":"15","sequence":"1"},"list_count":"9"}}'%(campaign_level,campaign_number,deck[0],deck[1],deck[2],deck[3],deck[4],deck[5],deck[6],deck[7],deck[8])
		self.movementCheck('{"seq":"60"}')
		if self.userCampaignStageStart(data)['result']<>0:
			self.log('quest not started')
			return
		reward=self.userCampaignStageClear('{"seq":"63","battle_result":"1","expert_booster":"0","event_check":"1","campaign_stars":"3","turn_count":"%s","die_count":"0"}'%(random.randint(10,20)))
		if reward['result']==0:
			#self.missionInvenUpdate('{"seq":"64","code":"1004","value":"1"}') # Clear 5 Campaign stages
			#self.missionInvenInsert('{"seq":"65","0":{"code":"4001","value":"1"},"list_count":"1"}') # Win in Campaign 20 times
			#self.missionInvenInsert('{"seq":"66","0":{"code":"4011","value":"1"},"list_count":"1"}') # Keep all your Mercenaries alive 5 times
			self.getRandomBox(reward)
			self.fakerewards(campaign_number)

if __name__ == "__main__":
	reload(sys)  
	sys.setdefaultencoding('utf8')
	a=API()
	a.setAccess_token('251702245|653|IPAD|KR|4805c07b21284817069e4016a76ed8783cc7ab57|1554637238658')
	a.login()