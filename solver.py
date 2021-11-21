import os
dizionario_path="./weakpass.txt"
lettere="qwertyuiopasdfghjklzxcvbnm"
lettere={i for i in lettere}
inizio=0

#funzione per caricare tutte le words del dizionario
def load_dizionario(path):
    d=[]
    with open(path,"r")as f:
        for i in f:
            d.append(i.strip())
    print(d)
    return d[inizio:]
#funzione per decriptare il ciphertext con la password pw
def attaccoAlDizionario(pw,u):
    #chiamo la funzione di openssl per decriptare con la password pw
    #il cifrario des in cbc, la key derivation function e butto gli output su out.txt
    #e gli errori in err.txt
    os.system('cmd /c openssl enc -aes-256-cbc -d -pass pass:'+pw+'  -in outfile.txt.enc > o.txt 2>e.txt')
    try:
        #apro il file con la frase decifrata come file binario
        with open("o.txt","rb") as f:
            s=""
            #leggo nella stringa s il file binario convertendolo in utf8
            byte=f.read(1)
            while(byte):
                s+=byte.decode("utf-8",errors="ignore")
                byte=f.read(1)
            #calcolo la percentuale di lettere presenti nella frase decifrata
            percentualelettere=0
            for i in s:
                if i.lower() in lettere:
                    percentualelettere+=1
            percentualelettere/=len(s)
            print(u,pw)
            #se la percentuale di lettere presenti è maggiore del 70%
            #allora considero la frase come decifrata
            if percentualelettere>0.7:
                print(pw+"trovato")
                print(s)
                return (True,pw,s)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")   
    return (False,0,0)
    
if __name__ == '__main__':
    #carico il dizionario
    d=load_dizionario(dizionario_path)
    u=inizio
    #per tutte le parole nel dizionario provo a decriptaree se trovo un match stoppo
    for i in d:
        u+=1
        a=attaccoAlDizionario(i,u)
        if(a[0]==True):
            print(a[1],a[2])
            break
    #se trovo un match verra scritto nel file out insieme alla key
    #ed anche nella stream di output
    print("finished")