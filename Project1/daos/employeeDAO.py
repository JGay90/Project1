from exceptions.resource_not_found import ResourceNotFound
from utils.db_connection import connection as dbc
from models.employee import Employee

class EmployeeDAO:
    @staticmethod
    def get_employee_by_id(id):
        sql = "Select * from \"Tuition\".employees where id = %s"
        cursor = dbc.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()

        if record:
            return Employee(record[0],record[1],record[2],record[3],record[4],record[5],record[6])
        else:
            raise ResourceNotFound(f"Employee with id {id} Not found")
    @staticmethod
    def get_all_employees():
        sql = "Select * from \"Tuition\".employees"
        cursor = dbc.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        employee_list= []
        for record in records:
            e = Employee(record[0], record[1], record[2], record[3],record[4], record[5], record[6])
            employee_list.append(e.json())

        return employee_list



def _test():
    edao = EmployeeDAO
    employees = edao.get_all_employees()
    print(employees)
    print(edao.get_employee_by_id(2).json())

if __name__ == '__main__':
    _test()