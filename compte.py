class Compte:
    def __init__(self, saldo, client) -> None:
        self.saldo = saldo
        self.client = client
        
    def imprimirDadesCompte(self):
        print(f"Client: {self.client['nom']}, {self.client['cognom']}")
        print(f"Saldo: {self.saldo}")

class Fixe(Compte):
    def __init__(self, saldo, plaç, interes, client) -> None:
        super().__init__(saldo, client)
        self.plaç = plaç
        self.interes = interes
        
    def obternirImport(self):
        
        return (self.saldo * self.interes) / 100

    def mostrarInformacio(self):
        
        print(f"Client: {self.client['nom']}, {self.client['cognom']}")
        print(f"Saldo: {self.saldo}")
        print(f"Plaç: {self.plaç}")
        print(f"Interes: {self.interes}")
        print(f"Import: {self.obternirImport()}")

class Estalvi(Compte):
    def __init__(self, saldo, client) -> None:
        super().__init__(saldo, client)

    def mostrarEstalvi(self):
        print(f"Client: {self.client['nom']}, {self.client['cognom']}")
        print(f"Saldo: {self.saldo}")
