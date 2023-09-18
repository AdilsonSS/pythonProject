class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor 
        self.altura = altura
        self.prprofundidade = profundidade
        self.largura = largura
        
    
        
        
controle_remoto = ControleRemoto('cinza', '10', '3', '3')
controle_remto2 = ControleRemoto('preto','15','2','2')

print(controle_remoto.cor)
print(controle_remto2.cor)