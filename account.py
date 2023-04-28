class Account:
    """
    A class representing details for a person's account object
    """

    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of a person's account object
        :param: account_name: Person's name on the account.
        :param account_balance: Person's balance on the account.
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount) -> float:  # increases account balance
        """
        Constructor to create the state of a person's deposit
        :param: amount: Person's balance amount on the account, when deposited.
        """
        if self.__account_balance >= 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:  # decreases account balance
        """
        Constructor to create the state of a person's withdraw.
        :param: amount: Person's balance amount on the account, when withdrawn
        """
        if self.__account_balance > 0:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Constructor to return the account's balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Constructor to return the account's name.
        """
        return self.__account_name