class Stock():
	def __init__(self, price_buy, price_sell, qty, fee_rate = 0.05 / 100):
		self.price_buy = price_buy
		self.price_sell = price_sell
		self.qty = qty
		self.fee_rate = fee_rate

		fee_buy = self.price_buy * self.qty * self.fee_rate
		fee_sell = self.price_sell * self.qty * self.fee_rate
		self.fee = fee_buy + fee_sell
		
		self.profit = (self.price_sell - self.price_buy) * self.qty - self.fee
		self.prc = (self.price_sell - self.price_buy) / self.price_buy * 100

		self.min_price = round(self.price_buy * (1 + self.fee_rate) / (1 - self.fee_rate), 2) + 0.01

		print("\tprofit = {0}\n\tfee = {1}\n\t% = {2}\n\tmin price = {3}"
				.format(self.profit, self.fee, self.prc, self.min_price))

# myStock = Stock(152.31, 152, 120, 0.05 / 100)
myStock = Stock(475.5, 315, 10, 0.025 / 100)
