class Member:
    def __init__(self, name, email, is_premium=False):
        self.name = name
        self.email = email
        self.is_premium = is_premium

    def calculate_late_fee(self, days_late):
        if self.is_premium:
            return days_late * 2
        return days_late * 5

