from controllers import LoginController as lc
from controllers import employeeController as ec
from controllers import reimbursementController as rc


def route(app):
    # Calls all other other controllers
    lc.route(app)
   # ec.route(app)
    rc.route(app)