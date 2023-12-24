from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()

nazev_procesu = input("Zadej jméno procesu, který chceš hacknout:\n")



def get_proces(nazev_procesu: str):
    proces = rwm.get_process_by_name(nazev_procesu)
    return proces

def get_probihajici_procesy():
    probihajici_procesy = rwm.enumerate_processes()
    return probihajici_procesy

def zapis_do_pameti_procesu(proces):
    proces.open()
    proces_pointer = proces.get_pointer(5304, offsets = [14])
    return proces_pointer


def main():
    print(zapis_do_pameti_procesu(proces=get_proces(nazev_procesu=nazev_procesu)))




if __name__ == "__main__":
    main()