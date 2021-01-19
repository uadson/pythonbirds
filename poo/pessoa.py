class Pessoa:
	def __init__(self, nome=None, idade=37):
		self.nome = nome
		self.idade = idade

	def cumprimentar(self):
		return f'Olá {id(self)}'


if __name__ == '__main__':
	p = Pessoa('Feitosa')
	print(Pessoa.cumprimentar(p))
	# id
	print(id(p))
	# ou
	print(p.cumprimentar())
	print(p.nome)
	# alterando o atributo
	p.nome = 'Uadson'
	print(p.nome)
	print(p.idade)


 
