from Classes.__init__c import Animal,Gato,Cachorro
if __name__=="__main__":
    gato1 = Gato("Mimi", "Persa","")
    gato1.get_informacoes()
    miado = gato1.miau()
    print(miado)

    cachorro1 = Cachorro("Rex", "Labrador","")
    cachorro1.get_informacoes()
    latido = cachorro1.latir()
    print(latido)
