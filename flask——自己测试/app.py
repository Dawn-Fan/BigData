import os

import flask
from  flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mingxi.5@localhost/flask"
app.config['SQLACHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# 创建模型类
class Role(db.Model):
    # 手动指定mysql表的名称
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    # 定义关系引用, 第一个参数User表示多方的类名
    # 第二个参数backref表示反向引用,给User模型用,实现多对一的查询
    # 等号左边给一方Role使用,backref给多方使用
    us = db.relationship("User", backref = 'role')


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    pswd = db.Column(db.String(128),unique=True)
    # 指定外键, 指向roles的id属性
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

if __name__ == '__main__':
    # 删除数据表
    db.drop_all()
    # 创建数据表
    db.create_all()

    # 实例化模型类对象,添加测试数据
    ro1 = Role(name = "admin")
    ro2 = Role(name = "user")
    db.session.add_all([ro1, ro2])
    db.session.commit()

    us1 = User(name = "wang", email = "wang@163.com", pswd = "123456", role_id = ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=ro1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()

    app.run(debug=True)



# @app.route('/')
# def hello_world():
#     response = flask.make_response('<h1>asd<h1>')
#     response.set_cookie('an','1')
#     return response
#
# @app.route('/abc/')
# def indexabc():
#     return flask.redirect('http://www.baidu.com')
# @app.route('/c/')
# def abc():
#     flask.abort(404)
#     return   'asd'


if __name__ == '__main__':
    app.run()
