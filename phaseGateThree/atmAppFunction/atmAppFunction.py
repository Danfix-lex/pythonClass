class AtmAppFunction:
    num_accounts = 4
    user_names = [""] * num_accounts
    user_pins = [""] * num_accounts
    user_date_of_births = [""] * num_accounts
    account_balances = [0.0] * num_accounts

    def create_accounts():
        for i in range(atmAppFunction.num_accounts):
            atmAppFunction.user_names[i] = f"User{i + 1}"
            atmAppFunction.user_pins[i] = "1234"
            atmAppFunction.user_date_of_births[i] = "01-01-2000"
            atmAppFunction.account_balances[i] = 0.0
        return "Accounts created successfully."

    def authenticate_user(entered_pin):
        for i, pin in enumerate(atmAppFunction.user_pins):
            if entered_pin == pin:
                return i
        return -1

    def display_options():
        print("\nATM Options:")
        print("1. Check account balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. Change pin")
        print("6. Exit")

    def process_choice(choice, account_index):
        if choice == 1:
            print(f"Your current balance is: {atmAppFunction.get_account_balance(account_index)}")
        elif choice == 2:
            deposit_amount = atmAppFunction.deposit_money(account_index, 100.0)
            print(f"Deposited: {deposit_amount}")
        elif choice == 3:
            withdrawn_amount = atmAppFunction.withdraw_money(account_index, 50.0)
            if withdrawn_amount > 0:
                print(f"Withdrawn: {withdrawn_amount}")
            else:
                print("Insufficient funds or invalid amount.")
        elif choice == 4:
            transferred_amount = atmAppFunction.transfer_money(account_index, 30.0)
            if transferred_amount > 0:
                print(f"Transferred: {transferred_amount}")
            else:
                print("Transfer failed.")
        elif choice == 5:
            change_pin_result = atmAppFunction.change_pin(account_index, "4321")
            print(change_pin_result)
        elif choice == 6:
            print("Exiting the ATM system. Goodbye!")
            return False
        else:
            print("Invalid option. Try again.")
        return True

    def deposit_money(account_index, deposit_amount):
        atmAppFunction.account_balances[account_index] += deposit_amount
        return deposit_amount

    def withdraw_money(account_index, withdraw_amount):
        if withdraw_amount > atmAppFunction.account_balances[account_index] or withdraw_amount <= 0:
            return -1
        else:
            atmAppFunction.account_balances[account_index] -= withdraw_amount
            return withdraw_amount

    def transfer_money(account_index, transfer_amount):
        if transfer_amount <= 0 or transfer_amount > atmAppFunction.account_balances[account_index]:
            return -1
        else:
            atmAppFunction.account_balances[account_index] -= transfer_amount
            return transfer_amount

    def change_pin(account_index, new_pin):
        atmAppFunction.user_pins[account_index] = new_pin
        return "Pin changed successfully."

    def get_account_balance(account_index):
        return atmAppFunction.account_balances[account_index]
