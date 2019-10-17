# -*- coding: utf-8 -*-
import sqlite3
import os.path

class Database(object):
	def __init__(self):
		self.sqlite_file='accounts.db'
		if not os.path.isfile(self.sqlite_file):
			self.createDb()

	def createDb(self):
		conn = sqlite3.connect(self.sqlite_file)
		c = conn.cursor()
		c.execute('''CREATE TABLE "info" ("udid" TEXT NOT NULL,"gold" INTEGER NOT NULL,"jewelry" INTEGER NOT NULL,"level" INTEGER NOT NULL,"owner_index" INTEGER NOT NULL,PRIMARY KEY("udid"));''')
		conn.commit()
		conn.close()

	def addAccount(self,udid,gold,jewelry,level,owner_index):
		conn = sqlite3.connect(self.sqlite_file)
		c = conn.cursor()
		c.execute("INSERT INTO info (udid,gold,jewelry,level,owner_index) VALUES ('%s',%s,%s,%s,%s)"%(udid,gold,jewelry,level,owner_index))
		conn.commit()
		conn.close()

	def updateAccount(self,udid,gold,jewelry,level,owner_index):
		conn = sqlite3.connect(self.sqlite_file)
		c = conn.cursor()
		c.execute("UPDATE info SET gold=%s,jewelry=%s,level=%s,owner_index=%s where udid='%s'"%(gold,jewelry,level,owner_index,udid))
		conn.commit()
		conn.close()

	def getAccount(self,udid):
		conn = sqlite3.connect(self.sqlite_file)
		c = conn.cursor()
		c.execute("select * from info where udid='%s'"%(udid))
		all_rows = c.fetchall()
		conn.close()
		return all_rows

	def getAllAccounts(self,limit=None):
		conn = sqlite3.connect(self.sqlite_file)
		c = conn.cursor()
		if limit:
			c.execute("select udid from info where jewelry>%s"%(limit))
		else:
			c.execute("select udid from info")
		all_rows = c.fetchall()
		conn.close()
		return all_rows

if __name__ == '__main__':
	db=Database()
	db.createDb()