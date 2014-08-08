"""
Bank account manager. Create a class called Account which will be an
abstract class for three other classes called CheckingAccount,
SavingsAccount and BusinessAccount.

For shortening i simply crate one class which inherits from Account
"""


class Account(object):
    def __init__(self, id):
        self.id = id


class CheckingAccount(Account):
    def __init__(self, id, name):
        Account.__init__(self, id)
        self.name = name

    def __str__(self):
        return "%s, %s" % (self.id, self.name)

testAc = CheckingAccount(5, "10")
print testAc
