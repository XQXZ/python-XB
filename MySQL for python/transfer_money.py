#coding:UTF8
import sys
import MySQLdb

class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    #检查用户id是否合法
    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid = %s" % acctid #查找用户
            cursor.execute(sql)
            print "check_acct_available:" + sql
            rs = cursor.fetchall()
            if len(rs)!= 1:
                raise Exception("账号%s不存在" % acctid)
        finally:
            cursor.close() 
    
    #是否有足够的钱转账
    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>%s" % (acctid, money) #查找用户
            cursor.execute(sql)
            print "has_enough_money:" + sql
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("账号%s没有足够的钱转账" % acctid)
        finally:
            cursor.close() 
    
    #转账成功后减少存款
    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" % (money, acctid) #查找用户
            cursor.execute(sql)
            print "reduce_money:" + sql
            if cursor.rowcount != 1:
                raise Exception("账号%s减款失败" % acctid)
        finally:
            cursor.close() 
    
    #转账成功后增加存款
    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" % (money, acctid) #查找用户
            cursor.execute(sql)
            print "add_money:" + sql
            if cursor.rowcount != 1:
                raise Exception("账号%s加款失败" % acctid)
        finally:
            cursor.close() 
    
    
    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)#检查用户id是否合法
            self.check_acct_available(target_acctid) 
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)#转账成功后减少存款
            self.add_money(target_acctid, money)#转账成功后增加存款
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e  #继续抛出异常
if __name__=="__main__":
    source_acctid = sys.argv[1]#从程序外部向程序传递参数
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    
    conn = MySQLdb.Connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '123456',
        db = 'xb',
        charset = 'utf8'
    )
    tr_money = TransferMoney(conn)
    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print "出现问题："+str(e)
    finally:
        conn.close()    


#创建表SQL语句
#CREATE TABLE `account`(
#   `acctid` INT(11) DEFAULT NULL COMMENT '账户ID',
#   `money` INT(11) DEFAULT NULL COMMENT '余额'
#)ENGINE = INNODB DEFAULT CHARSET = utf8 ;
