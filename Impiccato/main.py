import random, os

welcome ='''--------------------------------------------------------
ATTENZIONE IN QUESTA VERSIONE SARANNO PRESENTI PAROLACCE
________________________________________________________
           Benvenuto al gioco del impiccato'''

mostra_difficolta = {1:'facile', 2:'medio', 3:'difficile'}
difficolta = f'''
___________________________________
      Seleziona la difficoltà
___________________________________   
        _________________
        |  {mostra_difficolta[1]}   | 1 |
        |   {mostra_difficolta[2]}   | 2 |
        | {mostra_difficolta[3]} | 3 |
        #################
    
inserisci la difficoltà: '''

yes = ['y','yeah','s','si','s','yea','yep']
no = ['n','no','nop','nope']

def onlytxt(fdir = 'paroleitaliane'):
    path = os.getcwd()
    file_path = path+'\\'+fdir
    content = os.listdir(file_path)
    content = [content[c] for c in range(len(content)) if '.txt' in content[c]]
    return content

def seleziona_parola(arg):
    files = onlytxt()
    if arg == 3:
        lenght = 9
        
    elif arg == 2:
        lenght = 6
        for c in range(3):
            if len(files) > 1:
                files.remove(files[random.randint(0, len(files) - 1)])
    else:
        lenght = 2
        for c in range(6):
            if len(files) > 1:
                files.remove(files[random.randint(0, len(files) - 1)])

        
    rand_files = files[random.randint(0, len(files)-1)]

    with open(f'.\\paroleitaliane\\{rand_files}','r', encoding='utf8') as file:
        content = file.readlines()
        len_content = len(content)

        rand = random.randint(0, len_content)
        parola = content[rand]
        while len(parola)<=lenght: # seleziona parole più lunghe di 2 caratteri
            rand = random.randint(0, len_content)
            parola = content[rand]
        return parola[:-1].lower()# esclude \n dalla parola



def nascondi_parola(parola):
    lung = len(parola)
    wordlist = (parola[0]+' '+'_ '*(len(parola)-2)+parola[-1]).split(' ')
    
    for i in range(len(parola)): # serve per svelare tutte le lettere uguali alla fine e al inizio
        if parola[i] == parola[0]:
            wordlist[i] = parola[0]
        elif parola[i] == parola[-1]:
            wordlist[i] = parola[-1]            
    return wordlist



def spacetext(arg):
    text = ''

    if type(arg) is int or type(arg) is float or type(arg) is complex:
        arg = str(arg)
        for c in range(len(arg)):
            if c != len(arg):
                text += arg[c] + ' '
            else:
                text += arg[c]
        return text

    elif type(arg) is list:
        for c in range(len(arg)):
            if c != len(arg):
                text += arg[c] + ' '
            else:
                text += arg[c]
        return text

    elif type(arg) is str:
        for c in range(len(arg)):
            if c != len(arg):
                text += arg[c] + ' '
            else:
                text += arg[c]
        return text

    else:
        print('type variabile non supportata')



def clear(arg = 50):
    for c in range(arg):
        print('\n')



def replay(arg):
    request = input(arg+ '\n[y\\n]:').lower()
    if request in yes:
        return True
    elif request in no:
        return False
    else:
        print('risposta non valita\n\nsi procederà con le impostazioni di sistema')
        return False



diff = 0
vite = 10
repeat = True

print(welcome)
# scelta difficoltà
def scelta_diff(reset_vite = True, reset_diff = True):
    global repeat
    global diff
    global vite
    repeat = True
    while repeat:
        if reset_diff:
            diff = input('\n'+difficolta)
            while not diff.isnumeric():
                print('li valore inserito non è corretto')
                clear()
                diff = input('\n'+difficolta)
            diff = int(diff)

        if 1 <= diff <= 3:
            if reset_vite:
                if diff == 1:
                    vite = 15
                elif diff == 3:
                    vite = 5
            repeat = False
        else:
            print('il valore inserito non è accettato')
            repeat = replay('\n\nvuoi continuare con le impostazioni di sistema o vuoi cambiare il valore inserito?')



wait = input('\n\n\npremi invio per iniziare: ')
clear()
scelta_diff()
clear()

#liste
lettere_usate = []
parole_usate = []
ruota_parole = []

#boolean
vittoria = False
repeat = False

# Gioco vero e proprio
while True:
    if repeat:
        print('si ripete')
        vittoria = False
        if len(ruota_parole) >= 10:
            routa_parole = []
        lettere_usate = []
        parole_usate = []

        while parola in ruota_parole:
            parola = seleziona_parola(diff)
        parola_nascosta = nascondi_parola(parola)
        ruota_parole.append(parola)
    else:
        parola = seleziona_parola(diff)
        parola_nascosta = nascondi_parola(parola)

    while not vittoria:
        clear()
        tentativo = input(f'difficoltà selezionata: {mostra_difficolta[diff]}\n\n{spacetext(parola_nascosta)}   vite: {vite}\n\nlettere usate: {spacetext(lettere_usate)}\n\n parole usate: {spacetext(parole_usate)}\n\ninserisci lettera\\parola: ')

        if not vittoria:
            if len(tentativo) > 1 and not(tentativo in parole_usate):
                if tentativo == parola:
                    vittoria = True
                elif tentativo == '!diff!':
                    scelta_diff(reset_vite=False)
                    parola = seleziona_parola(diff)
                elif tentativo == '!show!':
                    wait = input(f'{parola}\n\nclicca invio per continuare:')
                else:
                    if not(tentativo in parole_usate):
                        parole_usate.append(tentativo)
                        vite -= 1
            elif tentativo in parola and not(tentativo in lettere_usate):
                lettere_usate.append(tentativo)
                vite += 1
                for char in range(len(parola)):
                    if tentativo == parola[char]:
                        parola_nascosta[char] = tentativo
                vittoria = ''.join(parola_nascosta) == parola
            else:
                if not(tentativo in lettere_usate):
                    lettere_usate.append(tentativo)
                    vite -= 1

    if vittoria:
        clear()
        scelta_diff(reset_diff=False)
        repeat = True
        ruota_parole.append(parola)
        wait = input('bravo hai indovinato la parola\n\n\npremi invio per continuare: ')




























