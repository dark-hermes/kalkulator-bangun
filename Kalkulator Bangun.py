ulang = ("Y")
while ulang=="Y" or ulang=="y":
    print("="*66)
    print("\t\t   KALKULATOR BANGUN MATEMATIKA")
    print("\tkalkulator ini menampilkan hasil dalam satuan cm")
    print("pastikan nilai yang anda input adalah dalam satuan centimeter (cm)")
    print("\t\t\t©Hermawan, S.S.")
    print("="*66)
    print("1. Bangun Datar\n2. Bangun Ruang\n3. Batalkan Program")
    menu_var = input("\nPilih perintah : ")

#option akhiri program
    if menu_var=="3":
        print("\n\n")
        print("="*18+"\nPROGRAM DIBATALKAN\n"+"="*18)
        break

#option bangun datar
    elif menu_var=="1":
        print("\n")
        print("="*12)
        print("Bangun Datar")
        print("="*12)
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Jajar Genjang")
        print("4. Segitiga")
        print("5. Belah Ketupat")
        print("6. Layang-Layang")
        print("7. Trapesium")
        print("8. Lingkaran")
        bd_var = input("\nPilih perintah : ")

       #Persegi
        if bd_var=="1":
            print("\n")
            print("="*7)
            print("PERSEGI")
            print("="*7)
            print("1. Keliling")
            print("2. Luas")
            op_var = input("\nPilih perintah : ")
            #Keliling persegi
            if op_var=="1":
                print("\n")
                print("="*16)
                print("KELILING PERSEGI")
                print("="*16)
                sisi = float(input("Masukkan panjang sisi : "))
                print("Keliling Persegi adalah", 4*sisi,"cm")
            #Luas persegi
            elif op_var=="2":
                print("\n")
                print("="*12)
                print("LUAS PERSEGI")
                print("="*12)
                sisi = float(input("Masukkan panjang sisi : "))
                print("Luas Persegi adalah", sisi*sisi,"cm^2")

        #Persegi Panjang
        elif bd_var=="2":
            print("\n")
            print("="*15)
            print("PERSEGI PANJANG")
            print("="*15)
            print("1. Keliling")
            print("2. Luas")
            op_var = input("\nPilih perintah : ")
            #Keliling persegi panjang
            if op_var=="1":
                print("\n")
                print("="*24)
                print("KELILING PERSEGI PANJANG")
                print("="*24)
                p = float(input("Masukkan panjang persegi panjang : "))
                l = float(input("Masukkan lebar persegi panjang   : "))
                print("Keliling persegi panjang adalah", (2*p)+(2*l),"cm")
            #Luas Persegi panjang
            elif op_var=="2":
                print("\n")
                print("="*20)
                print("LUAS PERSEGI PANJANG")
                print("="*20)
                p = float(input("Masukkan panjang persegi panjang : "))
                l = float(input("Masukkan lebar persegi panjang   : "))
                print("Luas persegi panjang adalah", p*l,"cm^2")
        
        #Jajar Genjang
        elif bd_var=="3":
            print("\n\n"+"="*13,"\nJAJAR GENJANG\n"+"="*13)
            print("1. Keliling")
            print("2. Luas")
            op_var = input("\nPilih perintah : ")
            #Keliling jajar genjang
            if op_var=="1":
                print("\n\n"+"="*22,"\nKELILING JAJAR GENJANG\n"+"="*22)
                a = float(input("Masukkan panjang sisi a : "))
                b = float(input("Masukkan panjang sisi b : "))
                c = float(input("Masukkan panjang sisi c : "))
                d = float(input("Masukkan panjang sisi d : "))
                print("Keliling jajar genjang adalah",a+b+c+d,"cm")
            #Luas jajar genjang
            elif op_var=="2":
                print("\n\n"+"="*18,"\nLUAS JAJAR GENJANG\n"+"="*18)
                a= float(input("Input nilai alas (a) jajar genjang    : "))
                t = float(input("Input nilai tinggi (t) jajar genjang : "))
                print("Luas jajar genjang adalah", a*t, "cm^2")
        
        #segitiga
        elif bd_var=="4":
            print("\n\n"+"="*8,"\nSEGITIGA\n"+"="*8)
            print("1. Keliling")
            print("2. Luas")
            op_var = input("Pilih perintah : ")
            #keliling segitiga
            if op_var=="1":
                print("\n\n"+"="*17,"\nKELILING SEGITIGA\n"+"="*17)
                s1 = float(input("Input nilai sisi 1 : "))
                s2 = float(input("Input nilai sisi 2 : "))
                s3 = float(input("Input nilai sisi 3 : "))
                print("Keliling segitiga adalah", s1+s2+s3,"cm")
            #luas segitiga
            elif op_var=="2":
                print("\n\n"+"="*13,"\nLUAS SEGITIGA\n"+"="*13)
                a = float(input("Input nilai alas (a)   : "))
                t = float(input("Input nilai tinggi (t) :"))
                print("Luas segitiga adalah", a*t/2,"cm^2")
        #Belah ketupat
        elif bd_var=="5":
            print("\n\n"+"="*13,"\nBELAH KETUPAT\n"+"="*13)
            print("1. Keliling")
            print("2. Luas")
            op_var = input("Pilih perintah : ")
            #Keliling belah ketupat
            if op_var=="1":
                print("\n\n"+"="*22,"\nKELILING BELAH KETUPAT\n"+"="*22)
                s = float(input("Input nilai sisi (s) : "))
                print("Keliling belah ketupat adalah",4*s,"cm")
            #Luas belah ketupat
            elif op_var=="2":
                print("\n\n"+"="*22,"\nLUAS BELAH KETUPAT\n"+"="*22)
                d1 = float(input("Input nilai diagonal satu (d1) : "))
                d2 = float(input("Input nilai diagonal dua (d2)  : "))
                print("Luas belah ketupat adalah", d1*d2/2,"cm^2")
        #Layang-layang
        elif  bd_var=="6":
            print("\n\n"+"="*13,"\nLAYANG-LAYANG\n"+"="*13)
            print("1. Keliling\n2. Luas")
            op_var = input("Pilih perintah : ")
            #Keliling layang-layang
            if op_var=="1":
                print("\n\n"+"="*22,"\nKELILING LAYANG-LAYANG\n"+"="*22)
                s1 = float(input("Input nilai sisi sejajar pendek  : "))
                s2 = float(input("Input nilai sisi sejajar panjang : "))
                print("Keliling layang-layang adalah", (2*s1)+(2*s2),"cm")
            #Luas layang-layang
            elif op_var=="2":
                print("\n\n"+"="*18,"\nLUAS LAYANG-LAYANG\n"+"="*18)
                d1 = float(input("Input nilai diagonal satu (d1) : "))
                d2 = float(input("Input nilai diagonal dua (d2)  : "))
                print("Luas layang-layang adalah", d1*d2/2,"cm^2")
        
        #Trapesium
        elif bd_var=="7":
            print("\n\n"+"="*9,"\nTRAPESIUM\n"+"="*9)
            print("1. Keliling\n2. Luas")
            op_var = input("Pilih perintah : ")
            #Keliling trapesium
            if op_var == "1":
                print("\n\n"+"="*18,"\nKELILING TRAPESIUM\n"+"="*18)
                s1 = float(input("Input nilai sisi satu (s1)  : "))
                s2 = float(input("Input nilai sisi dua (s2)   : "))
                s3 = float(input("Input nilai sisi tiga (s3)  : "))
                s4 = float(input("Input nilai sisi empat (s4) : "))
                print("Keliling trapesium adalah", s1+s2+s3+s4,"cm")
            #Luas Trapesium
            elif op_var == "2":
                print("\n\n"+"="*14,"\nLUAS TRAPESIUM\n"+"="*14)
                a = float(input("Input nilai sisi (a)   : "))
                b = float(input("Input nilai sisi (b)   : "))
                t = float(input("Input nilai tinggi (t) : "))
                print("Luas Trapesium adalah", (a+b)*t/2,"cm^2")
        
        #Lingkaran
        elif bd_var=="8":
            print("\n\n"+"="*9,"\nLINGKARAN\n"+"="*9)
            print("1. Keliling\n2. Luas")
            op_var = input("Pilih perintah : ")
            #Keliling Lingkaran
            if op_var=="1":
                print("\n\n"+"="*18,"\nKELILING LINGKARAN\n"+"="*18)
                phi = 3.14
                phi1 = 22/7
                r = float(input("Input jari-jari lingkaran (r) : "))
                if (r%7)==0:
                    print("Keliling lingkaran adalah", 2*phi1*r,"cm")
                else:
                    print("Keliling lingkaran adalah", 2*phi*r,"cm")
            #Luas lingkaran
            elif op_var=="2":
                print("\n\n"+"="*14,"\nLUAS LINGKARAN\n"+"="*14)
                phi = 3.14
                phi1 = 22/7
                r = float(input("Input jari-jari lingkaran (r) : "))
                if (r%7)==0:
                    print("Luas lingkaran adalah", phi1*r*r,"cm^2")
                else:
                    print("Luas lingkaran adalah", phi*r*r,"cm^2")

        #Input tidak valid
        else:
            print("\n\nPERINTAH TIDAK VALID\nPROGRAM DIAKHIRI")
            break


