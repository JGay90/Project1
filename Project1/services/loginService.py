from daos.LoginDAO import LoginUserDAO
from models.userLogin import UserLogin



class LoginService:
    ldao = LoginUserDAO()
    @staticmethod
    def login(json):
        return LoginUserDAO.login(json)

    @staticmethod
    def PickDepHead(ul):
        return LoginUserDAO.pickDepHead(ul)

    @staticmethod
    def pickBenco(ul):
        return LoginUserDAO.pickBenco(ul)
    @staticmethod
    def pickSuper(ul):
        return LoginUserDAO.pickSuper(ul)

    @staticmethod
    def pickEmployee(ul):
        return LoginUserDAO.pickEmployee(ul)