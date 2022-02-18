class bank:
	def __init__(self,balance,owner):
		self.balance = balance
		self.owner = owner
	def deposit (self,money_add):
		self.balance += money_add
		return self.balance

	def withdraw(self,money_minus):
		if self.balance < money_minus:
			return "error"
		else :	
			self.balance -= money_minus
			return self.balance
p1 = bank(int(input("Your balance ")),input("Enter your name "))


print(f'If you want to add a deposit type "1" ')
print(f'If you want to withdraw money type "2" ')
enter = int(input())

if enter == 1: 
	mo = int(input("How much money to add "))
	print(f'Your balance - {p1.deposit(mo)}')
else :
	mw = int(input("How much money to withdraw "))
	if p1.withdraw(mw) == "error":
		print("Insufficient funds to withdraw services")
	else :	
		print(f'Your balance - {p1.withdraw(mw)}') 	


