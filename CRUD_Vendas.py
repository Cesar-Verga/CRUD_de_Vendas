import os
import sys
import shutil
from prettytable import from_csv
from prettytable import PrettyTable
import csv
from csv import DictReader, DictWriter
x = PrettyTable()

# Chamar arquivo csv
arquivo_CSV = 'table_crud_vendas.csv'



# clearscreen para limpar a tela com a tecla cls = clearscreen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Menu com prettytable
def show_menu():
    clear_screen()
    x = PrettyTable()
    x.add_column("MENU",[""," [1] Adicionar itens   "," [2] Editar item       "," [3] Apagar item       ","[4] Encontrar item   "," [5] Ver Lista de Itens"," [0] Sair              ",""]) 
    x.align = "c"
    print(x)

    selected_menu = input("Escolha uma opção> ")
    
    # Ramificação para determinar opções de menu
    if(selected_menu == "1"):
        add_Table()
    elif(selected_menu == "2"):
        edit_Table()
    elif(selected_menu == "3"):
        delete_Table()
    elif(selected_menu == "4"):
        search_Table()
    elif(selected_menu == "5"):
        show_Table()
    elif(selected_menu == "0"):
        sys.exit("Sistema encerrado com êxito!")
    else:
        print("\nOpção invalida, tente novamente: ")
        
    back_to_menu()
        

# a função retorna ao seu conteúdo menu chama a função show menu
def back_to_menu():
    print("\n")
    input("Pressione [Enter] para retornar...")
    show_menu()


# função exibe a tabela (5)
def show_Table():
    clear_screen()
    # abra o arquivo CSV com o prettytable
    with open(arquivo_CSV, encoding="ISO-8859-1") as f:
        tabela = from_csv(f)
        tabela.align = "c"
        print(tabela)
         
    back_to_menu()

    
