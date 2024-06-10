menu = """

[d] Deposit
[w] Withdraw
[e] Extract
[q] Quit

--> """

balance = 0
limit = 500
extract = ""
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

while True:
  option = input(menu)

  if option == "d":
    value = float(input("Enter the deposit amount --> "))
    if value > 0:
      balance += value
      extract += f"Deposit --> $ {value:.2f}\n"
    else:
      print("The number entered is invalid.")

  elif option == "w":
    value = float(input("Enter the withdrawal amount --> "))
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = number_of_withdrawals >= WITHDRAWAL_LIMIT
    if exceeded_balance:
      print("Transaction failed, you don't have enough balance.")
    elif exceeded_limit:
      print("Operation failed, withdrawal amount exceeds limit.")
    elif exceeded_withdrawals:
      print("Operation failed, maximum number of withdrawals exceeded.")
    elif value > 0:
      balance -= value
      extract += f"Withdraw --> $ {value:.2f}\n"
      number_of_withdrawals += 1
    else:
      print("Operation failed, the number entered is invalid.")

  elif option == "e":
    print("\n===EXTRACT===")
    print("No transactions were made." if not extract else extract)
    print(f"\nBalance --> $ {balance:.2f}")
    print("=============")
  
  elif option == "q":
    break

  else:
    print("Invalid operation")


    
    
    