#Bangun Ruang
    elif menu_var=="2":
        print("\n\n"+"="*12,"\nBANGUN RUANG\n"+"="*12)
        print("1. Kubus\n2. Balok\n3. Tabung\n4. Kerucut\n5. Bola\n")
        br_var = input("Pilih perintah : ")

        #Kubus
        if br_var=="1":
            print("\n\n"+"="*5,"\nKUBUS\n"+"="*5)
            print("1. Luas Permukaan\n2. Volume")
            op_var = input("Pilih perintah : ")
            #Luas permukaan kubus
            if op_var=="1":
                print("\n\n"+"="*20,"\nLUAS PERMUKAAN KUBUS\n"+"="*20)
                s = float(input("Input nilai sisi : "))
                print("Luas permukaan kubus adalah", 6*s**2,"cm^2")
            #Volume kubus
            elif op_var=="2":
                print("\n\n"+"="*14,"\nVOLUME KUBUS\n"+"="*14)
                s = float(input("Input nilai sisi : "))
                print("Volume kubus adalah", s**3,"cm^3")
        
        #Balok
        elif br_var=="2":
            print("\n\n"+"="*5,"\nBALOK\n"+"="*5)
            print("1. Luas Permukaan\n2. Volume")
            op_var = input("Pilih perintah : ")
            #luas permukaan balok
            if op_var=="1":
                print("\n\n"+"="*20,"\nLUAS PERMUKAAN BALOK\n"+"="*20)
                p = float(input("Input nilai panjang (p) : "))
                l = float(input("Input nilai lebar (l)   : "))
                t = float(input("Input nilai tinggi (t)  :"))
                print("Luas permukaan balok adalah", 2*(p*l)+2*(p*t)+2*(l*t),"cm^2")
            #volume balok
            elif op_var=="2":
                print("\n\n"+"="*12,"\nVOLUME BALOK\n"+"="*12)
                p = float(input("Input nilai panjang (p) : "))
                l = float(input("Input nilai lebar   (l) : "))
                t = float(input("Input nilai tinggi  (t) : "))
                print("Volume balok adalah", p*l*t,"cm^3")
        
        #Tabung
        elif br_var=="3":
            print("\n\n"+"="*6,"\nTABUNG\n"+"="*6)
            print("1. Luas Permukaan (dengan tutup)\n2. Luas Permukaan (tanpa tutup)\n3. Volume\n4. Luas Selimut")
            op_var = input("Pilih perintah : ")
            #Luas Permukaan tabung
            if op_var=="1":
                print("\n\n"+"="*21,"\nLUAS PERMUKAAN TABUNG\n"+"="*21)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari alas tabung (r) : "))
                t = float(input("Input nilai tinggi tabung         (t) : "))
                if (r%7)==0:
                    print("Luas permukaan tabung adalah",2*phi2*r*(r+t),"cm^2")
                else:
                    print("Luas permukaan tabung adalah",2*phi*r*(r+t),"cm^2")
            #Luas permukaan tabung tanpa tutup
            elif op_var=="2":
                print("\n\n"+"="*34,"\nLUAS PERMUKAAN TABUNG (TANPA TUTUP)\n"+"="*34)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari alas tabung (r) : "))
                t = float(input("Input nilai tinggi tabung         (t) : "))
                if (r%7)==0:
                    print("Luas permukaan tabung adalah",phi2*r*(r+2*t),"cm^2")
                else:
                    print("Luas permukaan tabung adalah",phi*r*(r+2*t),"cm^2")
            #Volume tabung
            elif op_var=="3":
                print("\n\n"+"="*13,"\nVOLUME TABUNG\n"+"="*13)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari alas tabung (r) : "))
                t = float(input("Input nilai tinggi tabung         (t) : "))
                if (r%7)==0:
                    print("Volume tabung adalah",phi2*r*r*t,"cm^3")
                else:
                    print("Volume tabung adalah",phi*r*r*t,"cm^3")
            #Luas selimut tabung
            elif op_var=="4":
                print("\n\n"+"="*19,"\nLUAS SELIMUT TABUNG\n"+"="*19)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari alas tabung (r) : "))
                t = float(input("Input nilai tinggi tabung         (t) : "))
                if (r%7)==0:
                    print("Volume tabung adalah",2*phi2*r*t,"cm^2")
                else:
                    print("Volume tabung adalah",2*phi*r*t,"cm^2")
        
        #Kerucut
        elif br_var=="4":
            print("\n\n"+"="*7,"\nKERUCUT\n"+"="*7)
            print("1. Luas permukaan\n2. Volume\n3. Luas selimut/Luas permukaan tanpa alas")
            op_var = input("Pilih perintah : ")
            #Luas permukaan kerucut
            if op_var=="1":
                print("\n\n"+"="*22,"\nLUAS PERMUKAAN KERUCUT\n"+"="*22)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari alas kerucut (r) : "))
                t = float(input("Input nilai tinggi kerucut         (t) : "))
                s = float(input("Input nilai garis pelukis kerucut  (s) : "))
                if (r%7)==0:
                    print("Luas permukaan kerucut adalah",phi2*r*(r+s),"cm^2")
                else:
                    print("Luas permukaan kerucut adalah",phi*r*(r+s),"cm^2")
            #Volume kerucut
            elif op_var=="2":
                print("\n\n"+"="*14,"\nVOLUME KERUCUT\n"+"="*14)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari alas kerucut (r) : "))
                t = float(input("Input nilai tinggi kerucut         (t) : "))
                if (r%7)==0:
                    print("Volume kerucut adalah",1/3*phi2*r**2*t,"cm^3")
                else:
                    print("Volume kerucut adalah",1/3*phi*r**2*t,"cm^3")
            #Luas selimut kerucut
            elif op_var=="3":
                print("\n\n"+"="*20,"\nLUAS SELIMUT KERUCUT\n"+"="*20)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari alas kerucut (r) : "))
                s = float(input("Input nilai garis pelukis kerucut  (s) : "))
                if (r%7)==0:
                    print("Luas selimut kerucut adalah",phi2*r*s,"cm^2")
                else:
                    print("Luas selimut kerucut adalah",phi*r*s,"cm^2")
        
        #Bola
        elif br_var=="5":
            print("\n\n"+"="*4,"\nBOLA\n"+"="*4)
            print("1. Luas Permukaan Bola\n2. Luas Permukaaan Setengah Bola Pejal\n3. Luas Permukaan Setengah Bola Berongga\n4. Volume Bola")
            op_var = input("Pilih Perintah : ")
            #Luas permukaan bola
            if op_var=="1":
                print("\n\n"+"="*19,"\nLUAS PERMUKAAN BOLA\n"+"="*19)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari bola (r) : "))
                if (r%7)==0:
                    print("Luas permukaan bola adalah",4*phi2*r**2,"cm^2")
                else:
                    print("Luas permukaan bola adalah",4*phi*r**2,"cm^2")
            #Luas permukaan setengah bola pejal
            if op_var=="2":
                print("\n\n"+"="*34,"\nLUAS PERMUKAAN SETENGAH BOLA PEJAL\n"+"="*34)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari bola (r) : "))
                if (r%7)==0:
                    print("Luas permukaan setengah bola pejal adalah",3*phi2*r**2,"cm^2")
                else:
                    print("Luas permukaan setengah bola pejal adalah",3*phi*r**2,"cm^2")
            #Luas permukaan setengah bola berongga
            if op_var=="3":
                print("\n\n"+"="*37,"\nLUAS PERMUKAAN SETENGAH BOLA BERONGGA\n"+"="*37)
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari bola (r) : "))
                if (r%7)==0:
                    print("Luas permukaan setengah bola berongga adalah",2*phi2*r**2,"cm^2")
                else:
                    print("Luas permukaan setengah bola berongga adalah",2*phi*r**2,"cm^2")
            #Volume bola
            print("\n\n"+"="*11,"\nVOLUME BOLA\n"+"="*11)
            if op_var=="4":
                phi = 3.14
                phi2 = 22/7
                r = float(input("Input nilai jari-jari bola (r) : "))
                if (r%7)==0:
                    print("Volume bola adalah",4/3*phi2*r**3,"cm^3")
                else:
                    print("Volume bola adalah",4/3*phi*r**3,"cm^3")

    print("\n")
    print("="*28)
    ulang = input("Want to try again? [Y/N] : ")
    print("="*28)
    if ulang=="N"or ulang=="n":
        print("Program diakhiri, Terimakasih telah menggunakan")
        break

