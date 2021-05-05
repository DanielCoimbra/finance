import json


def acoes_menu():
  
  sec_opt = input("\n\n1 -> Check all\n2 -> Add new entry\n")
  if sec_opt=='1':
    for key in data['Acoes'].keys():
      counter=0
      print(f"\n{str(key)}\n")
      papel_total = 0
      for x in data['Acoes'][key]: 
        print(str(x) + "\n")
        papel_total += x[1] * x[2]
        counter+= x[2]
      print(f"Total: {papel_total}\n")
      print(f"Quantidade: {counter}\n")
      print(f"Preço médio: {papel_total / counter}\n")

  elif sec_opt=='2':
    cont =0
    for key in data['Acoes'].keys():
       print(f"{str(cont)} -> {str(key)}")
       cont+=1
    print(f"{str(cont)} -> Add new stock")
    acao = input()
    if acao == cont:
      n_ = input("Sigla do papel: ")
      data['Acoes'][n_]=[]
    d_, p_, q_= input("Data: "), input("Preço: "), input("Quantidade: ")
    nova_acao=[d_, float(p_), int(q_)]
    try:
      list(data['Acoes'].keys())[acao].append(nova_acao)
      with open("logs.json", "w") as f:
        json.dump(data, f, indent=2)
    except:
      print("\nerror\n")
 
def fiis_menu():
  sec_opt = input("\n\n1 -> Check all\n2 -> Add new entry\n")
  if sec_opt=='1':
    for key in data['FIIs'].keys():
      counter=0
      print("\n"+str(key) + "\n")
      papel_total = 0
      for x in data['FIIs'][key]:
        print(str(x) + "\n")
        papel_total += x[1] * x[2]
        counter+=x[2]
      print(f"Total: {papel_total}\n")
      print(f"Quantidade: {counter}\n")
      print(f"Preço médio: {papel_total / counter}\n")
 
  elif sec_opt=='2':
    cont =0
    for key in data['FIIs'].keys():
       print(f"\n {str(cont)} -> {str(key)}")
       cont+=1
    print(f"\n{str(cont)}-> Add new fii")
    fii = input()
    if fii == cont:
      n_ = input("Sigla do papel: ")
      data['FIIs'][n_]=[]
    d_, p_, q_= input("Data: "), input("Preço: "), input("Quantidade: ")
    novo_fii=[d_, float(p_), int(q_)]

    try:
      list(data['FIIs'].keys())[fii].append(novo_fii)
      with open("logs.json", "w") as f:
        json.dump(data, f, indent=2)
    except:
      print("error")
 
def etfs_menu():
  sec_opt = input("\n\n1 -> Check all\n2 -> Add new entry\n")
  if sec_opt=='1':
    for key in data['ETFs'].keys():
      
      counter = 0
      papel_total = 0
      print(f"\n{str(key)}\n")
      for x in data['ETFs'][key]:
        print(f"{str(x)}\n")
        papel_total += x[1] * x[2]
        counter += x[2]
      print(f"Total: {papel_total}\n")
      print(f"Quantidade: {counter}\n")
      print(f"Preço médio: {papel_total / counter}\n")
  elif sec_opt=='2':
    cont =0
    for key in data['ETFs'].keys():
       print(f"{str(cont)} -> {str(key)}")
       cont+=1
    print(f"{str(cont)} -> Add new etf")
    etf = input()
    if etf == cont:
      n_ = input("Sigla do papel: ")
      data['ETFs'][n_]=[]
    d_, p_, q_= input("Data: "), input("Preço: "), input("Quantidade: ")
    novo_etf=[d_, float(p_), int(q_)]
   
    try:  
      list(data['ETFs'].keys())[etf].append(novo_etf)
      with open("logs.json", "w") as f:
        json.dump(data, f, indent=2)
    except:
      print("error")

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
  
  print(f"\nFIIs: {fiis:.2f}")
  print(f"\nAcoes: {acoes:.2f}")
  print(f"\nETFs: {etfs:.2f}")
  print(f"\nTotal: {t:.2f}\n")

def crypto_menu():
  sec_opt = input("\n\n1 -> Check all\n2 -> Add new entry\n")
  if sec_opt == '1':
	for key in data['crypto']:
	  counter    =  0
	  papel_total = 0
	  print(f"\n{str[key]}\n")
      for x in data['Crypto'][key]:
        print(f"{str(x)}\n")
		papel_total+= x[1] * x{2}
		counter += x[2]
		print(f"Total: {papel_total}\n")
		print(f"Preço médio: {papel_total / counter}\n")
  elif sec_opt == '2':
    cont = 0
    for key in data['Crypto'].keys():
	  print(f"{str(cont)} -> {str(key)}")
      cont+=1
    print(f"{str(count)} -> Add new crypto")
	crypto = input()
    if crypto == cont:
      n_ = input("Sigla do ativo: ")
      data["Crypto"][n_]=[]
    d_,p_,q_ = input("Data: ", input("Preço: "), input("Quantidade: ")
    novo_crypto=[d_, float(p_), float(q_)]
    try:
      list(data["Crypto"].keys())[crypto].append(novo_crypto)
      with open("logs.json", "w") as f:
        json.dump(data, f , indent=2)
   except:
     print("error")




def main_menu(menu_opt):	
  if menu_opt=='0':
	crypto_menu()

  elif menu_opt=='1':
    acoes_menu()

  elif menu_opt=='2':
    fiis_menu()

  elif menu_opt=='3':
    etfs_menu()

  elif menu_opt=='4':
    total()

  elif menu_opt=='5':
    percentage()

  else: print('nothing happened\n')



while True:
  with open("logs.json", "r") as read_file: #logs.json
    data = json.load(read_file)

  
  #menu_opt menu
  menu_opt = input("Choose option\n\n1 -> Ações\n2 -> FIIs\n3 -> ETFs\n4 -> Total invested\n")
  # 0 ends the loop
  if menu_opt == '0': break
  main_menu(menu_opt)
  
print("end\n\n")


# falta fazer a passagem dos dados de volta ao json, crud de dados

# porcentagem de papeis desejada vs atual
