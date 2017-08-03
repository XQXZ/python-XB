#CREATE TABLE `user`(
#   `userid` INT(11) NOT NULL AUTO_INCREMENT,
#   `username` VARCHAR(100) DEFAULT NULL,
#   PRIMARY KEY(`userid`)    
#)ENGINE = INNODB AUTO_INCREMENT = 9 DEFAULT CHARSET = utf8
import MySQLdb

conn = MySQLdb.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'xb',
    charset = 'utf8'
    )
cursor = conn.cursor()

#三条操作为一个事务
sql_insert = "insert into user(userid, username) values(10, 'name10')"
sql_update = "update user set username = 'name91' where userid = 9"
sql_delete = "delete from user where userd<3"#错误操作

try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount

    conn.commit()
except Exception as e:
    print e
    conn.rollback()#回滚

cursor.close()
conn.close()
