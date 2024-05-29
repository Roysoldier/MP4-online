from flask import Flask, jsonify, request, render_template, session, make_response
from os import urandom,path,remove
from lib import myLogger,sign,sqlitewrap
import traceback
import re
import datetime
from werkzeug.utils import secure_filename
from random import randint
import sys
import yaml
import yamlordereddictloader
from apscheduler.schedulers.background import BackgroundScheduler
import threading
import json
import hashlib


ROOT_PATH = path.dirname(path.abspath(__file__)).strip() + "/"

CONFIG = {}

LOCK = threading.Lock()

lien =  r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[\w\-\./?#=&]+'

mydb = sqlitewrap.SqliteWrap(ROOT_PATH + "db/auth.db")

logger = myLogger.MyLogger(path=ROOT_PATH + "logs/messages.log")

debug = False

local = False
USERS = {}
#mydb.update_row("users",f"user = 'Noan'",f"status = 'admin'")

###############################################
# Appel de fonction
###############################################

# Définition du nom de mon application Flask
APP_FLASK = Flask(__name__)

APP_FLASK.permanent_session_lifetime = datetime.timedelta(days=1)

# Rechargement des pages WEB automatiquement dès qu'on les change
APP_FLASK.config["TEMPLATES_AUTO_RELOAD"] = True
APP_FLASK.config["SESSION_COOKIE_HTTPONLY"] = False
APP_FLASK.config["REMEMBER_COOKIE_HTTPONLY"] = True
APP_FLASK.config["SESSION_COOKIE_SAMESITE"] = "Strict"
APP_FLASK.config['UPLOAD_FOLDER'] = "./static/data"

# Génération d'un secret de connexion utile à Falsk
APP_FLASK.secret_key = urandom(12)

# Gestion de l'appel à la page index.html
@APP_FLASK.route('/', methods=['GET'])
@APP_FLASK.route('/index.html', methods=['GET'])
def index():
    try:
        cook = recup_cook()
        isConnect = sign.is_connected(logger=logger,mydb=mydb,pseudo=cook,debug=debug)
        userInfo,userError = mydb.read_row("userinfo",f"name = '{cook}'")
        res,err = mydb.read_row("users",f"user = '{cook}'")
        if isConnect:
            render = {"login":isConnect,"pseudo":cook,"img": f"./static/data/{userInfo[0][3]}","status":res[0][7]}
        else:
            render = {"login":isConnect}
        #print("render : ",render)
        if debug:
            logger.log("Requête index.html", "DEBUG")
        #renvoie du code source signin.html au navigateur web après traitement
        return render_template('index.html', render=render)
    except:
        logger.log("Erreur inconnue dans index.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")

@APP_FLASK.route('/code.html', methods=['GET'])
def code():
    try:
        cook = recup_cook()
        isConnect = sign.is_connected(logger=logger,mydb=mydb,pseudo=cook,debug=debug)
        userInfo,userError = mydb.read_row("userinfo",f"name = '{cook}'")
        res,err = mydb.read_row("users",f"user = '{cook}'")
        if isConnect:
            render = {"login":isConnect,"pseudo":cook,"img": f"./static/data/{userInfo[0][3]}","status":res[0][7]}
        else:
            render = {"login":isConnect}
        #print("render : ",render)
        if debug:
            logger.log("Requête code.html", "DEBUG")
        #renvoie du code source signin.html au navigateur web après traitement
        return render_template('code.html', render=render)
    except:
        logger.log("Erreur inconnue dans code.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")


# Gestion de l'appel à la page programmes.html
@APP_FLASK.route('/programmes.html', methods=['GET'])
def programmes():
    try:
        cook = recup_cook()
        isConnect = sign.is_connected(logger=logger,mydb=mydb,pseudo=cook,debug=debug)
        userInfo,userError = mydb.read_row("userinfo",f"name = '{cook}'")
        res,err = mydb.read_row("users",f"user = '{cook}'")
        if isConnect:
            render = {"login":isConnect,"pseudo":cook,"img": f"./static/data/{userInfo[0][3]}","status":res[0][7]}
        else:
            render = {"login":isConnect}
        #print("render : ",render)
        if debug:
            logger.log("Requête programmes.html", "DEBUG")
        #renvoie du code source signin.html au navigateur web après traitement
        return render_template('programmes.html', render=render)
    except:
        logger.log("Erreur inconnue dans programmes.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")



# Gestion de l'appel à la page scratch.html
@APP_FLASK.route('/scratch.html', methods=['GET'])
def scratch():
    try:
        cook = recup_cook()
        isConnect = sign.is_connected(logger=logger,mydb=mydb,pseudo=cook,debug=debug)
        userInfo,userError = mydb.read_row("userinfo",f"name = '{cook}'")
        res,err = mydb.read_row("users",f"user = '{cook}'")
        if isConnect:
            render = {"login":isConnect,"pseudo":cook,"img": f"./static/data/{userInfo[0][3]}","status":res[0][7]}
        else:
            render = {"login":isConnect}
        #print("render : ",render)
        if debug:
            logger.log("Requête scratch.html", "DEBUG")
        #renvoie du code source signin.html au navigateur web après traitement
        return render_template('scratch.html', render=render)
    except:
        logger.log("Erreur inconnue dans scratch.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")



# Gestion de l'appel à la page help.html
@APP_FLASK.route('/help.html', methods=['GET'])
def help():
    try:
        cook = recup_cook()
        isConnect = sign.is_connected(logger=logger,mydb=mydb,pseudo=cook,debug=debug)
        userInfo,userError = mydb.read_row("userinfo",f"name = '{cook}'")
        res,err = mydb.read_row("users",f"user = '{cook}'")
        if isConnect:
            render = {"login":isConnect,"pseudo":cook,"img": f"./static/data/{userInfo[0][3]}","status":res[0][7]}
        else:
            render = {"login":isConnect}
        #print("render : ",render)
        if debug:
            logger.log("Requête help.html", "DEBUG")
        #renvoie du code source signin.html au navigateur web après traitement
        return render_template('help.html', render=render)
    except:
        logger.log("Erreur inconnue dans help.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")



# Gestion de l'appel à la page prog-ventilateur.html
@APP_FLASK.route('/prog-ventilateur.html', methods=['GET'])
def prog_ventilateur():
    try:
        cook = recup_cook()
        isConnect = sign.is_connected(logger=logger,mydb=mydb,pseudo=cook,debug=debug)
        userInfo,userError = mydb.read_row("userinfo",f"name = '{cook}'")
        res,err = mydb.read_row("users",f"user = '{cook}'")
        if isConnect:
            render = {"login":isConnect,"pseudo":cook,"img": f"./static/data/{userInfo[0][3]}","status":res[0][7]}
        else:
            render = {"login":isConnect}
        #print("render : ",render)
        if debug:
            logger.log("Requête prog-ventilateur.html", "DEBUG")
        #renvoie du code source signin.html au navigateur web après traitement
        return render_template('prog-ventilateur.html', render=render)
    except:
        logger.log("Erreur inconnue dans prog-ventilateur.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")




# Gestion de l'appel à la page prog-artiste.html
@APP_FLASK.route('/prog-artiste.html', methods=['GET'])
def prog_artiste():
    try:
        cook = recup_cook()
        isConnect = sign.is_connected(logger=logger,mydb=mydb,pseudo=cook,debug=debug)
        userInfo,userError = mydb.read_row("userinfo",f"name = '{cook}'")
        res,err = mydb.read_row("users",f"user = '{cook}'")
        if isConnect:
            render = {"login":isConnect,"pseudo":cook,"img": f"./static/data/{userInfo[0][3]}","status":res[0][7]}
        else:
            render = {"login":isConnect}
        #print("render : ",render)
        if debug:
            logger.log("Requête prog-artiste.html", "DEBUG")
        #renvoie du code source signin.html au navigateur web après traitement
        return render_template('prog-artiste.html', render=render)
    except:
        logger.log("Erreur inconnue dans prog-artiste.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")



# Gestion de l'appel à la page prog-intelligent.html
@APP_FLASK.route('/prog-intelligent.html', methods=['GET'])
def prog_intelligent():
    try:
        cook = recup_cook()
        isConnect = sign.is_connected(logger=logger,mydb=mydb,pseudo=cook,debug=debug)
        userInfo,userError = mydb.read_row("userinfo",f"name = '{cook}'")
        res,err = mydb.read_row("users",f"user = '{cook}'")
        if isConnect:
            render = {"login":isConnect,"pseudo":cook,"img": f"./static/data/{userInfo[0][3]}","status":res[0][7]}
        else:
            render = {"login":isConnect}
        #print("render : ",render)
        if debug:
            logger.log("Requête prog-intelligent.html", "DEBUG")
        #renvoie du code source signin.html au navigateur web après traitement
        return render_template('prog-intelligent.html', render=render)
    except:
        logger.log("Erreur inconnue dans prog-intelligent.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")




# Gestion de l'appel à la page signin.html
@APP_FLASK.route('/signin.html', methods=['GET'])
def signin():
    try:
        if debug:
            logger.log("Requête signin.html", "DEBUG")
        #renvoie du code source signin.html au navigateur web après traitement
        return render_template('signin.html')
    except:
        logger.log("Erreur inconnue dans signin.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")


# Gestion de l'appel à la page signup.html
@APP_FLASK.route('/signup.html', methods=['GET'])
def signup():
    try:
        if debug:
            logger.log("Requête signup.html", "DEBUG")
        #renvoie du code source signup.html au navigateur web après traitement
        return render_template('signup.html')
    except:
        logger.log("Erreur inconnue dans signup.html", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")









###############################################
# API
###############################################

@APP_FLASK.route('/api/signup', methods=['POST'])
def api_signup():
    try:
        if debug:
            logger.log("Requête api_signup", "DEBUG")
            result = sign.signup(logger=logger,mydb=mydb,payload=request.json,debug=debug,bypass=False,verif=CONFIG['scheduler']['enable'],lock=LOCK,path=ROOT_PATH)
        return jsonify(result)
    except:
        logger.log("Erreur inconnue dans api_signup", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")
        return jsonify({"status":"nok","msg":'error'})
    
@APP_FLASK.route('/api/signin', methods=['POST'])
def api_signin():
    try:
       
        if debug:
            logger.log("Requête api_signin", "DEBUG")
        
        result,user = sign.signin(logger=logger,mydb=mydb,email=request.json['email'],pwd=request.json['password'],debug=debug)
        if user['auth']:
            binarykey = bytes(user['user'] + f"nroydevencryptagecookie{randint(1,1000)}", "utf-8")
            hashcook = hashlib.sha256(binarykey).hexdigest()
            res,err = mydb.update_row("users",f"user = '{user['user']}'",f"hashcook = '{hashcook}'")
            res, err = mydb.read_rows("users", ["user","hashcook"])

            resp = make_response(jsonify (result))  
            if not local:
                resp.set_cookie('USER_ID',hashcook,path="/",domain="nroydev.fr", httponly=True, secure=True)  
            else:
                resp.set_cookie('USER_ID',hashcook,path="/", httponly=True, secure=True)  
            
        return resp
    except:
        logger.log("Erreur inconnue dans api_signin", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")
        return jsonify({"status":"nok","msg":'error'})


@APP_FLASK.route('/api/signout', methods = ['POST'])
def api_signout():
    try:
        cook = recup_cook()

        payload = request.json
        sign.sign_out(logger=logger,mydb=mydb,pseudo=cook,debug=debug)
        logger.log(payload["message"],"INFO")
        return jsonify({"status":"ok","msg":'cool'})
    except:
        logger.log("Erreur inconnue dans api/signout", "ERROR")
        if debug:
            logger.log(str(traceback.format_exc()),"DEBUG")
        return jsonify({"status":"nok","msg":'error'})


###############################################
# Fonction 
###############################################
def recup_cook():
    cook = request.cookies.get('USER_ID',"")
    if cook and mydb.read_row("users",f"hashcook = '{cook}'") != []:
        cook = mydb.read_row("users",f"hashcook = '{cook}'")[0][0][1]
    return cook
   

###############################################
# Main 
###############################################
if __name__ == '__main__':
    logger.log("Lancement de l'application ! ", "INFO")
    logger.log("Ouverture du fichier de configuration", "INFO")
    try:
        with open(ROOT_PATH + "config.yaml", "r") as f:
            CONFIG = yaml.load(f, Loader=yamlordereddictloader.Loader)
    except IOError:
        logger.log("Erreur dans le fichier de config", "ERROR")
        sys.exit()
    
    debug = CONFIG.get('debug',False)
    local = CONFIG.get('local',False)
    logger.log("Création de la base de donnée", "INFO")
    mydb.create_table("users",[("id","INTEGER"),("user","TEXT"),("email","TEXT"),("mdp","TEXT"),("lastlog","INTEGER"),("connected","INTEGER"),("hashcook","TEXT"),("status","TEXT")])
    mydb.create_table("userinfo",[("name","TEXT"),("email","TEXT"),("img","TEXT")])
    if CONFIG['scheduler']['enable']:
        logger.log("Démarrage du scheduler", "INFO")
        scheduler = BackgroundScheduler()
        job = scheduler.add_job(check_account, 'interval', minutes=CONFIG['scheduler']['interval'])
        scheduler.start()
    logger.log("Démarrage du serveur flask", "INFO")
    APP_FLASK.run(ssl_context=(ROOT_PATH + 'ssl/cert.cer',ROOT_PATH + 'ssl/key.key'),host = CONFIG['network']['ip'], port = CONFIG['network']['port'])
    #APP_FLASK.run(host = CONFIG['network']['ip'], port = CONFIG['network']['port'])