# função adicionar item (1) 
def add_Table():
    clear_screen()
    Table = []
    with open(arquivo_CSV, mode="r",newline='', encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Table.append(row)
            
    #Prettytable
    with open(arquivo_CSV, encoding="ISO-8859-1") as f:
        tabela = from_csv(f)
        tabela.align = "c"
        print(tabela)

    NF = input("NF: ")
    existe = 0
    indeks = 0
    
    # verificando se NF é um campo vazio
    if (NF == ""):
        print("O campo nota fiscal deve ser preenchido, tente novamente")
        back_to_menu()
        
    # verificando se NF já existe
    for data in Table:
        if (data['NF'] == NF):
            existe = existe + 1
            
    # Abrir .CSV para escrever uma nova linha
    if (existe == 0):
        with open(arquivo_CSV, mode='a',newline='', encoding="ISO-8859-1") as csv_file:
            fieldnames = ['NF', 'NOME', 'FORNECEDOR','QT','CUSTO DE PRODUÇÂO','VALOR DE VENDA']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            NOME = input("NOME: ")
            # verificando se NOME é um campo vazio
            if (NOME == ""):
                print("O campo nome deve ser preenchido, tente novamente")
                back_to_menu()
                
            FORNECEDOR = input("FORNECEDOR: ")
            # verificando se FORNECEDOR é um campo vazio
            if (FORNECEDOR == ""):
                print("O campo fornecedor deve ser preenchido, tente novamente")
                back_to_menu()
                
            QT = input("QT: ")
            # verificando se QT é um campo vazio
            if (QT == ""):
                print("O campo quantidade deve ser preenchido, tente novamente")
                back_to_menu()
            
            CUSTO_DE_PRODUCAO = input("CUSTO DE PRODUÇÂO: ")
            # verificando se CUSTO_DE_PRODUCAO é um campo vazio
            if (CUSTO_DE_PRODUCAO == ""):
                print("O campo Custo de Produção deve ser preenchido, tente novamente")
                back_to_menu()
             
            VALOR_DE_VENDA = input("VALOR DE VENDA: ")
            # verificando se VALOR_DE_VENDA é um campo vazio
            if (VALOR_DE_VENDA == ""):
                print("O campo Valor de Venda deve ser preenchido, tente novamente")
                back_to_menu()
                
            #Utiliza os inputs para escrever no .CSV
            writer.writerow({'NOME': NOME, 'NF': NF, 'FORNECEDOR': FORNECEDOR, 'FORNECEDOR': FORNECEDOR, 'QT': QT, 'CUSTO DE PRODUÇÂO': CUSTO_DE_PRODUCAO, 'VALOR DE VENDA': VALOR_DE_VENDA})    
    else:
        print("NF já cadastrado, tente novamente")
        
    back_to_menu()

# função editar item (2)    
def edit_Table():
    clear_screen()
    Table = []
    
    with open(arquivo_CSV, mode="r",newline='', encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Table.append(row)

   # abra o arquivo CSV com o prettytable
    with open(arquivo_CSV, encoding="ISO-8859-1") as f:
        tabela = from_csv(f)
        tabela.align = "c"
        print(tabela)

            
    NF = input("Selecione a NF do produto : ")
    existe = 0
    indeks = 0
    # procurando se a NF é exista no .CSV
    for data in Table:
        if (data['NF'] == NF):
            existe = existe + 1

    if (existe > 0):
        
        NOME = input("novo nome: ")
        # verificando se NOME é um campo vazio
        if (NOME == ""):
            print("O campo nome deve ser preenchido, tente novamente")
            back_to_menu()
        
        FORNECEDOR = input("novo FORNECEDOR: ")
        # verificando se FORNECEDOR é um campo vazio
        if (FORNECEDOR == ""):
            print("O campo Fornecedor deve ser preenchido, tente novamente")
            back_to_menu()
            
        QT = input("novo quantidade: ")
        # verificando se QT é um campo vazio
        if (QT == ""):
            print("O campo quantidade deve ser preenchido, tente novamente")
            back_to_menu()

        CUSTO_DE_PRODUCAO = input("novo custo de produção: ")
        # verificando se CUSTO_D_PRODUCAO é um campo vazio
        if (CUSTO_DE_PRODUCAO == ""):
            print("O campo Custo de Produção deve ser preenchido, tente novamente")
            back_to_menu()

        VALOR_DE_VENDA = input("novo valor de venda")
        # verificando se VALOR_DE_VENDA é um campo vazio
        if (VALOR_DE_VENDA == ""):
            print("O campo Valor de Venda deve ser preenchido, tente novamente")
            back_to_menu()
        
        for data in Table:
            if (data['NF'] == NF):
                Table[indeks]['NOME'] = NOME
                Table[indeks]['FORNECEDOR'] = FORNECEDOR
                Table[indeks]['QT'] = QT
                Table[indeks]['CUSTO DE PRODUÇÂO'] = CUSTO_DE_PRODUCAO
                Table[indeks]['VALOR DE VENDA'] = VALOR_DE_VENDA
                # Grava novos dados no arquivo CSV (reescreve)
                with open(arquivo_CSV, mode="w", newline='', encoding="ISO-8859-1") as csv_file:
                    fieldnames = ['NF', 'NOME', 'FORNECEDOR','QT','CUSTO DE PRODUÇÂO','VALOR DE VENDA']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in Table:
                        writer.writerow({'NF': new_data['NF'], 'NOME': new_data['NOME'], 'FORNECEDOR': new_data['FORNECEDOR'], 'QT': new_data['QT'],'CUSTO DE PRODUÇÂO': new_data['CUSTO DE PRODUÇÂO'],'VALOR DE VENDA': new_data['VALOR DE VENDA']})
                
            indeks = indeks + 1
            
    else:
        print("NF Inexistente, tente novamente")
        back_to_menu




       

    back_to_menu()

# função deletar item (3)   
def delete_Table():
    clear_screen()
    Table = []

    with open(arquivo_CSV, mode="r", encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Table.append(row)

    # abra o arquivo CSV com o prettytable
    with open(arquivo_CSV, encoding="ISO-8859-1") as f:
        tabela = from_csv(f)
        tabela.align = "c"
        print(tabela)
        
    NF = input("Excluir itens com NF : ")
    
    existe = 0
    indeks = 0
    for data in Table:
        if (data['NF'] == NF):
            Table.remove(Table[indeks])
            existe = existe + 1
        indeks = indeks + 1

    if (existe == 1):
        print("Produto removido com sucesso!")
    else:
        print("Produto Inexistente, tente novamente")   
    
    # Grava novos dados no arquivo CSV (reescreve)
    with open(arquivo_CSV, mode="w", newline='', encoding="ISO-8859-1") as csv_file:
        fieldnames = ['NF', 'NOME', 'FORNECEDOR', 'QT','CUSTO DE PRODUÇÂO', 'VALOR DE VENDA']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Table:
            writer.writerow({'NF': new_data['NF'], 'NOME': new_data['NOME'], 'FORNECEDOR': new_data['FORNECEDOR'], 'QT': new_data['QT'],'CUSTO DE PRODUÇÂO': new_data['CUSTO DE PRODUÇÂO'],'VALOR DE VENDA': new_data['VALOR DE VENDA']}) 

    
    back_to_menu()
       

        
# função buscar item (4)        
def search_Table():
    clear_screen()
    Table = []

    #LER TABELA
    with open(arquivo_CSV, mode="r", encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Table.append(row)

    NF = input("Pesquisar por código> ")

    data_found = []
    existe = 0
    
    # procurando por Table (4)
    
    x = PrettyTable()
    indeks = 0
    for data in Table:
        if (data['NF'] == NF):
            data_found = Table[indeks]
            existe = 1
        indeks = indeks + 1
    
    
    if (existe == 1):
        #CALCULO DO LUCRO NA FUNÇAO BUSCAR (4)
        custos = float(data_found['QT']) * float(data_found['CUSTO DE PRODUÇÂO'])
        ganhos = float(data_found['QT']) * float(data_found['VALOR DE VENDA'])
        LUCRO  = float(ganhos - custos)
        
        #PRINT NOS DADOS ENCONTRADOS (4)
        print("\nDados Encontrados: \n")
        x.field_names = ["NOME", "FORNECEDOR", "QT", "CUSTO DE PRODUÇÂO","VALOR DE VENDA","LUCRO"]
        x.add_row([data_found['NOME'],data_found['FORNECEDOR'],data_found['QT'],data_found['CUSTO DE PRODUÇÂO'],data_found['VALOR DE VENDA'],LUCRO])
        print(x)
    else:
        print("Nenhum dado encontrado")
        
    


    
    
    back_to_menu()

# Para manter o menu sempre aberto
if __name__ == "__main__":
    while True:
        show_menu()


# 

# In[ ]:





# In[ ]:





# In[ ]:




