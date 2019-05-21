import threading


class BankAccount(object):
    def __init__(self):
        self.is_open = False
        self.lock = threading.Lock()

    def get_balance(self):
        with self.lock:
            if self.is_open:
                return self.balance
            else:
                raise ValueError("Account is not open!")

    def open(self):
        if not self.is_open:
            self.is_open = True
            self.balance = 0.0
        else:
            raise ValueError("Account is not open!")

    def deposit(self, amount):
        with self.lock:
            if self.is_open and amount > 0:
                self.balance += amount
            else:
                raise ValueError("Account is not open!")

    def withdraw(self, amount):
        with self.lock:
            if self.is_open and amount > 0 and self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError("Withdrawal error!")

    def close(self):
        if self.is_open:
            self.is_open = False
        else:
            raise ValueError("Account is not open!")
