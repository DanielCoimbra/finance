import json


def acoes_menu():
  sec_opt = input("\n\n1 -> Check all\n2 -> Add new entry\n")
  if sec_opt=='1':
    for key in acoes.keys():
      print("\n"+str(key) + "\n")
      papel_total = 0
      for x in acoes[key]: 
        print(str(x) + "\n")
        papel_total += x[1] * x[2]
      print(f"Total: {papel_total}\n")
  elif sec_opt=='2':
    cont =0
    for key in acoes.keys():
       print(str(cont) + "-> " + str(key))
       cont+=1
    print(str(cont) + "-> Add new stock")
    acao = input()
    if acao == cont:
      n_ = input("Sigla do papel: ")
      acoes[n_]=[]
    d_, p_, q_= input("Data: "), input("Preço: "), input("Quantidade: ")
    nova_acao=[d_, float(p_), int(q_)]
    if acao in data["Acoes"].keys():
      list(data['Acoes'].keys())[acao].append(nova_acao)
      with open("renda_variavel_2021.json", "w") as f:
        json.dump(data, f, indent=2)
 
 
def fiis_menu():
  sec_opt = input("\n\n1 -> Check all\n2 -> Add new entry\n")
  if sec_opt=='1':
    for key in fiis.keys():
      print("\n"+str(key) + "\n")
      papel_total = 0
      for x in fiis[key]: 
        print(str(x) + "\n")
        papel_total += x[1] * x[2]
      print(f"Total: {papel_total}\n")
 
  elif sec_opt=='2':
    cont =0
    for key in fiis.keys():
       print("\n"+str(cont) + "-> " + str(key))
       cont+=1
    print(str(cont) + "-> Add new fii")
    fii = input()
    if fii == cont:
      n_ = input("Sigla do papel: ")
      fiis[n_]=[]
    d_, p_, q_= input("Data: "), input("Preço: "), input("Quantidade: ")
    novo_fii=[d_, float(p_), int(q_)]
    if fii in fiis.keys():
  
      list(data['FIIs'].keys())[fii].append(novo_fii)
      with open("renda_variavel_2021.json", "w") as f:
        json.dump(data, f, indent=2)


def etfs_menu():
  sec_opt = input("\n\n1 -> Check all\n2 -> Add new entry\n")
  if sec_opt=='1':
    for key in etfs.keys():
      papel_total = 0
      print(str(key) + "\n")
      for x in etfs[key]:
        print(str(x) + "\n")
        papel_total += x[1] * x[2]
      print(f"Total: {papel_total}\n")
  elif sec_opt=='2':
    cont =0
    for key in etfs.keys():
       print(str(cont) + "-> " + str(key))
       cont+=1
    print(str(cont) + "-> Add new fii")
    etf = input()
    if etf == cont:
      n_ = input("Sigla do papel: ")
      etfs[n_]=[]
    d_, p_, q_= input("Data: "), input("Preço: "), input("Quantidade: ")
    novo_etf=[d_, float(p_), int(q_)]
    if etf in etfs.keys():
  
      list(data['ETFs'].keys())[etf].append(novo_etf)
      with open("renda_variavel_2021.json", "w") as f:
        json.dump(data, f, indent=2)


def total():
  t = 0
  acoes = 0
  fiis = 0
  etfs = 0
  for key in data:
    for key2 in data[key]:
      for x in range(len(data[key][key2])):
        if key == "Acoes": acoes += data[key][key2][x][1] * data[key][key2][x][2]
        if key == "ETFs": etfs += data[key][key2][x][1] * data[key][key2][x][2]
        if key == "FIIs": fiis += data[key][key2][x][1] * data[key][key2][x][2]
        t += data[key][key2][x][1] * data[key][key2][x][2]
  
  print(f"FIIs: {fiis:.2f}")
  print(f"Acoes: {acoes:.2f}")
  print(f"ETFs: {etfs:.2f}")
  print(f"Total: {t:.2f}")



def main_menu(menu_opt):	
  if menu_opt=='1':
    acoes_menu()

  elif menu_opt=='2':
    fiis_menu()

  elif menu_opt=='3':
    etfs_menu()

  elif menu_opt=='4':
    total()

  else: print('nothing happened\n')



while True:
  with open("renda_variavel_2021.json", "r") as read_file:
    data = json.load(read_file)

  acoes = data["Acoes"]

  fiis = data["FIIs"]

  etfs = data["ETFs"]
 
  #menu_opt menu
  menu_opt = input("Choose option\n\n1 -> Ações\n2 -> FIIs\n3 -> ETFs\n4 -> Total invested\n")
  # 0 ends the loop
  if menu_opt == '0': break
  main_menu(menu_opt)
  
print("end\n\n")
