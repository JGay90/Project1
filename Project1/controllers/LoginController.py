from flask import jsonify, request, json
from exceptions.resource_not_found import ResourceNotFound
from flask_cors import CORS
from models.userLogin import UserLogin
from services.loginService import LoginService


def route(app):
    @app.route("/login", methods=['POST'])
    def loggingin():
        ul = UserLogin()
        ul.json_parse(request.json)
        LoginService.login(ul)
        return jsonify(ul.json()),200
    @app.route("/login/valid", methods=['POST'])
    def checkStatus():
        ul = UserLogin.json_parse(request.json)
        print(ul.__repr__())
        if ul.eid == 2:
            # print("returned Dept. Head")
            ul.depHead = True
            # u = ul
            #


        if ul.eid == 1:
            # print("Returned Supervisor")
            ul.supervisor = True


        if ul.eid == 5:
            # print("Returned Benco")
            ul.benco = True


        if ul.eid == 4:
            ul.benco = False
            ul.depHead = False
            ul.supervisor=False


        return jsonify(ul.json(), 200)