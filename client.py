from validaciones import validar_nom_cognom, validar_telefon, validar_quantitat_diners
from compte import Compte, Fixe, Estalvi


class Client:
    def __init__(self) -> None:
        self.clients = []

    def afegirClient(self):
        nom = input("Nom: ")
        cognom = input("Cognom: ")
        telefon = input("Telefon: ")
        quantitatDiners = input("Quantitat Diners: ")
        tipusConte = input("Tipus de compte (fixe/estalvi): ")

        # validacions
        if not validar_nom_cognom(nom, cognom):
            print("Nom i cognom han de contenir només lletres.")
            return
        
        if not validar_telefon(telefon):
            print("Telèfon ha de ser un número vàlid amb almenys 5 dígits.")
            return
        
        if not validar_quantitat_diners(quantitatDiners):
            print("La quantitat de diners ha de ser un número no negatiu.")
            return

        quantitatDiners = float(quantitatDiners) 
        
        if tipusConte == "fixe":
            compte = Fixe(saldo=quantitatDiners, plaç=12, interes=5.0, client={"nom": nom, "cognom": cognom})
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
        print(f"Client {nom} afegit correctament.")

    def llistarClients(self):
        if not self.clients:
            print("No hi ha clients per llistar.")
            return
        for client in self.clients:
            print(f"{client['nom']} {client['cognom']}")
            
            # compte = Fixe() 
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
                    quant = compte.obternirImport()
                    print(f"El client {nom} té {quant} € en el plaç fix.")
                else:
                    print("El client no té una compte fixe.")
                return
        
        print("No s'ha trobat el client.")

    def buscarClient(self):
        nom = input("Introdueix el nom del client: ")
        for client in self.clients:
            if client.get("nom").lower() == nom.lower():
                r = Compte(client.get("compte").saldo, client)
                r.imprimirDadesCompte()
                return
        print("No s'ha trobat el client")

    def eliminarClient(self):
        nom = input("Introdueix el nom del client: ")
        for client in self.clients:
            if client.get("nom").lower() == nom.lower():
                self.clients.remove(client)
                print(f"Client {nom} eliminat correctament.\n")
                return
        print("No s'ha trobat el client.\n")
