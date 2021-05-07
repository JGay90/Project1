class Employee:
    def __init__(self, id = 0,first_name = "", last_name = "", supervisor_id = 0, department_head = 0, department = 0,tuition_available = True):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.supervisor_id = supervisor_id
        self.department_head = department_head
        self.department = department
        self.tuition_available = tuition_available

    def __repr__(self):
        return repr(dict(id=self.id,first_name = self.first_name,last_name = self.last_name,supervisor = self.supervisor_id,department_head = self.department_head, department = self.department, tuition_available = self.tuition_available))

    def json(self):
        return {
            "ID" : self.id,
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Supervisor": self.supervisor_id,
            "Department Head": self.department_head,
            "Department" : self.department

        }
    @staticmethod
    def json_parse(json):
        employee = Employee()
        employee.id = json["ID"]if "ID" in json else 0
        employee.first_name = json["First Name"]
        employee.last_name = json["Last Name"]
        employee.supervisor_id = json["Supervisor"]
        employee.department_head = json["Department Head"]
        employee.department = json["Department"]

        return employee