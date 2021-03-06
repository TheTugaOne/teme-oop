'''
pentru a stoca conturile bancare folosesc un dictionar in care , la fiecare cheie se afla o lista cu 2 valori :
-parola atribuita cheii (sau numele utilizatorului)
-suma de bani depusa in cont
ex: conturi["andrei"][0] = masina33 (parola)
    conturi["andrei"][1] = 150 (sold in lei)
'''
conturi = {}
'''
am adaug un "test" in dictionar deoarece la un moment dat iterez prin el si se poate sa apara o eroare in cazul in care
este gol
'''
conturi["test"] = "test"
#folosesc o singura clasa in care sunt incluse toate functiile
class Banca():
    #fiecare cont are un nume de utilizator , parola si sold (initializat cu 0)
    def __init__(self, nume, parola):
        self.nume = nume
        self.parola = parola
        self.sold = 0

    #functie folosita pentru autentificare
    def autentificare(self , nume , parola):
        #mai intai caut daca exista contul printre cele create anterior
        ok = 0
        #iterez prin cheile din dictionar
        for keys in conturi:
            '''
            daca una din ele se potriveste cu numele dat , atunci actualizez variabilele in care tin minte numele ,
            parola , si soldul asociat cheii respective
            '''
            if keys == nume:
                if conturi[nume][0] == parola:
                    self.nume = nume
                    self.parola = parola
                    self.sold = conturi[nume][1]
                    print("V-ati autentificat cu succes , bun venit " , nume , "\n")
                    print("Soldul din contul dvs. este de " , conturi[nume][1] , " lei\n")
                    ok = 1
        #in cazul in care niciun nume nu se potriveste cu una din chei atunci afisez un mesaj si atat
        if ok == 0:
            print("Datele introduse sunt gresite\n")

    #functie pentru crearea conturilor
    def creare(self, nume ,parola):
        #verific daca numele de utilizator dat a mai fost inregistrat inainte si afisez eroare in cazul in care exista
        ok = 1
        for keys in conturi:
            if keys == nume:
                ok = 0

        if ok == 1:
            #fiecare cheie are asociata o lista
            conturi.setdefault(nume, [])
            #adaug parola data pe pozitia 0 si sold initial 0 lei pe pozitia 1
            conturi[nume].append(parola)
            conturi[nume].append(0)
            print("Contul a fost creat cu succes\n")
        else:
            print("Contul exista deja\n")


    def inchiderecont(self, nume):
        '''
        folosesc variabila login pentru a verifica daca la un moment dat cel ce utilizeaza programul este logat pe un
        cont sau nu pentru a afisa un anumit tip de erori
        '''
        global login
        ok = 0
        for keys in conturi:
            if keys == nume:
                ok = 1

        if ok == 0:
            print("contul introdus nu exista\n")
        else:
            #parola este necesara pentru a sterge un cont
            parola = input("Pentru a sterge contul va rog introduceti parola : ")
            if conturi[nume][0] != parola:
                #daca parola introdusa este gresita apare o eroare specifica
                print("Parola introdusa este gresita\n")
            else:
                '''
                -acum tratez cazul in care utilizatorul doreste sa stearga contul pe care este logat curent , in acest
                caz variabila login trece pe 0 , adica inainte sa se stearga contul este delogat si trebuie sa se
                logheze din nou pentru a folosii optiunile din meniu altfel apar erori
                -cand sterg contul pur si simplu ii dau pop din dictionar
                '''
                if nume == self.nume:
                    login = 0
                    conturi.pop(nume, None)
                    print("contul a fost sters cu succes\n")
                else :
                    conturi.pop(nume, None)
                    print("contul a fost sters cu succes\n")

    #functie pentru depozitarea de bani in cont
    def depoziteaza(self, suma):
        #se adauga suma data la datele curente ale contului dar si la dictionar
        self.sold += suma
        conturi[self.nume][1] += suma
        print("Ati depozitat cu succes suma de " , suma , " de lei in contul " , self.nume , "\n")

    #functie pentru extragerea de bani din cont
    def extrage(self, suma):
        '''
        in cazul in care nu sunt destule fonduri in cont apare o eroare specifica altfel se actualizeaza datele curente
        si datele din dictionar
        '''
        if conturi[self.nume][1] - suma < 0:
            print("Suma ceruta nu poate fi extrasa : fonduri insuficiente\n")
        else:
            print("Ati extras cu succes suma de", suma, "de lei in contul ", self.nume , "\n")
            conturi[self.nume][1] -= suma
            self.sold -= suma

    #functie de transfer de bani , ea necesita sa fii logat pe un cont deja si sa introduci un utilizator si suma dorita
    def transfer(self,nume2,suma):
        ok = 0
        for keys in conturi:
            if keys == nume2:
                ok = 1
        #eroare in cazul in care nu sunt fonduri suficiente pe cont
        if conturi[self.nume][1] - suma < 0:
            print("Suma ceruta nu poate fi transferata , transfer anulat\n")
        else:
            if ok == 1:
                #scad din soldul contului curent suma data si o adaug in contul cerut
                conturi[self.nume][1] -= suma
                self.sold -= suma
                conturi[nume2][1] += suma
                print("Ati transferat cu succes suma de " , suma , " de lei din contul " , self.nume , " in contul " , nume2 ,"\n")
            else :
                #eroare in cazul in care nu exista al doilea cont
                print("Al doilea cont nu exista , transfer anulat\n")

    #functie ce afiseaza datele contului pe care utilizatorul este logat curent
    def date(self):
        # datele afisate sunt numele , parola si soldul
        print("Datele contului pe care sunteti logat curent sunt :")
        print("Nume : " , self.nume )
        print("Parola : " , self.parola )
        print("Sold : " , self.sold ,"\n" )

