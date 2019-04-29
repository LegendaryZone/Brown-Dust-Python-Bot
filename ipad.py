from main import API
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

a=API()
a.setUdid('5990139B-C394-4C37-92C8-4546603C7153')
a.setRegion('global')

a.login()
a.getMail()
a.getPermanent()

#a.finishQuest(0,11)
#a.finishQuest(0,12)
#a.finishQuest(0,13)
#a.finishQuest(0,14)
#a.finishQuest(0,15)
#a.finishQuest(0,16)
#a.finishQuest(0,17)
#a.finishQuest(0,20)
#exit(1)
#while(1):
a.selectCharInven('{"seq":"42"}',makedeck=True)
for i in range(24,40):
	a.finishQuest(0,i+1)
exit(1)
#a.finishQuest(0,1)