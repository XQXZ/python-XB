python3.x使用MySQL

安装pymysql包
 pip install pymysql
引入开发包
import pymysql.cursors
获取数据库链接
connection = pymysql.connect(
					host = 'localhost',
				    user = 'root',
				    passwd = '123456',
				    db = 'xb',
				    charset = 'utf8mb4')
获取会话指针
cursor = connection.cursor()
执行SQL语句
sql = ""
cursor.execute(sql,(参数1，参数2……))
提交
connection.commit()
关闭
connection.close()

注：若sql查询数据则 cursor.execute(sql) 返回int型数据（总记录数）
调用cursor.fetch*()可返回数据