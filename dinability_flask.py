from flask import Flask
#build app object
app = Flask(__name__) #__name__ represents the module itself,dinability_flask.py
#fast navigation of flask
#acquire a direction to find the model file

# url: http[80]/https[443]://www.dinability.com:443/path
#url与视图：path与视图

#创建路由（route）和视图函数的映射
@app.route('/login')#‘/’根路由
def login():
    return "Hungry? username!"#return值返回至route#11行

@app.route('/welcome/<user_name>')
def welcome(user_name):
    return "Let's get started, %s" % user_name


if __name__ == '__main__':
    app.run(debug =True) #change host to 0.0.0.0 to let others to see flask(--host = 0.0.0.0)
    #change port (--host = 0.0.0.0 --port = 8000) if the original port is occupied