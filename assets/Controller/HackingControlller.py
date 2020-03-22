import base64
import json
import os
import random

class HackingController():
    def __init__(self, vkID, session):
        self.session = session
        self.victimQR = None
        self.hackingPoints = 0
        self.currenParametr = ''
        self.valuebleParams = ['district', 'name']
        self.hackingMode = ''
        self.hackedParams = []
        self.vkID = vkID
        pass

    def ParseEvent(self):
        pass

    def FindVictim(self, victimQR: int):
        path = '../AnthillPay/DB/'
        for f in os.listdir(f'{path}'):
            if not os.path.isdir(f'{path}{f}'):
                victim = json.loads(open(f'{path}{f}', 'r').read())
                if victim['id'] == victimQR:
                    self.victimQR = victimQR
                    return True
        return False

    def LoadVictim(self):
        path = '../AnthillPay/DB/'
        for f in os.listdir(f'{path}'):
            if not os.path.isdir(f'{path}{f}'):
                victim = json.loads(open(f'{path}{f}', 'r').read())
                if victim['id'] == self.victimQR:
                    return victim

    def CheckCurrentParametr(self, value):
        victim = self.LoadVictim()
        if victim:
            if self.currenParametr not in self.hackedParams:
                if self.currenParametr in victim.keys():
                    if victim[self.currenParametr] == value.lower():
                        if self.currenParametr in self.valuebleParams:
                            self.hackingPoints += 30
                        else:
                            self.hackingPoints += 5
                        self.hackedParams.append(self.currenParametr)
                        self.currenParametr = None
                        return True
        self.hackingPoints -= 10
        if self.hackingPoints <= 0:
            self.HackProfile()
            return False
        else:
            return True

    def HackMoney(self):
        v = self.LoadVictim()
        amount = round(v['money'] / 3)
        payload = {'action': 'hack', 
            'type':'money', 
            'amount': amount, 
            'hackerVkID': self.vkID, 
            'victimID': self.victimQR, 
            'hackingPoints': self.hackingPoints
        }
        payload = json.dumps(payload)
        self.session.method('messages.send', {
            'message': payload,
            'peer_id': 2000000001,
            'random_id': random.randint(1, 10000000000000)
        }) 
        pass

    def HackProfile(self):
        v = self.LoadVictim()
        payload = {
            'action': 'hack',
            'type': 'profile',
            'hackerVkID': self.vkID,
            'victimID': self.victimQR,
            'hackingPoints': self.hackingPoints
        }
        payload = json.dumps(payload)
        self.session.method('messages.send', {
            'message': payload,
            'peer_id': 2000000001,
            'random_id': random.randint(1, 10000000000000)
        }) 
        self.session.method('messages.send', {
            'message': f'Взлом цели {self.victimQR} провален.\nФайерволл успел собрать твой цифровой след',
            'peer_id': self.vkID,
            'random_id': random.randint(1, 10000000000000)
        })


    def TryToHack(self):
        if self.hackingMode == 'wallet':
            if self.hackingPoints >= 20:
                self.HackMoney()
                return True
        if self.hackingMode == 'profile':
            if self.hackingPoints >= 70:
                self.HackProfile()
                return True
            pass
        return False