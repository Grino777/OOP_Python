from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper()

    @staticmethod
    def check_card_number(number: str) -> bool:
        DIGITS = digits
        number = ''.join(number.split('-'))
        if len(number) == 16:
            for i in number:
                if i not in digits:
                    return False
            return True
        return False

    @classmethod
    def check_name(cls, name: str) -> bool:
        name = name.split(' ')
        if len(name) == 2:
            for i in name:
                for j in i:
                    if j not in cls.CHARS_FOR_NAME:
                        return False
            return True
        return False

is_name = CardCheck.check_name("SERGEI BALAKIREV")
is_number = CardCheck.check_card_number("1234-5678-9012-0000")
print(is_number)