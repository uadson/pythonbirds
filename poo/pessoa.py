class Pessoa:
	def __init__(self, nome=None, idade=37, *filhos):
		# atributo de instancia
		self.nome = nome
		self.idade = idade
		# atributo complexo
		self.filhos = list(filhos)
	
	# método 
	def cumprimentar(self):
		return f'Olá {id(self)}'


if __name__ == '__main__':
	feitosa = Pessoa(nome='Feitosa')
	uadson = Pessoa(nome='Uadson')
	print(Pessoa.cumprimentar(uadson))
	# id
	print(id(uadson))
	# ou
	print(uadson.cumprimentar())
	print(feitosa.nome)
	# alterando o atributo
	uadson.nome = 'Castro'
	print(uadson.nome)
	print(uadson.idade)
	print(uadson.filhos)
	for filho in uadson.filhos:
		print(filho.nome)


 
