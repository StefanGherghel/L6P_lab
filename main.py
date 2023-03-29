class Celula:
    def get_nume(self)->str:
        pass

class FibraMusculara(Celula):
    masa_musc_totala = 0

    def __init__(self,num,masa):
        self.nume = num
        self.masa_musculara = masa
        type(self).masa_musc_totala+=masa

    def get_nume(self)->str:
        return self.nume

    def get_masa_musculara(self)->float:
        return self.masa_musculara

class FibraNervoasa(Celula):
    lung_totala = 0
    def __init__(self,num,len):
        type(self).lung_totala += len
        self.nume = num
        self.lungime = len
    def get_nume(self)->str:
        return self.nume
    def get_lungime(self)->float:
        return self.lungime

class MuschiGeneric:
    def __init__(self, num, mass, scope):
        self.fibre = []
        self.nume = num
        self.masa_musculara = mass
        self.scop = scope
    def add_Fibra(self, Fibra:FibraMusculara):
        self.fibre.append(Fibra)
    def get_nume(self):
        for f in self.fibre:
            print("Masa musculara a muschilor ["+f.get_nume()+"] : "+str(f.get_masa_musculara()))
        print("Masa totala a "+self.nume+" este: "+str(self.masa_musculara)+" cu scopul: "+self.scop)
    def get_masa_musc_totala(self):
        return FibraMusculara.masa_musc_totala


class TrunchiNervos():
    def __init__(self, num, lung, specializ):
        self.nervi = []
        self.nume = num
        self.lungime = lung
        self.scop = specializ
    def add_Nerv(self, nerv:FibraNervoasa):
        self.nervi.append(nerv)
    def get_nume(self):
        for f in self.nervi:
            print("Lungimea sistemului nervos ["+f.get_nume()+"] : "+str(f.get_lungime()))
        print("Lungimea axonilor din "+self.nume+" este: "+str(self.lungime)+" cu scopul: "+self.scop)
    def get_lungimea_totala(self):
        return FibraNervoasa.lung_totala

def getFilteredMuscles(lista,scop):
    tmp = []
    for f in lista:
        if f.scop == scop:
            tmp.append(f)
    return tmp

if __name__=='__main__':
    MG = MuschiGeneric("biceps stang",100.12,"intindere")
    MG.add_Fibra(FibraMusculara("biceps",10.134))
    MG.add_Fibra(FibraMusculara("triceps", 112.564))
    MG.get_nume()
    print(str(MG.get_masa_musc_totala())+" este masa musculara totala")

    print("\n======================================================\n")

    TN = TrunchiNervos("sistemul nervos",120, "inervare")
    TN.add_Nerv(FibraNervoasa("maduva", 10.134))
    TN.add_Nerv(FibraNervoasa("nerv optic", 56.23))
    TN.get_nume()
    print(str(TN.get_lungimea_totala()) + " este lungimea nervoasa totala")

    print("\n======================================================\n")

    VMG = []
    VMG.append(MG)
    VMG.append(MuschiGeneric("Biceps drept",100.12,"relaxare"))
    VMG.append(MuschiGeneric("Gamba", 43.2, "intindere"))
    VMG.append(MuschiGeneric("Pectoral", 12.324, "relaxare"))

    tmp = getFilteredMuscles(VMG,"relaxare")
    for i in tmp:
        i.get_nume()