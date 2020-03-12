import assets.Controller.UserController as UserController
import assets.Controller.APIController as APIController
import assets.Controller.HackingControlller as HackingControlller
import assets.View.keyboards as keyboards
import vk_api
import random
import json
import base64



class MainView():
    def __init__(self, session, vkID, event):
        self.session = session
        self.vkID = vkID
        self.apiController = APIController.APIController(session= self.session)
        self.hackingController = HackingControlller.HackingController(self.vkID, session)
        self.event = ''
    pass

    def CheckCurrentHackingParam(self):
        if self.hackingController.currenParametr:
            if self.hackingController.CheckCurrentParametr(json.loads(self.event.raw['object']['payload'])[self.hackingController.currenParametr]):
                self.session.method('messages.send', {
                    'message': f'Параметр указан верно\nОчков взлома {str(self.hackingController.hackingPoints)}/80',
                    'peer_id': self.vkID,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': keyboards.humanCreatorKB
                })                               
            else:
                self.session.method('messages.send', {
                    'message': f'Параметр указан неверно\nОчков взлома {str(self.hackingController.hackingPoints)}/80',
                    'peer_id': self.vkID,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': keyboards.humanCreatorKB
                })                               
        pass

    def ParseEvent(self, event):
        self.event = event
        if UserController.CheckRegistration(self.vkID):
            try:
                text =  event.raw['object']['text']
                decodedText = base64.b64decode(text)
                targetID = decodedText[len('TransferMoneyTo '):]
                if self.hackingController.FindVictim(int(targetID)):
                    self.session.method('messages.send', {
                        'message': 'Выбери способ атаки',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': keyboards.mainKB
                    })
                    pass
                else:
                    self.session.method('messages.send', {
                        'message': 'Неверный код',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000)
                    })
                    return True

            except Exception as e:
                if not self.hackingController.victimQR:
                    self.session.method('messages.send', {
                        'message': 'Неверный код',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000)
                    })
                    return True
                else:
                    if 'payload' in event.raw['object'].keys():
                        payload = json.loads(event.raw['object']['payload'])
                        if 'mainMenu' in payload.keys():
                            if payload['mainMenu'] == "wallet":
                                self.hackingController.hackingMode = 'wallet'
                                self.session.method('messages.send', {
                                    'message': 'Выбери параметр',
                                    'peer_id': self.vkID,
                                    'random_id': random.randint(1, 10000000000000),
                                    'keyboard': keyboards.humanCreatorKB
                                })
                            elif payload['mainMenu'] == 'profile':
                                self.hackingController.hackingMode = 'profile'
                                self.session.method('messages.send', {
                                    'message': 'Выбери параметр',
                                    'peer_id': self.vkID,
                                    'random_id': random.randint(1, 10000000000000),
                                    'keyboard': keyboards.humanCreatorKB
                                })
                            pass
                        elif 'button' in payload.keys():
                            if payload['button'] not in ['confirm', 'end']:
                                
                                self.hackingController.currenParametr = payload['button']
                                if self.hackingController.currenParametr == 'eyes':
                                    self.session.method('messages.send', {
                                        'message': 'Введите занчение',
                                        'peer_id': self.vkID,
                                        'random_id': random.randint(1, 10000000000000),
                                        'keyboard': keyboards.eyeColorKB
                                    })
                                elif self.hackingController.currenParametr == 'hair':
                                    self.session.method('messages.send', {                                    
                                        'message': 'Введите занчение',
                                        'peer_id': self.vkID,
                                        'random_id': random.randint(1, 10000000000000),
                                        'keyboard': keyboards.hairKB
                                    })
                                elif self.hackingController.currenParametr == 'district':
                                    self.session.method('messages.send', {                                                                      
                                        'message': 'Введите занчение',
                                        'peer_id': self.vkID,
                                        'random_id': random.randint(1, 10000000000000),
                                        'keyboard': keyboards.districtKB
                                    })
                                elif self.hackingController.currenParametr == 'height':
                                    self.session.method('messages.send', {                                                                      
                                        'message': 'Введите занчение',
                                        'peer_id': self.vkID,
                                        'random_id': random.randint(1, 10000000000000),
                                        'keyboard': keyboards.heightKB
                                    })
                                elif self.hackingController.currenParametr == 'work':
                                    self.session.method('messages.send', {                                                                      
                                        'message': 'Введите занчение',
                                        'peer_id': self.vkID,
                                        'random_id': random.randint(1, 10000000000000),
                                        'keyboard': keyboards.worksKB
                                    })
                                elif self.hackingController.currenParametr == 'name':
                                    self.session.method('messages.send', {                                       
                                            'message': "Введите имя",
                                            'peer_id': self.vkID,
                                            'random_id': random.randint(1, 10000000000000)
                                        }) 
                                   
                                
                            else:
                                if payload['button'] == 'confirm':
                                    if self.hackingController.TryToHack():
                                        return True
                                    else:
                                        self.session.method('messages.send', {
                                            'message': "Недостаточно очков взлома",
                                            'peer_id': self.vkID,
                                            'random_id': random.randint(1, 10000000000000),
                                            'keyboard': keyboards.humanCreatorKB
                                        }) 
                                else:
                                    self.session.method('messages.send', {                                       
                                            'message': "Введите имя",
                                            'peer_id': self.vkID,
                                            'random_id': random.randint(1, 10000000000000)
                                        }) 
                                    return True
                        else: #'eyeColor' in payload.keys():
                            a = list(payload.keys())[0]
                            self.hackingController.currenParametr = a
                            self.CheckCurrentHackingParam()
                        
                    else:
                        if self.hackingController.currenParametr:
                            if self.hackingController.CheckCurrentParametr(event.raw['object']['text']):
                                self.session.method('messages.send', {
                                    'message': f'Параметр указан верно\nОчков взлома {str(self.hackingController.hackingPoints)}/80',
                                    'peer_id': self.vkID,
                                    'random_id': random.randint(1, 10000000000000),
                                    'keyboard': keyboards.humanCreatorKB
                                })                               
                            else:
                                self.session.method('messages.send', {
                                    'message': f'Параметр указан неверно\nОчков взлома {str(self.hackingController.hackingPoints)}/80',
                                    'peer_id': self.vkID,
                                    'random_id': random.randint(1, 10000000000000),
                                    'keyboard': keyboards.humanCreatorKB
                                })                               
                        pass

                pass
        else:
            pass