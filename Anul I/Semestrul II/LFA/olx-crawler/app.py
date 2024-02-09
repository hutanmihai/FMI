from flask import Flask, render_template
import flask.cli
import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures

app = Flask(__name__)


@app.route('/')
def index():
    f = open("anunturi_parser.txt", "w", encoding="utf-8", errors="ignore")
    maxnr = 20

    def func_link(anunt):
        curent = BeautifulSoup(requests.get(f"https://olx.ro{anunt}").content, "html.parser")
        titlu = str(curent.select(
            "html body div#root div.css-50cyfj div.css-1on7yx1 div.css-1d90tha div.css-dwud4b div.css-1wws9er div.css-sg1fy9 h1.css-r9zjja-Text"))[
                56:-6]
        descriere = str(curent.select(
            "html body div#root div.css-50cyfj div.css-1on7yx1 div.css-1d90tha div.css-dwud4b div.css-1wws9er div.css-1m8mzwg div.css-g5mtbi-Text")).replace(
            '<br>', '').replace('</br>', '').replace('<br/>', '')[30:-7]
        titlu = titlu.replace('\n', ' ')
        descriere = descriere.replace('\n', ' ')
        titlu = titlu.replace('\r', ' ')
        descriere = descriere.replace('\r', ' ')
        creat = "---" + titlu + " " + descriere + "\n"
        f.write(creat)

    for i in range(maxnr):
        soup = BeautifulSoup(requests.get(f"https://www.olx.ro/d/servicii-afaceri-colaborari/?page={i}").content,
                             "html.parser")
        anunturi = soup.find_all("a", class_="css-1bbgabe", href=True)
        for j in range(len(anunturi)):
            anunturi[j] = anunturi[j]["href"]
        concurrent.futures.ThreadPoolExecutor().map(func_link, anunturi)

    f.close()
    f = open("anunturi_parser.txt", 'r', encoding="utf-8", errors="ignore")

    lista = []

    dict_categorii = {"Transporturi: ": 0, "Tractari: ": 0, "Constructii: ": 0, "Reparatii: ": 0, "Evenimente: ": 0,
                      "Infrumusetare: ": 0, "Curatenie: ": 0}

    dict_evenimente = {"Nunta: ": 0, "Botez: ": 0, "Majorat: ": 0}

    dict_localitati = {"Ilfov: ": 0, "Bucuresti: ": 0, "Ploiesti: ": 0, "Sibiu: ": 0, "Caracal: ": 0,
                       "Focsani: ": 0, "Cluj: ": 0, "Iasi: ": 0, "Brasov: ": 0, "Pitesti: ": 0}

    dict_preturi = {"Mai putin de 100 de lei: ": 0, "Intre 100 si 250 lei: ": 0, "Intre 250 si 500 lei: ": 0,
                    "Intre 500 si 1000 lei: ": 0}

    dict_service = {"Service auto: ": 0, "Service telefoane: ": 0, "Service electrocasnice: ": 0}

    dict_materiale = {"Tigla: ": 0, "Ceramica: ": 0, "Faltz: ": 0, "Roca vulcanica: ": 0, "Tabla: ": 0, "Inox: ": 0}

    dict_limbaje = {"Python: ": 0, "Javascript: ": 0, "Java: ": 0, "Html: ": 0, "CSS: ": 0, "C/C++: ": 0}

    dict_culori = {"Albastru: ": 0, "Rosu: ": 0, "Verde: ": 0, "Roz: ": 0, "Galben: ": 0, "Maro: ": 0}

    dict_curatenie = {"Tapiterii: ": 0, ": ": 0, "Autoturisme: ": 0, "Case/apartamente: ": 0, "Covoare: ": 0}

    dict_diverse = {"DJ: ": 0, "Fotograf: ": 0, "Lumini: ": 0, "Band: ": 0, "Barman: ": 0}

    for line in f:

        # CATERGORII

        anunt = re.search("transport(am|uri|ăm|a|ă)?", line, re.I)
        if anunt:
            dict_categorii["Transporturi: "] += 1

        anunt = re.search("tract(am|ari|ăm|ări|ează|eaza)", line, re.I)
        if anunt:
            dict_categorii["Tractari: "] += 1

        anunt = re.search("constr(uim|uiesc|uc[tț]ie)", line, re.I)
        if anunt:
            dict_categorii["Constructii: "] += 1

        anunt = re.search("(repar([ăa]m|a[tț](i|ii))?|depan([aă]m|are|ez)|service)", line, re.I)
        if anunt:
            dict_categorii["Reparatii: "] += 1

        anunt = re.search("organiz((ez)|(am)|(ăm)|(are))?.*evenimente?", line, re.I)
        if anunt:
            dict_categorii["Evenimente: "] += 1

        anunt = re.search("(salo(n|ane))|(beauty)|([iî]nfrumuse[tț]are)|(machiaj(e)?)|(coafor|tuns(ur[aăi])|unghi[i])",
                          line, re.I)
        if anunt:
            dict_categorii["Infrumusetare: "] += 1

        anunt = re.search("(menajer([aă])?)|(cura[tț](enie)?)", line, re.I)
        if anunt:
            dict_categorii["Curatenie: "] += 1

        # LOCALITATE

        anunt = re.search(r"bucure[sș]ti", line, re.I)
        if anunt:
            dict_localitati["Bucuresti: "] += 1

        anunt = re.search(r"ilfov", line, re.I)
        if anunt:
            dict_localitati["Ilfov: "] += 1

        anunt = re.search(r"cluj", line, re.I)
        if anunt:
            dict_localitati["Cluj: "] += 1

        anunt = re.search(r"bra[sș]ov", line, re.I)
        if anunt:
            dict_localitati["Brasov: "] += 1

        anunt = re.search(r"caracal", line, re.I)
        if anunt:
            dict_localitati["Caracal: "] += 1

        anunt = re.search(r"foc[sș]ani", line, re.I)
        if anunt:
            dict_localitati["Focsani: "] += 1

        anunt = re.search(r"pite[sș]ti", line, re.I)
        if anunt:
            dict_localitati["Pitesti: "] += 1

        anunt = re.search(r"ploie[sș]ti", line, re.I)
        if anunt:
            dict_localitati["Ploiesti: "] += 1

        anunt = re.search(r"sibiu", line, re.I)
        if anunt:
            dict_localitati["Sibiu: "] += 1

        anunt = re.search(r"ia[sș]i", line, re.I)
        if anunt:
            dict_localitati["Iasi: "] += 1

        # EVENIMENTE

        anunt = re.search(r"organiz([(ez)|(am)|(ăm)|(are)])?.*nun[țt][iaă]", line, re.I)
        if anunt:
            dict_evenimente["Nunta: "] += 1
        anunt = re.search(r"organiz([(ez)|(am)|(ăm)|(are)])?.*botez[uri]?", line, re.I)
        if anunt:
            dict_evenimente["Botez: "] += 1
        anunt = re.search(r"organiz([(ez)|(am)|(ăm)|(are)])?.*majorat([e])?", line, re.I)
        if anunt:
            dict_evenimente["Majorat: "] += 1

        # PRET
        anunt = re.search(r"(\d{1,4}).\D*?(?<=(?:\blei\b|\bron\b))", line, re.I)
        if anunt:
            pret = int(anunt.groups()[0])
            if pret <= 100:
                dict_preturi["Mai putin de 100 de lei: "] += 1
            elif 100 < pret <= 250:
                dict_preturi["Intre 100 si 250 lei: "] += 1
            elif 250 < pret <= 500:
                dict_preturi["Intre 250 si 500 lei: "] += 1
            elif 500 < pret <= 1000:
                dict_preturi["Intre 500 si 1000 lei: "] += 1

        # TIPURI SERVICE

        anunt = re.search(
            r"(repar([ăa]m|a[tț](i|ii))?|depan([aă]m|are|ez)|(service)).*(auto(vehicul|turism)?|ma[șs]in[ăa]|cami(on|oane))",
            line, re.I)
        if anunt:
            dict_service["Service auto: "] += 1

        anunt = re.search(
            r"(repar([ăa]m|a[tț](i|ii))?|depan([aă]m|are|ez)|(service)).*(telefo(n|ane)|iphone(-uri)?|samsung|huawei|xiaomi)",
            line, re.I)
        if anunt:
            dict_service["Service telefoane: "] += 1

        anunt = re.search(
            r"(repar([ăa]m|a[tț](i|ii))?|depan([aă]m|are|ez)|(service)).*(electrocasnice|ma[sș]in[ăa] de (sp[aă]lat (vase)?)|microunde)",
            line, re.I)
        if anunt:
            dict_service["Service electrocasnice: "] += 1

        #  MATERIALE:
        anunt = re.search("[tț][îi]gl[aă]", line, re.I)
        if anunt:
            dict_materiale["Tigla: "] += 1

        anunt = re.search("ceramic[aă]", line, re.I)
        if anunt:
            dict_materiale["Ceramica: "] += 1

        anunt = re.search("fal[tț]?(tz)?", line, re.I)
        if anunt:
            dict_materiale["Faltz: "] += 1

        anunt = re.search("roc[aă].*vulcanic[aă]", line, re.I)
        if anunt:
            dict_materiale["Roca vulcanica: "] += 1

        anunt = re.search("tabl[aă]", line, re.I)
        if anunt:
            dict_materiale["Tabla: "] += 1

        anunt = re.search("ino[x|(cs)]", line, re.I)
        if anunt:
            dict_materiale["Inox: "] += 1

        #     LIMBAJE DE PROGRAMARE

        anunt = re.search("python", line, re.I)
        if anunt:
            dict_limbaje["Python: "] += 1
        anunt = re.search("java\s?script", line, re.I)
        if anunt:
            dict_limbaje["Javascript: "] += 1
        anunt = re.search("\bjava\b", line, re.I)
        if anunt:
            dict_limbaje["Java: "] += 1
        anunt = re.search("html", line, re.I)
        if anunt:
            dict_limbaje["Html: "] += 1
        anunt = re.search("css", line, re.I)
        if anunt:
            dict_limbaje["CSS: "] += 1
        anunt = re.search("(\bc\b)|((cpp)|(c\+\+))", line, re.I)
        if anunt:
            dict_limbaje["C/C++: "] += 1

        # CULORI

        anunt = re.search("alb[aă]str[ui]|alba[sș]trii", line, re.I)
        if anunt:
            dict_culori["Albastru: "] += 1
        anunt = re.search("(ro[șs](u|ii)?|ro[sș]iatici?)", line, re.I)
        if anunt:
            dict_culori["Rosu: "] += 1
        anunt = re.search("roz|rozali[ui]", line, re.I)
        if anunt:
            dict_culori["Roz: "] += 1
        anunt = re.search("g[aă]lb(in|ene?|ui)", line, re.I)
        if anunt:
            dict_culori["Galben: "] += 1
        anunt = re.search("ver(de|zui|zi)", line, re.I)
        if anunt:
            dict_culori["Verde: "] += 1
        anunt = re.search("maro(ni[ui])?", line, re.I)
        if anunt:
            dict_culori["Maro: "] += 1

        #     SERVICII DE CURATENIE

        anunt = re.search("cur[ăa][tț](?:[aă]m|a[tț]i|eni[ei]|are).*tapi[tț]er[ie]", line, re.I)
        if anunt:
            dict_curatenie["Tapiterii: "] += 1
        anunt = re.search("cur[ăa][tț](?:[aă]m|a[tț]i|eni[ei]|are).*(?:cas[ăae]|apartamente?|domicili[iu])", line, re.I)
        if anunt:
            dict_curatenie["Case/apartamente: "] += 1
        anunt = re.search("cur[ăa][tț](?:[aă]m|a[tț]i|eni[ei]|are).*(auto(vehicul|turism)?|ma[șs]in[ăa]|cami(on|oane))",
                          line, re.I)
        if anunt:
            dict_curatenie["Autoturisme: "] += 1
        anunt = re.search("cur[ăa][tț](?:[aă]m|a[tț]i|eni[ei]|are).*covo(?:r|are)", line, re.I)
        if anunt:
            dict_curatenie["Covoare: "] += 1

        #         DIVERSE

        anunt = re.search("\bdj\b", line, re.I)
        if anunt:
            dict_diverse["DJ: "] += 1

        anunt = re.search("fotograf(i?e?)?", line, re.I)
        if anunt:
            dict_diverse["Fotograf: "] += 1
        anunt = re.search("\bband(uri)?\b|\bforma[țt]i[ie]?\b", line, re.I)
        if anunt:
            dict_diverse["Band: "] += 1
        anunt = re.search("[îi]nchirier[ei].*(lumin[aăi])", line, re.I)
        if anunt:
            dict_diverse["Lumini: "] += 1
        anunt = re.search("barman(i([tț][aă])?)", line, re.I)
        if anunt:
            dict_diverse["Barman: "] += 1

    lista.append(["Categorii", dict_categorii])
    lista.append(["Localitati", dict_localitati])
    lista.append(["Evenimente", dict_evenimente])
    lista.append(["Preturi", dict_preturi])
    lista.append(["Service", dict_service])
    lista.append(["Materiale", dict_materiale])
    lista.append(["Limbaje de programare", dict_limbaje])
    lista.append(["Culori", dict_culori])
    lista.append(["Servicii de curatenie", dict_curatenie])
    lista.append(["Personal evenimente", dict_diverse])

    final_list = []

    for categorie in lista:
        temp_dict = {}
        backup_dict = {}
        altele = 0
        for key in categorie[1]:
            if categorie[1][key] <= 2:
                altele += categorie[1][key]
            else:
                temp_dict[key] = categorie[1][key]
            backup_dict[key] = categorie[1][key]
        if altele != 0:
            temp_dict["Altele: "] = altele
        if len(temp_dict) == 0:
            final_list.append([categorie[0], {"Nu au fost gasite rezultate pe acest filtru ": "!"}])
        elif len(temp_dict) == 1 and "Altele: " in temp_dict:
            temp_dict.clear()
            for key in backup_dict:
                if backup_dict[key] != 0:
                    temp_dict[key] = backup_dict[key]
            temp_dict["Celelalte filtre nu au fost gasite "] = '!'
            final_list.append([categorie[0], temp_dict])
        elif len(temp_dict) == 1:
            temp_dict["Celelalte filtre nu au fost gasite "] = "!"
            final_list.append([categorie[0], temp_dict])
        else:
            final_list.append([categorie[0], temp_dict])

    return render_template("index.html", lista=final_list)


if __name__ == '__main__':
    app.run()
