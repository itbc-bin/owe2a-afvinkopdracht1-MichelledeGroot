def main():
    bestand = "alpaca.fna" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
    headers, seqs = lees_inhoud(bestand) 
        
    zoekwoord = input("Geef een zoekwoord op: ")
    is_dna(seqs, zoekwoord, headers)
    knipt(seqs, headers, zoekwoord)
    
    
def lees_inhoud(bestands_naam):

    try:
        bestand = open(bestands_naam)
    except FileNotFoundError:
        print("File not found")
        return [], []
    
    headers = []
    seqs = []
    lines = ""

    
    for line in bestand:
        lines += line
    sequences = lines.split(">")
    sequences.pop(0)

    for i in range(len(sequences)):        
        
        header, seq = sequences[i].split("\n",1)
        seq = seq.replace("\n","")
        headers.append(header)
        seqs.append(seq)
    
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
     
    return headers, seqs

    
def is_dna(seq, zoek, header):
    
    if zoek in header:
        s = set(seq)
        if s.issubset({"A","C","T","G"}):
            return "is DNA of mRNA. "
        else:
            return "is geen DNA of mRNA. "

    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    

def knipt(seqs, headers, zoek):

    enzym = []
    try:
        with open("enzyme.txt") as openfile:
            enzym = list(openfile)

    
        for x in range(len(seqs)):
            if zoek in headers[x]:
                print(headers[x])
                print(is_dna(seqs[x], zoek, headers[x]))        

                for i in enzym:
                    enzymnaam, seq = i.split()
                    seq = seq.replace("^", "")
                    if seq in seqs[x]:

                        print(enzymnaam, "knipt op plaats", seqs[x].index(seq), "in sequentie",x+1)
                print("-"*40)
            
    except Exception as err:
        print("Error: ", str(err))
    

                    
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
       
    
main()
