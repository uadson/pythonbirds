class Pessoa:
	def cumprimentar(self):
		return f'Olá {id(self)}'


if __name__ == '__main__':
	p = Pessoa()
	print(Pessoa.cumprimentar(p))
	# id
	print(id(p))
	# ou
	print(p.cumprimentar())


 
