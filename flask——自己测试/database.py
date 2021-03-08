from sqlalchemy import create_engine

HOSTNAME = 'localhost'  # 连接数据库地址 -->小区
DATABASE = 'flask'  # 数据库 -->单元
PORT = 3306  # 端口 -->门牌号
USERNAME = 'root'  # 用户名和密码 -->开锁
PASSWORD = 'mingxi.5'
# 用户名对应密码，地址对应端口，连接的哪个数据库
# 如果报了警告，就pip install mysql-connector 将pymysql换为mysqlconnector就好，这是因为最新的官方版本想要我们用最新的去使用
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)  # 创建数据库引擎
with engine.connect()as conn:  # 创建连接
    result = conn.execute('select * from stu')  # 执行sql语句，原生的sql写法，后面会讲ORM操作数据库
    print(result)  # 它是一个对象，打印出来的是内存地址 <sqlalchemy.engine.result.ResultProxy object at 0x000001C9581A5DC8>
    print(result.fetchone())  # 打印出一条表中的结果，以元组的形式输出(1, 'beiyue', 'M')


