class PasswordChecker:
    """Задача: password_checker"""
    def __init__(self, pwd: str):
        self.pwd = pwd

    def is_strong(self) -> bool:
        """Длина >= 8 и есть цифра"""
        if len(self.pwd) >= 8:
            a=0
            for i in range(10):
                if str(i) in self.pwd:
                    a=1
            if a==1:return True
            else:return False
        else:return False