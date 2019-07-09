import os
import sys
import time

data = []
count = 0

def perulangan():
    global data, count
    try:
        lis = open("list.txt", "r")

    except IOError:
        open("list.txt", "w")
        perulangan()

    except ValueError:
        print " Gak Cocok..."

    
    else:
        try:
            while True:
                print 
                dat = open("list.txt", "r")
                da = dat.readlines()
                print " ================================="
                print " [#] Jumlah Data: ", len(da)
                word = raw_input(" ["+str(count)+"] Masukkan Data: ")
                count += 1
                if word == "1":
                    print " Success"
                    sys.exit()

                else: 
                    print " Fail..."
                    print
                    data.append(word)
                    tam = open("list.txt", "a")
                    tam.write(word + "\n")
                    tam.close()
                    for i in data:
                        print " [#] [ " + i + " ]"

        except KeyboardInterrupt:
            try:
                def opsi():
                            
                    print
                    print " ============================="
                    print "  [1] Hapus Data...?"
                    print "  [2] Keluar Dari Program.."
                    print "  [3] Kembali Ke Program"
                    print " ============================="
                    op = raw_input(" Pilih => ")
                    if op == "1":
                        os.system("del list.txt")
                        os.system("rm -f list.txt")
                        print " Data Terhapus"
                    elif op == "2":
                        sys.exit()
                        print " Keluar Dari Program"
                    elif op == "3":
                        perulangan()
                    else:
                        print " Salah Ndolll"
                        opsi()
                opsi()

            except KeyboardInterrupt:
                print
                print " Keluar Dari Program.."
                sys.exit()
    
   

def main():
    perulangan()

if __name__=="__main__":
    main()
