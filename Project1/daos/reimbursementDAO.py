from models.employee import Employee
from models.reimburse_request import ReimbursementRequest
from utils.db_connection import connection as dbc


class ReimbursementDAO:

    def check_available_funds(eid):

        request = ReimbursementRequest(eid=eid)
        e = Employee(id=eid)
        sql = "Select * from \"Tuition\".reimbursements where eid =%s"
        cursor = dbc.cursor()
        cursor.execute(sql, [eid])
        recs = cursor.fetchone()
        tutAmounts = []
        for rec in recs:
            rqs = ReimbursementRequest(rec[0], rec[1], int(rec[2]), rec[3], rec[4], rec[5], rec[6], rec[7])
        tutAmounts.append(rqs)

        i = 0
        totA = 0
        while i < tutAmounts.len():
            totA += int(rqs.amount)
            i += 1
        total = 1000 - totA
        return total

    @staticmethod
    def get_all_requests():
        sql = "select * from \"Tuition\".reimbursments"
        cursor = dbc.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        requests_list = []

        for rec in records:
            rqs = ReimbursementRequest(rec[0], rec[1], int(rec[2]), rec[3], rec[4], rec[5], rec[6], rec[7])
            requests_list.append(rqs.json())

        return requests_list

    @staticmethod
    def get_by_id(id):
        sql = "Select * from \"Tuition\".reimbursements where id =%s"
        cursor = dbc.cursor()
        cursor.execute(sql,[id])
        records = cursor.fetchall()
        requests_list = []

        for rec in records:
            rqs = ReimbursementRequest(rec[0], rec[1], int(rec[2]), rec[3], rec[4], rec[5], rec[6], rec[7])
            requests_list.append(rqs.json())

        return requests_list

    @staticmethod
    def get_by_EID(eid):
        sql = "select * from \"Tuition\".reimbursments where eid = %s"
        cursor = dbc.cursor()
        cursor.execute(sql,[eid])
        records = cursor.fetchall()
        requests_list = []

        for rec in records:
            rqs = ReimbursementRequest(rec[0], rec[1], int(rec[2]), rec[3], rec[4], rec[5], rec[6], rec[7],rec[8],rec[9],rec[10].rec[11,rec[12]])
            requests_list.append(rqs.json())
        print(requests_list.__repr__())
        return requests_list

    @staticmethod
    def create_req(reqt):
        r = ReimbursementRequest.json_parse(reqt)
        sql = "INSERT INTO \"Tuition\".reimbursments (eid, amount, finalized, course_id,status, start_date) VALUES(%s, %s, false, %s,%s,%s) Returning *;"
        cursor = dbc.cursor()
        cursor.execute(sql,(r.eid,r.amount,r.course_id,r.status,r.startDate))
        dbc.commit()

        rec = cursor.fetchone()
        new_request = ReimbursementRequest(rec[0], rec[1], int(rec[2]), rec[3], rec[4], rec[5], rec[6], rec[7])

        return new_request

    @staticmethod
    def get_by_supervisor(sid):
        sql = "Select * from \"Tuition\".reimbursements where supervisorid =%s"
        cursor = dbc.cursor()
        cursor.execute(sql, [sid])
        records = cursor.fetchall()
        requests_list = []

        for rec in records:
            rqs = ReimbursementRequest(rec[0], rec[1], int(rec[2]), rec[3], rec[4], rec[5], rec[6], rec[7],rec[8],rec[9])
            requests_list.append(rqs.json())

        return requests_list

    @staticmethod
    def get_by_department_head(depHeadID):
        sql = "Select * from \"Tuition\".reimbursements where department_head =%s"
        cursor = dbc.cursor()
        cursor.execute(sql, [depHeadID])
        records = cursor.fetchall()
        requests_list = []

        for rec in records:
            rqs = ReimbursementRequest(rec[0], rec[1], int(rec[2]), rec[3], rec[4], rec[5], rec[6], rec[7], rec[8],rec[9])
            requests_list.append(rqs.json())

        return requests_list

    @staticmethod
    def get_by_benco(bencoID):
        sql = "Select * from \"Tuition\".reimbursements where benco =%s"
        cursor = dbc.cursor()
        cursor.execute(sql, [bencoID])
        records = cursor.fetchall()
        requests_list = []
        for rec in records:
                rqs = ReimbursementRequest(rec[0], rec[1], int(rec[2]), rec[3], rec[4], rec[5], rec[6], rec[7],rec[8],rec[9])

        return requests_list

    @staticmethod
    def update_request(req):
        updateReq = ReimbursementRequest.json_parse(req)
        sql ="UPDATE \"Tuition\".reimbursments SET amount=%s, supervisorid=%s, department_head=%s, benco=%s, finalized=%s, status=%s WHERE eid=%s RETURNING *;"
        cursor = dbc.cursor()
        cursor.execute(sql, (updateReq.amount,updateReq.supervisor,updateReq.dephead,updateReq.benco,updateReq.finalized,updateReq.status) )
        dbc.commit()
        record = cursor.fetchone()
        newreq= ReimbursementRequest(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9])
        return newreq

    @staticmethod
    def get_all_requestids():
        sql = "select * from \"Tuition\".reimbursments"
        cursor = dbc.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        requests_list = []

        for rec in records:
            rqs = ReimbursementRequest(rec[0])
            requests_list.append(rqs.json())

        return requests_list

    @staticmethod
    def dept_Approval(rqJson):
        updateReq = ReimbursementRequest.json_parse(rqJson)
        updateReq.supervisor_approval = True
        updateReq.deptapproval = True
        print(updateReq.id)
        sql = "UPDATE \"Tuition\".reimbursments SET supervisor_approval = %s,deptapproval=%s WHERE id=%s RETURNING *;"
        cursor = dbc.cursor()
        cursor.execute(sql, (updateReq.supervisor_approval,updateReq.deptapproval,updateReq.id))
        dbc.commit()
        record = cursor.fetchone()
        newreq = ReimbursementRequest(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8], record[9],record[10],record[11],record[12])
        newreq.deptapproval = True
        newreq.supervisor_approval = True
        return newreq

    @staticmethod
    def bencoApproval(rq):
        updateReq = ReimbursementRequest.json_parse(rq)
        updateReq.supervisor_approval = True
        updateReq.deptapproval = True
        updateReq.bencoapproval = True
        print(updateReq.id)
        sql = "UPDATE \"Tuition\".reimbursments SET supervisor_approval = %s,deptapproval=%s,bencoapproval = %s, Status = 'Approved Pending Grade' WHERE id=%s RETURNING *;"
        cursor = dbc.cursor()
        cursor.execute(sql, (updateReq.supervisor_approval, updateReq.deptapproval,updateReq.bencoapproval, updateReq.id))
        dbc.commit()
        record = cursor.fetchone()
        newreq = ReimbursementRequest(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8], record[9], record[10], record[11], record[12])
        newreq.deptapproval = True
        newreq.supervisor_approval = True
        newreq.bencoapproval = True
        print(newreq.json())
        return newreq

    @staticmethod
    def denied(req):
        updateReq = ReimbursementRequest.json_parse(req)
        updateReq.supervisor_approval = True
        updateReq.deptapproval = True
        updateReq.bencoapproval = True
        print(updateReq.id)
        sql = "UPDATE \"Tuition\".reimbursments SET finalized = true, supervisor_approval = %s,deptapproval=%s,bencoapproval = %s, Status = 'Denied' WHERE id=%s RETURNING *;"
        cursor = dbc.cursor()
        cursor.execute(sql,
                       (updateReq.supervisor_approval, updateReq.deptapproval, updateReq.bencoapproval, updateReq.id))
        dbc.commit()
        record = cursor.fetchone()
        newreq = ReimbursementRequest(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8], record[9], record[10], record[11], record[12])
        newreq.deptapproval = True
        newreq.supervisor_approval = True
        newreq.bencoapproval = True
        print(newreq.json())
        return newreq


def _test():
    rdao = ReimbursementDAO()
    requests =rdao.get_all_requests()
    print(requests)


if __name__ == '__main__':
    _test()