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
        if (LoginService.pickBenco(ul.json()) == True):
            # print("Returned Benco")
            return jsonify(ul.json()), 200
        elif (LoginService.PickDepHead(ul.json()).depHead == True):
            # print("returned Dept. Head")
            ul.depHead = True
            u = ul
            return jsonify(ul.json(), 200)
        elif (LoginService.pickSuper(ul.json()).supervisor == True):
            # print("Returned Supervisor")
            ul.supervisor = True
            return jsonify(ul.json(), 200)
        elif (LoginService.pickBenco(ul.json()) == True):
                # print("Returned Benco")
                ul.benco = True
                return jsonify(ul.json()), 200
        else:
            # print("Returned Employee")
            return jsonify(ul.json(), 200)
