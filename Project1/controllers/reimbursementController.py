from flask import jsonify, request, json
from exceptions.resource_not_found import ResourceNotFound
from flask_cors import CORS
from exceptions.credentials_not_valid import CredentialsNotFound
from models.reimburse_request import ReimbursementRequest
from daos.reimbursementDAO import ReimbursementDAO

def route(app):

    @app.route("/request_form", methods=['POST'])
    def new_request(request):
        req = ReimbursementRequest()
        req.json_parse(request)
        ReimbursementDAO.create_req(req)
        return jsonify(req.json()),200

    @app.route("/all_Requests",methods=['GET'])
    def get_requests(eid):
        returned = ReimbursementDAO.get_by_EID(int(eid))
        return jsonify(returned.__str__()),200

    @app.route("/Supervisor_View",methods=['GET'])
    def supervisor_view(sid,eid):
        if sid == eid:
            results = ReimbursementDAO.get_by_supervisor(sid)
            return results.__str__(),200
        else:
            raise CredentialsNotFound(f"Your credentials are invalid for this view")

    @app.route("/DepartmentHead_View", methods=['GET'])
    def DepartmentHead_view(dhid, eid):
        if dhid == eid:
            results = ReimbursementDAO.get_by_department_head(dhid)
            return jsonify(results), 200
        else:
           raise CredentialsNotFound(f"Your credentials are invalid for this view")

    @app.route("/Benco_View", methods=['GET'])
    def benco_view(bencoid, eid):
        if bencoid == eid:
            results = ReimbursementDAO.get_by_benco(bencoid)
            return results.__str__(), 200
        else:
            raise CredentialsNotFound(f"Your credentials are invalid for this view")