#variabila ce verifica daca utilizatorul este logat pe un cont este initializata cu 0
login = 0

def MENIU():
    global nume , parola , user , user2 , login
    print("Banca Lui Radu:")
    print("Optiunea 1 : Deschide cont nou.")
    print("Optiunea 2 : Autentifica-te")
    print("Optiunea 3 : Inchide cont ")
    print("Optiunea 4 : Adauga o suma de bani (lei) la cont ")
    print("Optiunea 5 : Extrage o suma de bani (lei) din cont ")
    print("Optiunea 6 : Transfera o suma de bani dintr-un cont in altul")
    print("Optiunea 7 : Afisaza raportul contului logat curent")
    print("Optiunea 8 : Iesire din program")
    tip = input("Alegeti optiunea : ")
    if tip == '1':
        print()
        '''
        la crearea unui cont se vor introduce un nume si o parola , acestea pot contine simboluri sau spatii deoarece
        sunt salvate ca stringuri iar cheile din dictionar permit acest lucru
        ex : nume : Popescu Ion
             parola : tastatura22
        '''
        nume = input("Introduceti numele countului . Numele poate sa contina spatii sau simboluri : ")
        parola = input("Introduceti parola . De poate trebuie sa contina spatii sau simboluri : ")
        print()
        '''
        aici folosesc user2 pentru functia de creare deoarece , in cazul in care sunt logat pe contul radu (sa zicem)
        si creez un nou cont andrei , cand voi afisa datele contului curent se vor afisa cele ale lui andrei (chiar daca
        sunt logat pe contul radu) , iar folosind un al doilea obiect user2 evit aceasta problema
        '''
        user2 = Banca(nume , parola)
        user2.creare(nume,parola)
        MENIU()
    elif tip == '2':
        print()
        #la momentul logarii pe un cont variabila login devine 1
        login = 1
        nume = input("Introduceti numele contului : ")
        parola = input("Introduceti parola contului : ")
        user = Banca(nume, parola)
        print()
        user.autentificare(nume,parola)
        MENIU()
    elif tip == '3':
        print()
        #pentru a sterge un cont este nevoie de nume , apoi functia din clasa cere si parola
        nume = input("Introduceti nuemele contului pe care doriti sa-l stergeti : ")
        parola = ' '
        user.inchiderecont(nume)
        MENIU()
    elif tip == '4':
        print()
        #in cazul in care utilizatorul nu s-a logat pe un cont apare o eroare specifica (valabila si la optiunile 5,6,7)
        if login == 0:
            print("Nu v-ati logat inca , selectati prima sau a doua optiune\n")
            MENIU()
        else:
            #suma se citeste de la tastatura si se adauga la contul curent
            suma = input("Selectati suma pe care doriti sa o depozitati : ")
            user.depoziteaza(int(suma))
            MENIU()
    elif tip == '5':
        print()
        if login == 0:
            print("Nu v-ati logat inca , selectati prima sau a doua optiune\n")
            MENIU()
        else:
            suma = input("Selectati suma pe care doriti sa o extrageti : ")
            user.extrage(int(suma))
            MENIU()
    elif tip == '6':
        print()
        if login == 0:
            print("Nu v-ati logat inca , selectati prima sau a doua optiune\n")
            MENIU()
        else:
            #pentru transfer este nevoie de numele celui de-al doilea cont si suma dorita
            nume2 = input("Selectati contul in care doriti sa transferati bani : ")
            suma = input("Selectati suma pe care doriti sa o transferati : ")
            user.transfer(nume2 , int(suma))
            MENIU()
    elif tip == '7':
        if login == 0:
            print("Nu v-ati logat inca , selectati prima sau a doua optiune\n")
            MENIU()
        else:
            print()
            user.date()
            MENIU()
    elif tip =='8':
        print()
        print("Programul se va inchide.")
    else:
        print("\nOptiunea aleasa este invalida , introduceti alta.\n")
        MENIU()


MENIU()
