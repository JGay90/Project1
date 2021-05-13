from flask import jsonify, request, json
from exceptions.resource_not_found import ResourceNotFound
from flask_cors import CORS
from exceptions.credentials_not_valid import CredentialsNotFound
from models.reimburse_request import ReimbursementRequest
from daos.reimbursementDAO import ReimbursementDAO
from services.ReimbursementServices import ReimbursementService


def route(app):

    @app.route("/request_form", methods=['POST'])
    def new_reqt():
        rqJson=request.json
        req =ReimbursementService.create_request(rqJson)
        return jsonify(req.json()),200
    @app.route("/BencoDeny",methods=['POST'])
    def BencoDeny():
        rq = request.json
        deny = ReimbursementService.denied(rq)
        return jsonify(deny.json()),200

    @app.route("/all_Requests",methods=['POST'])
    def get_requests():
        returned = ReimbursementDAO.get_all_requests()
        return jsonify(returned.__str__()),200
    @app.route("/all_Requests/RequestIDs",methods=['POST'])
    def get_requestids():
        returned = ReimbursementDAO.get_all_requestids()
        return jsonify(returned),200
    @app.route("/Supervisor_View",methods=['GET'])
    def supervisor_view(sid,eid):
        if sid == eid:
            results = ReimbursementDAO.get_by_supervisor(sid)
            return results.__str__(),200
        else:
            raise CredentialsNotFound(f"Your credentials are invalid for this view")
    @app.route("/DeptApproved",methods=['Post'])
    def deptApproval():
        rqJson = request.json
        update= ReimbursementDAO.dept_Approval(rqJson)
        return jsonify(update.json()),200
    @app.route("/BencoApproval",methods=['POST'])
    def bencoapprval():
        rq = request.json
        update = ReimbursementDAO.bencoApproval(rq)
        return jsonify(update.json()),200
    @app.route("/DepartmentHead_View", methods=['POST'])
    def DepartmentHead_view():
        dhid = request.json
        eid = request.json
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

