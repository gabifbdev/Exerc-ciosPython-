largura  = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: ' ))
resultado = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m'.format(largura, altura, resultado))
tinta = resultado / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))

