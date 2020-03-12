import os.path


def CheckRegistration(vkID: int):
    a = os.listdir('../AnthillPay/DB')
    if os.path.exists(f'../AnthillPay/DB/{str(vkID)}.json'):
        return True
    else:
        return False