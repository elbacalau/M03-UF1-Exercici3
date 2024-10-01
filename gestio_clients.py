from client import Client

class GestioClients:
    def __init__(self) -> None:
        self.client = Client()
        

    def mostrarMenu(self):
        print("1. Afegir un client")
        print("2. Llistar Clients")
        print("3. Mostrar les dades d'un client amb plaç fix")
        print("4. Buscar Client")
        print("5. Eliminar un client")
        print("6. Sortir")

        while True:
            try:
                opcio = int(input("\nIntrodueix una opció: "))
                if opcio == 1:
                    self.client.afegirClient()
                elif opcio == 2:
                    self.client.llistarClients()
                elif opcio == 3:
                    self.client.mostrarQuantitatPlaçFix()
                elif opcio == 4:
                    self.client.buscarClient()
                elif opcio == 5:
                    self.client.eliminarClient()
                elif opcio == 6:
                    print("Sortint...")
                    break
                else:
                    print("Opció no vàlida, intenta-ho de nou.")
            except ValueError:
                print("Entrada no vàlida, introdueix un número.")
