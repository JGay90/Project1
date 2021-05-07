from daos.reimbursementDAO import ReimbursementDAO


class ReimbursementService:
    rdao = ReimbursementDAO
    @staticmethod
    def get_all_requests():
        return ReimbursementDAO.get_all_requests()
    @staticmethod
    def get_request_by_ID(id):
        return ReimbursementDAO.get_by_id(int(id))

    @staticmethod
    def get_by_employeeID(eid):
        return ReimbursementDAO.get_by_EID(int(eid))
    @staticmethod
    def create_request(request):
        return ReimbursementDAO.create_req(request)

    @staticmethod
    def check_available(eid):
        return ReimbursementDAO.check_available_funds(int(eid))
    @staticmethod
    def get_by_supervisor(sid):
        return ReimbursementDAO.get_by_supervisor(int(sid))
    @staticmethod
    def get_by_department_head(dphid):
        return ReimbursementDAO.get_by_department_head(int(dphid))

    @staticmethod
    def get_by_benco(bid):
        return ReimbursementDAO.get_by_benco(int(bid))

    @staticmethod
    def update_request(req):
        return ReimbursementDAO.update_request(req)