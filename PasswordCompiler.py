version = "3.5.1"
scriptURL = "https://raw.githubusercontent.com/alfanoandrea/password-compiler/main/PasswordCompiler.py"
debug = False


class Color:
    violet = "\033[35;1m"
    red = "\u001b[31;1m"
    cyan = "\u001b[36;1m"
    green = "\u001b[32;1m"
    yellow = "\u001b[33;1m"
    fucsia = "\u001b[35;1m"
    gray = "\033[90;1m"
    italic = "\033[3;1m"
    reset = "\u001b[0m"


try:
    from tqdm import tqdm
    import requests
    import os
    import time
    import itertools
    import re
except ImportError:
    print(f"{Color.red} Missing modules! Run 'pip install -r requirements.txt'{Color.reset}")
    exit(1)


def internet():
    try:
        requests.head('https://www.google.com', timeout=5) 
        return True
    except requests.exceptions.RequestException:
        return False


class graphics:
    def clear():
            os.system("cls") if os.name == 'nt' else os.system("clear")

    def intro(dynamic):
        graphics.clear()
        logo = [
            Color.green,
            "    _____                             _ \n",
            "   |  _  |___ ___ ___ _ _ _ ___ ___ _| |\n",
            "   |   __| .'|_ -|_ -| | | | . |  _| . |\n",
            "   |__|  |__,|___|___|_____|___|_| |___|\n",
            "      _____               _ _         \n",
            "     |     |___ _____ ___|_| |___ ___ \n",
            "     |   --| . |     | . | | | -_|  _|\n",
            "     |_____|___|_|_|_|  _|_|_|___|_|  \n",
            "                     |_|            \n",
            Color.violet, Color.italic,
            f"       by alfanowski     {Color.reset}version: {version}\n"
        ]
        for i in logo:
            for j in i:
                print(j, end='', flush=True)
                time.sleep(0.01) if dynamic else None
        time.sleep(0.7) if dynamic else None
        print(f"{Color.red} ------------------------------------------\n{Color.reset}")

    def selezione():
        while True:
            graphics.intro(dynamic = False)
            print(f"  {Color.gray}({Color.green}1{Color.gray}){Color.cyan} Generate{Color.reset}")
            print(f"  {Color.gray}({Color.green}2{Color.gray}){Color.cyan} Update{Color.reset}")
            print(f"  {Color.gray}({Color.green}X{Color.gray}){Color.red} Exit{Color.reset}")
            sel = input(f"\n{Color.violet}   >> {Color.reset}").lower()
            if sel in ['1', '2', 'x']:
                return sel


