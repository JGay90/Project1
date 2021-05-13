from utils.db_connection import connection as dbc
from models.userLogin import UserLogin
from models.employee import Employee


class LoginUserDAO:
    @staticmethod
    def login(userlogin):
        # print(userlogin.__repr__())
        sql = "Select * from \"Tuition\".login where username = %s and password = %s"
        cursor = dbc.cursor()
        # print(userlogin)
        cursor.execute(sql, (userlogin.un, userlogin.pw))
        record = cursor.fetchone()
        if record:
            login = UserLogin(username=record[1], password=record[2], eid= int(record[3]))
            sql = "select * from \"Tuition\".employees where id = %s"
            cursor = dbc.cursor()
            cursor.execute(sql, [login.eid])
            rec = cursor.fetchone()
            if rec:
                 emp = Employee(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6])
            return emp

    @staticmethod
    def pickSuper(json):
        u = UserLogin.json_parse(json)
        e = Employee()
        e.eid = u.eid
        sql ="select * from \"Tuition\".supervisors where id =%s "
        cursor = dbc.cursor()
        cursor.execute(sql, [e.eid])
        record = cursor.fetchone()
        # print("------Supervisor pick-----")
        # rec = record
        # print(rec)
        if e.eid in record:
         login = UserLogin(username=u.un, password=u.pw, eid=int(e.eid),supervisor=True)
         # print(login)
         return login


    @staticmethod
    def pickDepHead(ul):
        u = UserLogin.json_parse(ul)
        e = Employee()
        e.eid = int(u.eid)
        sql = "select * from \"Tuition\".department_heads where eid =%s "
        cursor = dbc.cursor()
        cursor.execute(sql, [e.eid])
        record = cursor.fetchone()
        rec = e.eid
        # print("------depHead pick-----")
        # print(rec)
        # print("should be printing L here")

        if rec in record:
            login =UserLogin(username=u.un, password=u.pw, eid=int(e.eid),depHead=True)
            # l = login
            # print(l.json())
            return login
        else:
            return ul


    @staticmethod
    def pickBenco(ul):
        u = UserLogin.json_parse(ul)
        e = Employee()
        e.eid = int(u.eid)
        # print(e.eid)
        sql = "select * from \"Tuition\".benifits_coordinators where id =%s"
        cursor = dbc.cursor()
        cursor.execute(sql, [e.eid])
        # print("------benco pick-----")
        record = cursor.fetchone()
        # print("-----Benco lines-----")
        # rec = record
        # print(rec)
        # print(record)
        if record:
            login = UserLogin(username=u.un, password=u.pw, eid=int(e.eid),benco=True)
            # print(login)
            return login.json()
        else:
           return ul

    @staticmethod
    def pickEmployee(ul):
        pass


def _test():
    uldao = LoginUserDAO()
    print(uldao.login(UserLogin("moonlight","moon")))


if __name__ == '__main__':
    _test()