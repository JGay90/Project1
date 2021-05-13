class ReimbursementRequest:
    def __init__(self, id=0, eid=0, amount=0, supervisor=0, dep_head=0, benco=0, finalized=False,
                 course_id="", status = "Pending",startDate = "",supervisor_approval = False,
                 deptapproval= False,bencoapproval= False):
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
        self.supervisor_approval = supervisor_approval
        self.deptapproval = deptapproval
        self.bencoapproval = bencoapproval

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
        j = json
        print(type(j))
        request = ReimbursementRequest()
        request.id = json["RequestID"] if "RequestID" in json else 0
        request.eid = json["EmployeeID"]
        request.amount = json["Amount"] if "Amount" in json else 0
        request.supervisor = json["Supervisor"] if "Supervisor" in json else 0
        request.dephead = json["DepartmentHead"] if "DepartmentHead" in json else 0
        request.benco = json["BenefitsCoordinator"] if "BenefitsCoordinator" in json else 0
        request.finalized = json["Finalized"] if "Finalized" in json else False
        request.course_id = json["CourseID"] if "CourseID" in json else "null"
        request.status = json["Status"]if "Status" in json else "Pending"
        request.startDate = json["StartDate"] if "StartDate" in json else "00-00-00"
        request.supervisor_approval = json["supervisor_approval"] if "supervisor_approval" in json else False
        request.deptapproval = json["DeptApprove"] if "DeptApprove" in json else False
        request.bencoapproval = json["BencoApprove"] if "BencoApprove" in json else False
        return request

    def __repr__(self):
        return (dict(id=self.id,eid=self.eid,amount=self.amount,course_id=self.course_id,status=self.status,startDate=self.startDate))