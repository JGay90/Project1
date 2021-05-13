class UserLogin:
    def __init__(self,username= "", password = "", eid = 0,supervisor = False, depHead = False, benco = False):
        self.un = username
        self.pw = password
        self.eid = eid
        self.supervisor = supervisor
        self.depHead = depHead
        self.benco = benco


    def json(self):
        return {
        "username":self.un,
        "password":self.pw,
        "eids":self.eid,
        "supervisor":self.supervisor,
        "depHead": self.depHead,
        "benco":self.benco
        }

    def __repr__(self):
        return (dict(un=self.un,pw=self.pw,eids=self.eid,supervisor=self.supervisor,depHead=self.depHead,benco=self.benco))

    @staticmethod
    def json_parse(json):
        ul = UserLogin()
        # print(json.values())
        # print(type(json))
        ul.un = json["username"]
        ul.pw = json["password"]
        ul.eid = json["eids"]
        ul.supervisor = json["supervisor"] if"supervisor" in json else False
        ul.depHead = json["depHead"] if"depHead" in json else False
        ul.benco = json["benco"] if"benco" in json else False
        return ul



def _test():
    ul = UserLogin("moonlight","moon")
    json= ul.json()
    print(ul.json_parse(json).__repr__())

if __name__ == '__main__':
    _test()