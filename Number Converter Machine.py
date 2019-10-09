repeat = "Y"
while repeat=="Y"or"y":
    print("\n\n"+"="*40,"\n\tNUMBER CONVERTER MACHINE\n"+"\t\t oleh\n"+"\t hermawansent@gmail.com\n"+"="*40)
    print("1. Biner\n2. Desimal\n3. Oktal\n4. Hexadesimal")
    menu_var = input("Pilih bilangan yang ingin dikonversi : ")
    #Biner
    if menu_var=="1" or menu_var=="biner" or menu_var=="Biner" or menu_var=="BINER":
        print("\n\n"+"="*5,"\nBINER\n"+"="*5)
        dec_var = int(input("Masukkan angka biner : "),2)
        oct_var = oct(dec_var)[2:]
        hex_var = hex(dec_var)[2:]
        print("\nDesimal     = ",dec_var,"\nOktal       = ",oct_var,"\nHexadesimal = ",hex_var)
    #Desimal
    elif menu_var=="2" or menu_var=="desimal" or menu_var=="Desimal" or menu_var=="DESIMAL":
        print("\n\n"+"="*7,"\nDESIMAL\n"+"="*7)
        dec_var = int(input("Masukkan angka desimal : "))
        bin_var = bin(dec_var)[2:]
        oct_var = oct(dec_var)[2:]
        hex_var = hex(dec_var)[2:]
        print("\nBiner       = ",bin_var,"\nOktal       = ",oct_var,"\nHexadesimal = ",hex_var)
    #Oktal
    elif menu_var=="3" or menu_var=="oktal" or menu_var=="Oktal" or menu_var == "OKTAL":
        print("\n\n"+"="*5,"\nOKTAL\n"+"="*5)
        dec_var = int(input("Masukkan angka oktal : "),8)
        bin_var = bin(dec_var)[2:]
        hex_var = hex(dec_var)[2:]
        print("\nBiner       = ",bin_var,"\nDesimal     = ",dec_var,"\nHexadesimal = ",hex_var)
    #Hex
    elif menu_var=="4" or menu_var=="hex" or menu_var=="Hex" or menu_var=="HEX" or menu_var=="hexadesimal" or menu_var=="Hexadesimal" or menu_var=="HEXADESIMAL":
        print("\n\n"+"="*11,"\nHEXADESIMAL\n"+"="*11)
        dec_var = int(input("Masukkan angka Hexadesimal : "),16)
        bin_var = bin(dec_var)[2:]
        oct_var = oct(dec_var)[2:]
        print("\nBiner     = ",bin_var,"\nDesimal   = ",dec_var,"\nOktal     = ",oct_var)
    else:
        print("\nInput tidak valid, Program diakhiri")
        break
    print()
    print("="*28)
    repeat = input("Want to try again? [Y/N] : ")
    print("="*28)
    if repeat=="N" or repeat=="n" or repeat=="no" or repeat=="No" or repeat=="NO" or repeat=="nO":
        print("Program diakhiri, Terimakasih telah menggunakan")
        break




    




    
