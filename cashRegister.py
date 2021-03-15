from pyfiglet import figlet_format 

class Cash_Register:
	def __init__(self, discount = 0):
		self.total = 0
		self.subTotal = 0
		self.discount = discount
		self.items = {}
		self.transaction = []

	def add_item(self, title, price, q=1):
		self.total += price * q
		self.subTotal += price * q
		for x in range(q):
			self.items[f'{q}x {title}'] = price * q
		self.transaction = [title, price, q]
		
		
	def sub_total(self):
		print('-' * 30)
		print(f'Subtotal: ${self.subTotal:,.2f}')
		
	def list_items(self):
		for x in self.items:
			print(f'{x} - ${self.items[x]:,.2f}')

	def apply_discount(self):
		self.total -= (self.total * self.discount) / 100.00
		if self.discount == 0:
			print(f"\nThere is no discount to apply, the total comes to ${self.total:,.2f}.")
		else:
			print(f"\nAfter the {self.discount}% discount, the total comes to ${self.total:,.2f}.")

	def void_last_transaction(self):
		self.total -= self.transaction[1] * self.transaction[2]
		self.subTotal -= self.transaction[1] * self.transaction[2]
		self.items.popitem()
		



print(figlet_format(" Shopping"))
print(figlet_format(" " * 13 + "Cart"))
trans_1 = Cash_Register(20)
trans_1.add_item("mouse", 16.99)
trans_1.add_item("books", 5.99, 3)
trans_1.add_item("macbook air", 999.95)
#trans_1.void_last_transaction()
trans_1.list_items()
trans_1.sub_total()
trans_1.apply_discount()
#print(len(trans_1.items))

