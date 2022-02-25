'''
a partir do menor termo são feitas tentativas de divisão na função calc(),
[número da lista fornecida] % [número suposto], caso o número suposto não
seja um divisor comum entre todos os elementos, ou seja, em alguma divisão
o resto foi maior que 0, então a função calc() é chamada novamente, desta
vez com o número suposto uma unidade a menos que o anterior, esse loop
segue em execução até que o número suposto seja divisível por todos os
elementos da lista fornecida, ou seja, o resto de todas as divisões foi
igual a 0, descobrindo assim o MDC.
'''


def mdc(numeros):
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 \
            else calc(divisor - 1)
    return calc(min(numeros))


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1
