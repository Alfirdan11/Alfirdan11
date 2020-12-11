print("Fitur Kalkulator Biaya Kuliah")
print("=============================")

nim = input("Masukkan NIM:")
if nim[5:7] == '20' and len(nim) == 10:
    bop = 4000000
    sks = 200000
    ang = "2020"
    print("BOP Mahasiswa angkatan", ang, "adalah", bop)
    rt = eval(input("Jumlah SKS yang diambil semester ini:"))
    if rt > 15:
        tsks=(rt-15)*sks
        total=bop + tsks
        print("Biaya tambahan untuk", rt - 15, "SKS: ", tsks)
        print("Total biaya kuliah: ", total, "\n")
        subs = input("Apakah kamu ingin mengajukan subsidi biaya kuliah (Y/T):")
        if subs == 'Y' or subs =='y':
            tar = 0
            avg = 0
            sem1 = eval(input("Semester berapa anda sekarang:"))
            if sem1 > 1 and sem1 < 9:
                for i in range(1, sem1):
                    ip = eval(input("Masukkan IP Semester " + str(i) + ": "))
                    if ip <= 4:
                        avg = avg + ip
                    else:
                        print("Inputan Semester ke-", i," Salah")
                        import sys
                        sys.exit()
                tar = avg/(sem1-1)
                srsubs = (round(tar, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(srsubs))
                print("Total biaya kuliah anda: Rp.", total - round(srsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
        elif subs == 'T' or subs =='t':
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan Salah")
    elif rt == 15:
        subs = input("\nApakah kamu ingin mengajukan subsidi biaya kuliah (Y/T):")
        if subs == 'Y' or subs =='y':
            tar = 0
            avg = 0
            sem1 = eval(input("Semester berapa anda sekarang:"))
            if sem1 > 1 and sem1 < 9:
                for i in range(1, sem1):
                    ip = eval(input("Masukkan IP Semester "+ str(i) + ": "))
                    if ip <= 4:
                        avg = avg + ip
                    else:
                        print("Inputan Semester ke-", i," Salah")
                        import sys
                        sys.exit()
                tar = avg/(sem1-1)
                srsubs = (round(tar, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(srsubs))
                print("Total biaya kuliah anda: Rp.", bop - round(srsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
        elif subs == 'T' or subs =='t':
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan Salah")
    else:
        print("SKS yang anda Masukkan Kurang")
elif nim[5:7] =='19' and len(nim) ==10:
    bop = 3500000
    sks = 175000
    print("BOP Mahasiswa angkatan 2019 adalah", bop)
    rt = eval(input("Jumlah SKS yang diambil semester ini:"))
    if rt > 15:
        tsks=(rt-15)*sks
        total=bop + tsks
        print("Biaya tambahan untuk", rt - 15, "SKS: ", tsks)
        print("Total biaya kuliah: ", total, "\n")
        subs = input("Apakah kamu ingin mengajukan subsidi biaya kuliah (Y/T):")
        if subs == 'Y' or subs =='y':
            tar = 0
            avg = 0
            sem1 = eval(input("Semester berapa anda sekarang:"))
            if sem1 > 1 and sem1 < 9:
                for i in range(1, sem1):
                    ip = eval(input("Masukkan IP Semester " + str(i) + ": "))
                    if ip <= 4:
                        avg = avg + ip
                    else:
                        print("Inputan Semester ke-", i," Salah")
                        import sys
                        sys.exit()
                tar = avg/(sem1-1)
                srsubs = (round(tar, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(srsubs))
                print("Total biaya kuliah anda: Rp.", total - round(srsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
        elif subs == 'T' or subs =='t':
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan Salah")
    elif rt == 15:
        subs = input("\nApakah kamu ingin mengajukan subsidi biaya kuliah (Y/T):")
        if subs == 'Y' or subs =='y':
            tar = 0
            avg = 0
            sem1 = eval(input("Semester berapa anda sekarang:"))
            if sem1 > 1 and sem1 < 9:
                for i in range(1, sem1):
                    ip = eval(input("Masukkan IP Semester "+ str(i) + ": "))
                    if ip <= 4:
                        avg = avg + ip
                    else:
                        print("Inputan Semester ke-", i," Salah")
                        import sys
                        sys.exit()
                tar = avg/(sem1-1)
                srsubs = (round(tar, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(srsubs))
                print("Total biaya kuliah anda: Rp.", bop - round(srsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
        elif subs == 'T' or subs =='t':
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan Salah")
    else:
        print("SKS yang anda Masukkan Kurang")
elif nim[5:7] =='18' and len(nim) ==10:
    bop = 3200000
    sks = 150000
    print("BOP Mahasiswa angkatan 2018 adalah", bop)
    rt = eval(input("Jumlah SKS yang diambil semester ini:"))
    if rt > 15:
        tsks=(rt-15)*sks
        total=bop + tsks
        print("Biaya tambahan untuk", rt - 15, "SKS: ", tsks)
        print("Total biaya kuliah: ", total, "\n")
        subs = input("Apakah kamu ingin mengajukan subsidi biaya kuliah (Y/T):")
        if subs == 'Y' or subs =='y':
            tar = 0
            avg = 0
            sem1 = eval(input("Semester berapa anda sekarang:"))
            if sem1 > 1 and sem1 < 9:
                for i in range(1, sem1):
                    ip = eval(input("Masukkan IP Semester " + str(i) + ": "))
                    if ip <= 4:
                        avg = avg + ip
                    else:
                        print("Inputan Semester ke-", i," Salah")
                        import sys
                        sys.exit()
                tar = avg/(sem1-1)
                srsubs = (round(tar, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(srsubs))
                print("Total biaya kuliah anda: Rp.", total - round(srsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
        elif subs == 'T' or subs =='t':
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan Salah")
    elif rt == 15:
        subs = input("\nApakah kamu ingin mengajukan subsidi biaya kuliah (Y/T):")
        if subs == 'Y' or subs =='y':
            tar = 0
            avg = 0
            sem1 = eval(input("Semester berapa anda sekarang:"))
            if sem1 > 1 and sem1 < 9:
                for i in range(1, sem1):
                    ip = eval(input("Masukkan IP Semester "+ str(i) + ": "))
                    if ip <= 4:
                        avg = avg + ip
                    else:
                        print("Inputan Semester ke-", i," Salah")
                        import sys
                        sys.exit()
                tar = avg/(sem1-1)
                srsubs = (round(tar, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(srsubs))
                print("Total biaya kuliah anda: Rp.", bop - round(srsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
        elif subs == 'T' or subs =='t':
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan Salah")
    else:
        print("SKS yang anda Masukkan Kurang")
elif nim[5:7] =='17' and len(nim) ==10:
    bop = 2800000
    sks = 130000
    print("BOP Mahasiswa angkatan 2017 adalah", bop)
    rt = eval(input("Jumlah SKS yang diambil semester ini:"))
    if rt > 15:
        tsks=(rt-15)*sks
        total=bop + tsks
        print("Biaya tambahan untuk", rt - 15, "SKS: ", tsks)
        print("Total biaya kuliah: ", total, "\n")
        subs = input("Apakah kamu ingin mengajukan subsidi biaya kuliah (Y/T):")
        if subs == 'Y' or subs =='y':
            tar = 0
            avg = 0
            sem1 = eval(input("Semester berapa anda sekarang:"))
            if sem1 > 1 and sem1 < 9:
                for i in range(1, sem1):
                    ip = eval(input("Masukkan IP Semester " + str(i) + ": "))
                    if ip <= 4:
                        avg = avg + ip
                    else:
                        print("Inputan Semester ke-", i," Salah")
                        import sys
                        sys.exit()
                tar = avg/(sem1-1)
                srsubs = (round(tar, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(srsubs))
                print("Total biaya kuliah anda: Rp.", total - round(srsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
        elif subs == 'T' or subs =='t':
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan Salah")
    elif rt == 15:
        subs = input("\nApakah kamu ingin mengajukan subsidi biaya kuliah (Y/T):")
        if subs == 'Y' or subs =='y':
            tar = 0
            avg = 0
            sem1 = eval(input("Semester berapa anda sekarang:"))
            if sem1 > 1 and sem1 < 9:
                for i in range(1, sem1):
                    ip = eval(input("Masukkan IP Semester "+ str(i) + ": "))
                    if ip <= 4:
                        avg = avg + ip
                    else:
                        print("Inputan Semester ke-", i," Salah")
                        import sys
                        sys.exit()
                tar = avg/(sem1-1)
                srsubs = (round(tar, 2)/4.0 * 1000000)
                print("Anda mendapatkan subsidi sebesar Rp.", round(srsubs))
                print("Total biaya kuliah anda: Rp.", bop - round(srsubs))
            else:
                print("Anda tidak dapat mengajukan subsidi.")
        elif subs == 'T' or subs =='t':
            print("Penghitungan biaya kuliah selesai.")
        else:
            print("Inputan Salah")
    else:
        print("SKS yang anda Masukkan Kurang")
else:
    print("NIM anda Tidak Benar")
