
class Product:
	def __init__(self, design, size_amount, price, raw_material, benefit, useful_life, name):
		self.design = design
		self.size_amount = size_amount
		self.price = price
		self.raw_material = raw_material
		self.benefit = benefit
		self.useful_life = useful_life
		self.name=name

	def __str__(self):
		return "The product is a "+ self.name + ". The design is "+self.design+", the size/amount is "+self.size_amount+" with a "+self.price+" price, the raw material is "+self.raw_material+", the benefit is "+self.benefit+" and the useful life is "+self.useful_life
	
	def eval_product(self):
		"""Evaluates the correct creation of determinate instance of the Product class"""

		if self.design != "sober" and self.design != "shocking":
			raise Exception ("The design must be sober or shocking")

		elif self.size_amount != "little" and self.size_amount != "median" and self.size_amount != "big":
			raise Exception ("The size/amount must be little, median or big")

		elif self.price != "cheap" and self.price != "normal" and self.price != "expensive":
			raise Exception ("The price must be cheap, normal or expensive") 

		elif self.benefit != "mellability" and self.benefit != "delivery speed" and self.benefit != "delight": 
			raise Exception ("The benefit must be mellability, delivery speed or delight")

		elif not "months" in self.useful_life and not self.useful_life[0].isdigit():
			raise Exception ("The usefull ife must be expressed in months")

	def select_attribute(self):
		"""Select a random attribute and generate random innovations based on the design, the raw ingredients, the benefits, 
		the effort reduction, the price reduction, the useful life, increase or reduction of any characteristic
		Always having clair that the succes of a product is based in the of reduction of a determinate pain of the costumer"""
		import random
		focus=random.randrange(5)
		print (focus)
		if focus == 0:
			if self.design == "sober":
				product = Product("shocking",self.size_amount,self.price,self.raw_material,self.benefit,self.useful_life,self.name)
			product = Product("sober",self.size_amount,self.price,self.raw_material,self.benefit,self.useful_life,self.name)
		elif focus == 1:
			if self.size_amount == "little":
				product = Product(self.design,"median",self.price,self.raw_material,self.benefit,self.useful_life,self.name)
			elif self.size_amount == "median":
				product = Product(self.design,"little",self.price,self.raw_material,self.benefit,self.useful_life,self.name)
			product = Product(self.design,"median",self.price,self.raw_material,self.benefit,self.useful_life,self.name)
		elif focus == 2:
			if self.price == "cheap":
				product = Product(self.design,self.size_amount,"expensive",self.raw_material,self.benefit,self.useful_life,self.name)
			elif self.price == "normal":
				product = Product(self.design,self.size_amount,"cheap",self.raw_material,self.benefit,self.useful_life,self.name)
			product = Product(self.design,self.size_amount,"normal",self.raw_material,self.benefit,self.useful_life,self.name)
		elif focus == 3:
			product = Product(self.design,self.size_amount,self.price,"...",self.benefit,self.useful_life,self.name)
		elif focus == 4:
			if self.design == "mellability":
				product = Product(self.design,self.size_amount,self.price,self.raw_material,"delight",self.useful_life,self.name)
			elif self.design == "delight":
				product = Product(self.design,self.size_amount,self.price,self.raw_material,"delivery speed",self.useful_life,self.name)
			product = Product(self.design,self.size_amount,self.price,self.raw_material,"mellability",self.useful_life,self.name)
		elif focus == 5:
			months = int(self.useful_life) * 5
			product = Product(self.design,self.size_amount,self.price,self.raw_material,self.benefit,str(months))
		
		return product
	
	def loop_variations(product):
		for p in range (0,10):
			product.select_attribute()
			product=product
			print(product)

table = Product("shocking","little","cheap","wood","delight","800 months","table")
cereal = Product("shocking","little","cheap","flakes","mellability","3 months","cereal")
print (mesa)
r = loop_variations(table)
print (r)






"""
complex_product = [
	("ciber","coffee"),("bar of", "cereal"),("shopping","filling station"),("yogurt","defense"),("chocolate","surpise"),
	("shop","virtual"),("house","car"),("reality","show"),("sponsor a","child"),("tape deck","headphones")
"""