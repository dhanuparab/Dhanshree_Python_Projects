from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, username, pin):
        self._username = username   
        self.__pin = pin            
        self.balance = 0.0          
        self.transaction_history = []  

    @abstractmethod
    def calculate_balance(self):
        pass

    def check_balance(self):
        return self.balance

    def _get_pin(self): 
        return self.__pin

 
class User(BankAccount):
    def __init__(self, username, pin):
        super().__init__(username, pin)

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Deposit operation completed.")

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
        finally:
            print("Withdrawal operation completed.")

    def show_transaction_history(self):
        return self.transaction_history

    def calculate_balance(self):
        return self.balance  
    def __del__(self):
        print(f"User {self._username} account is deleted!")


class ATM:
    def __init__(self):
        self.users = {}  
        self.current_user = None

    def create_user(self, username, pin):
        try:
            if username in self.users:
                raise ValueError("Username already exists.")
            self.users[username] = User(username, pin)
            print(f"User {username} created successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def login(self, username, pin):
        try:
            if username not in self.users:
                raise ValueError("User not found.")
            if self.users[username]._get_pin() != pin:
                raise ValueError("Incorrect PIN.")
            self.current_user = self.users[username]
            print(f"Welcome, {username}!")
        except ValueError as e:
            print(f"Error: {e}")

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Logout")

    def run(self):
        while True:
            action = input("\nDo you want to (1) Create User or (2) Login? ")
            if action == '1':
                username = input("Enter username: ")
                pin = input("Enter PIN: ")
                self.create_user(username, pin)
            elif action == '2':
                username = input("Enter username: ")
                pin = input("Enter PIN: ")
                self.login(username, pin)
                if self.current_user:
                    while True:
                        self.display_menu()
                        choice = input("Select an option (1-6): ")
                        if choice == '1':
                            print(f"Your current balance is: ${self.current_user.check_balance():.2f}")
                        elif choice == '2':
                            amount = float(input("Enter amount to deposit: $"))
                            self.current_user.deposit(amount)
                        elif choice == '3':
                            amount = float(input("Enter amount to withdraw: $"))
                            self.current_user.withdraw(amount)
                       
                        elif choice == '4':
                            print("\nTransaction History:")
                            for transaction in self.current_user.show_transaction_history():
                                print(transaction)
                        elif choice == '5':
                            print("Logging out...")
                            self.current_user = None
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")
            else:
                print("Invalid action. Please select 1 or 2.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()

