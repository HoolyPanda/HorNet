import assets.Controller.APIController as APIController


class APIView:
    def __init__(self, session, vkID):
        self.session = session
        self.vkID = vkID
        self.APIController = APIController.APIController(self.session)

    def ParseEvent(self, event):
        a = 0
        pass
