# carro recebo como parâmetro a velocidade máxima

class Carro:
    def __init__(self, limite=180):
        self.limite = limite
        self.velocidade = 0
    

    def acelerar(self, delta=5):
        self.velocidade += delta
        if self.velocidade >= self.limite:
            self.velocidade = self.limite
        
        return self.velocidade

    
    def frear(self, delta=5):
        self.velocidade -= delta
        if self.velocidade <= 0:
            self.velocidade = 0
        
        return self.velocidade


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(f'Velocidade atual: {c1.acelerar(9)}')

    for _ in range(10):
        print(f'Velocidade atual: {c1.frear(25)}')