def dictionary():
    def getName():
        if debug:
            return "babbo"
        while True:
            graphics.intro(dynamic = False)
            print(f"{Color.gray} ({Color.green}B{Color.gray}){Color.yellow} Back{Color.reset}\n")
            nome = input(f"{Color.cyan} Write the name\n{Color.violet}   >> {Color.reset}")
            if all(char.isalpha() for char in nome) and len(nome) > 1 or nome.lower() == 'b':
                return nome

    def getSurname():
        if debug:
            return "natale"
        while True:
            graphics.intro(dynamic = False)
            print(f"{Color.gray} ({Color.green}B{Color.gray}){Color.yellow} Back{Color.reset}\n")            
            cognome = input(f"{Color.cyan} Write the surname\n{Color.violet}   >> {Color.reset}")
            if all(char.isalpha() for char in cognome) and len(cognome) > 1 or cognome.lower() == 'b':
                return cognome

    def getNascita():
        if debug:
            return "25122000"
        while True:
            graphics.intro(dynamic = False)
            print(f"{Color.gray} ({Color.green}B{Color.gray}){Color.yellow} Back{Color.reset}\n")
            nascita = input(f"{Color.cyan} Write the birth year {Color.gray}(DDMMYYYY)\n{Color.violet}   >> {Color.reset}")
            if len(nascita) == 8 and nascita.isdigit() or nascita.lower() == 'b':
                return nascita

    def current(nome, cognome, giorno, mese, anno):
        if debug:
            return True
        while True:
            graphics.intro(dynamic = False)
            print(f"{Color.cyan}          NAME {Color.yellow}>> {Color.reset}{nome.capitalize()}")
            print(f"{Color.cyan}       SURNAME {Color.yellow}>> {Color.reset}{cognome.capitalize()}")            
            print(f"{Color.cyan}    BIRTH DATE {Color.yellow}>> {Color.reset}{giorno}/{mese}/{anno}\n")    
            selezione = input(f"{Color.yellow} Are you sure? {Color.gray}(Y or N)\n{Color.violet}  >> {Color.reset}").lower()
            if selezione == 'y':
                return True
            elif selezione == 'n':
                return False
        
    def nomeFile():
        def chiediNomeFile():
            graphics.intro(dynamic=False)
            print(f"{Color.gray} ({Color.green}B{Color.gray}){Color.yellow} Back{Color.reset}\n")
            file = input(f"{Color.cyan} Give a name to the file to generate {Color.gray}(without .txt)\n{Color.red}  >>  {Color.reset}")
            if file.lower() == 'b':
                return 'b'
            if not len(file) > 0:
                return chiediNomeFile()
            return file
        
        def confermaNomeFile(file):
            graphics.intro(dynamic = False)
            print(f"   {Color.cyan}FILE {Color.yellow}>> {Color.reset}{file}{Color.gray}.txt{Color.reset}\n")
            selezione = input(f"{Color.yellow} Are you sure? {Color.gray}(Y or N)\n{Color.violet}   >> {Color.reset}").lower()
            if selezione not in ('y', 'n'):
                return confermaNomeFile(file)
            return selezione
        
        if debug:
            return "debug.txt"
        file = chiediNomeFile()
        if file.lower() == 'b':
                return file
        selezione = confermaNomeFile(file)
        if selezione == 'y':
            return file + ".txt"
        else:
            return nomeFile()

    def precisione():
        while True:
            graphics.intro(dynamic = False)
            print(f"{Color.cyan} Enter the file size:")
            print(f"{Color.gray}  ({Color.yellow}1{Color.gray}){Color.green} Small {Color.gray}{Color.italic} more than 15 thousand passwords{Color.reset}")
            print(f"{Color.gray}  ({Color.yellow}2{Color.gray}){Color.fucsia} Big {Color.gray}{Color.italic} more than 500 thousand passwords{Color.reset}")
            print(f"{Color.gray}  ({Color.yellow}3{Color.gray}){Color.red} Huge {Color.gray}{Color.italic} more than 19 million passwords\n{Color.reset}")
            sel = input(f"{Color.violet}   >> {Color.reset}")
            if sel.isnumeric() and 1 <= int(sel) <= 3: 
                return int(sel) + 3

    def generazione(file, combinazioni, dimensione):
        graphics.intro(dynamic=False)
        print(f"{Color.gray} Data calculation... {Color.reset}")
        totale = 0
        for length in range(2, dimensione):
            totale += len(list(itertools.permutations(combinazioni, length)))
        graphics.intro(dynamic=False)
        cont = 0
        print(Color.green, end='')
        with tqdm(total=totale, desc='', unit='B', leave=False, bar_format='  {percentage:3.0f}% |{bar}|  ', ncols=35) as pbar:
            with open(file, 'w') as f:
                for length in range(1, dimensione):
                    for combo in itertools.permutations(combinazioni, length):
                        password = ''.join(combo)
                        if len(password) >= 6 and any(name in password.lower() for name in combinazioni[:6]):
                            f.write(password + "\n")
                            cont += 1
                            pbar.update(1)
        print(Color.reset, end='')
        return cont
    
    def fine(file, paroleGenerate):
        graphics.intro(dynamic = False)
        print(f" The file {Color.green}{file}{Color.reset} has been created!\n")
        input(f" Lines: {Color.cyan}{paroleGenerate}{Color.reset}\n\n")
        graphics.clear()

    def folder():
        if not os.path.exists("dictionaries"):
            os.makedirs("dictionaries")

    while True:
        nome = getName().lower()
        if nome == 'b':
            return
        cognome = getSurname().lower()
        if cognome == 'b':
            return
        nascita = getNascita()
        if nascita == 'b':
            return
        giorno = str(nascita[:2])
        mese = str(nascita[2:4])
        anno = str(nascita[4:])
        if current(nome, cognome, giorno, mese, anno):
            break
    file = nomeFile()
    if file == 'b':
        return
    file = "dictionaries/" + file  
    combinazioni = [
        nome, cognome, 
        nome.capitalize(), cognome.capitalize(),
        nome.upper(), nome.upper(), 
        giorno, mese, anno, anno[-2:], 
        '.', ',', '?', '@', '#', '_', '-', '!', '$', '%', '[', ']', '(', ')'
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ]
    folder()
    paroleGenerate = str(generazione(file, combinazioni, precisione()))
    fine(file, paroleGenerate)


def update():
    graphics.intro(dynamic = False)
    try:
        response_check = requests.get(scriptURL, headers={'Range': 'bytes=0-200'}, timeout=5)
        response_check.raise_for_status()
        first_lines = response_check.text
        match = re.search(r'version\s*=\s*["\'](\d+\.\d+)["\']', first_lines)    
        if not match:
            return
        latestVersion = match.group(1)    
    except requests.exceptions.RequestException:
        return
    if version != latestVersion:
        print(f"{Color.yellow}  New version {Color.green}({latestVersion}){Color.yellow} avaible. Updating...{Color.reset}\n")
        try:
            response_script = requests.get(scriptURL, timeout=10)
            response_script.raise_for_status()
            script_filename = os.path.basename(__file__)
            with open(script_filename, 'w') as f:
                f.write(response_script.text)
            print(f"{Color.green}  Update completed, you can restart the script.\n{Color.reset}")
            exit(0)
        except requests.exceptions.RequestException:
            print(f"{Color.red}  [!] Error downloading script. Check {scriptURL}{Color.reset}")
        except IOError:
             print(f"{Color.red}  [!] Writing error! Check directory permissions.{Color.reset}")
    else:
        pass


#   M - A - I - N 
if __name__ == "__main__":
    if not debug:
        graphics.intro(dynamic = True)
    while True:
        opt = graphics.selezione()
        if opt == '1':
            dictionary()
        elif opt == '2':
            update()
        elif opt == 'x':
            graphics.clear()
            break

