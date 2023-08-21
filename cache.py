class Memoria:
    def read(self, endereco):
        pass

    def write(self, endereco, valor):
        pass

class RAM(Memoria):
    def __init__(self, tamanho):
        self.memoria = [0] * tamanho

    def read(self, endereco):
        return self.memoria[endereco]

    def write(self, endereco, valor):
        self.memoria[endereco] = valor

class CacheSimples(Memoria):
    def __init__(self, tamanho, ram):
        self.tamanho = tamanho
        self.ram = ram
        self.memoria = [None] * tamanho

    def read(self, endereco):
        if self.memoria[endereco] is None:
            self.memoria[endereco] = self.ram.read(endereco)
        return self.memoria[endereco]

    def write(self, endereco, valor):
        self.memoria[endereco] = valor
        self.ram.write(endereco, valor)

class CPU:
    def __init__(self, memoria, io):
        self.memoria = memoria
        self.io = io

    def run(self, endereco):
        try:
            instrucao = self.memoria.read(endereco)
            # Lógica para executar a instrução
            pass
        except EnderecoInvalido as e:
            print("Endereço inválido:", e.ender, file=sys.stderr)

try:
    io = IO(sys.stdin, sys.stdout)
    ram = RAM(7)
    cache = CacheSimples(8, ram)
    cpu = CPU(cache, io)

    inicio = 10
    cache.write(inicio, 118)
    cache.write(inicio + 1, 130)
    cpu.run(inicio)
except EnderecoInvalido as e:
    print("Endereço inválido:", e.ender, file=sys.stderr)
