class ReimbursementRequest:
    def __init__(self, id=0, eid=0, amount=0, supervisor=0, dep_head=0, benco=0, finalized=False, course_id="", status = "",startDate = ""):
        self.id = id
        self.eid = eid
        self.amount = amount
        self.supervisor = supervisor
        self.dephead = dep_head
        self.benco = benco
        self.finalized = finalized
        self.course_id = course_id
        self.status = status
        self.startDate = startDate

    def json(self):
        return {
            "RequestID": self.id,
            "EmployeeID": self.eid,
            "Amount": self.amount,
            "Finalized": self.finalized,
            "CourseID": self.course_id,
            "Status": self.status,
            "StartDate": self.startDate



        }

    @staticmethod
    def json_parse(json):
        request = ReimbursementRequest()
        request.id = json["RequestID"] if "RequestID" in json else 0
        request.eid = json["EmployeeID"]
        request.amount = json["Amount"]
        request.supervisor = json["Supervisor"] if "Supervisor" in json else 0
        request.dephead = json["DepartmentHead"] if "DepartmentHead" in json else 0
        request.benco = json["BenefitsCoordinator"] if "BenefitsCoordinator" in json else 0
        request.finalized = json["Finalized"] if "Finalized" in json else False
        request.course_id = json["CourseID"]
        request.status = json["Status"]
        request.startDate = json["StartDate"]

        return request
