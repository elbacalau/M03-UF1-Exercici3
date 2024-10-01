from validaciones import validar_nom_cognom, validar_telefon, validar_quantitat_diners
from compte import Fixe, Estalvi


class Client:
    def __init__(self) -> None:
        self.clients = []

    def afegirClient(self):
        nom = input("Nom: ")
        cognom = input("Cognom: ")
        telefon = input("Telefon: ")
        quantitatDiners = input("Quantitat Diners: ")
        tipusConte = input("Tipus de compte (fixe/estalvi): ").lower()
        
        
        if not validar_nom_cognom(nom, cognom):
            print("Ha de contenir només lletres.")
            return
        
        if not validar_telefon(telefon):
            print("Telèfon ha de ser un número vàlid amb almenys 5 dígits.")
            return
        
        if not validar_quantitat_diners(quantitatDiners):
            print("La quantitat de diners ha de ser un número no negatiu.")
            return

        quantitatDiners = float(quantitatDiners) 
        
        compte = None
        if tipusConte == "fixe":
            plaç = int(input("Plaç (només per comptes fixos): "))
            interes = float(input("Interes (només per comptes fixos): "))  
            
            compte = Fixe(saldo=quantitatDiners, plaç=plaç, interes=interes, client={"nom": nom, "cognom": cognom})
        
        elif tipusConte == "estalvi":
            compte = Estalvi(saldo=quantitatDiners, client={"nom": nom, "cognom": cognom})
        
        else:
            print("Tipus de compte no vàlid.")
            return
        
        client = {
            "nom": nom,
            "cognom": cognom,
            "telefon": telefon,
            "compte": compte
        }
        
        self.clients.append(client)
        print(f"Client {nom} afegit correctament amb un compte {tipusConte}.")

    def llistarClients(self):
        if not self.clients:
            print("No hi ha clients per llistar.")
            return
        for client in self.clients:
            print(f"{client['nom']} {client['cognom']}")
            client['compte'].imprimirDadesCompte()
    
    def mostrarQuantitatPlaçFix(self):
        nom = input("Introdueix el nom del client: ")
        
        if not nom.isalpha():
            print("Nom ha de contenir només lletres.")
            return

        for client in self.clients:
            if client.get("nom").lower() == nom.lower():
                compte = client.get("compte")
                if isinstance(compte, Fixe):
                    compte.mostrarInformacio()
                else:
                    print(f"El client {client['nom']} no té una compte fixe.")
                return
        
        print("No s'ha trobat el client.")

    def buscarClient(self):
        nom = input("Introdueix el nom del client: ").lower()
        
        for client in self.clients:
            if client.get("nom").lower() == nom:
                client['compte'].imprimirDadesCompte()
                return
        print("No s'ha trobat el client")

    def eliminarClient(self):
        nom = input("Introdueix el nom del client: ").lower()
        
        for client in self.clients:
            if client.get("nom").lower() == nom:
                self.clients.remove(client)
                print(f"Client {client['nom']} eliminat correctament.\n")
                return
        print("No s'ha trobat el client.\n")
