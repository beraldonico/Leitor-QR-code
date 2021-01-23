import read_QR
import create_QR

print('------------------------------------------------------')
print('Teste da funcionalidade de leitura e criação de QRcode')
print('------------------------------------------------------')
while True:
    print('Selecione uma opção:')
    print('1 - Ler QR')
    print('2 - Gerar QR')
    print('3 - Sair da funcionalidade de QRcode')
    try:
        entrada = int(input('Opção:'))
    except ValueError:
        entrada = None
    if entrada == 1:
        read_QR.read()
    elif entrada == 2:
        create_QR.create()
    elif entrada == 3:
        break
    else:
        print('opção invalida\n')
print("fim da execução")