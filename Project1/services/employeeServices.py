from daos.employeeDAO import EmployeeDAO

class EmployeeService:
    edao = EmployeeDAO

    @classmethod
    def all_employees(self):
        return EmployeeDAO.get_all_employees()
    @classmethod
    def get_by_id(cls,id):
        return cls.edao.get_employee_by_id(id)
    @staticmethod
    def update_employee(employee):
        EmployeeDAO.update_employee(employee)


