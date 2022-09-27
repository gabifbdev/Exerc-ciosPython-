produto = float(input('Insira o preço do produto para calcular o desconto R$: '))


desconto = produto - (produto / 100 * 5)


print('O valor com desconto é de R$ {} '.format(desconto))