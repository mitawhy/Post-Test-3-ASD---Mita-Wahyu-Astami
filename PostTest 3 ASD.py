import os
from prettytable import PrettyTable
os.system("cls")

# Data
Nama_Owner = ["Ana", "Melly", "Mita", "Prapto"]
Nama_Kucing = ["Amek", "Ocil", "Semprul", "Bimbim"]
BB_Kucing = [3.5, 2, 1, 4]
Penyakit_Kucing = ["Scabies", "Infeksi Jamur", "Cacingan", "Diabetes"]
Tgl_Kedatangan = ["7 Juli", "11 Maret", "12 Desember", "3 Maret"]

# Node
class Node(object):
    def __init__(self, initvalue): # Fungsi untuk menginisialisasi objek node
            self.value = initvalue
            self.next = None # Menetapkan data Inisialisasi berikutnya sebagai null
            self.previous = None # Menetapkan data Inisialisasi sebelumnya sebagai null

    def getvalue(self): # Mengembalikan data yang disimpan
        return self.value
   
    def getNext(self): # Mengembalikan node berikutnya
        return self.next
    
    def setvalue(self,newvalue): # Mengatur ulang pointer ke node baru
        self.value=newvalue

# LinkedList
class LinkedList:
    def __init__(self, head, next = None): # Fungsi untuk menginisialisasi objek Linked List
        self.head = head
        self.next = next

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

def makelist(data):
    head = LinkedList(data[0])
    for data in data[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = LinkedList(data)
    return head

def printlist(self, self1, self2, self3, self4):
    if self.head is None:
        print("The linked list is empty.")
    else:
        ptr = self
        ptr1 = self1
        ptr2 = self2
        ptr3 = self3
        ptr4 = self4
        i = 0
        table = PrettyTable(["No.","Nama Owner","Nama Kucing","BB Kucing","Penyakit Kucing", "Tanggal Kedatangan"]) # Membuat tabel
        while ptr:
            table.add_row([i+1, ptr.head, ptr1.head, ptr2.head, ptr3.head, ptr4.head])
            ptr = ptr.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            ptr3 = ptr3.next
            ptr4 = ptr4.next
            i += 1
        print(table)

# Function
def insert(): # Memasukkan/Menyisipkan data
    no = input("Input Nama Owner: ")
    Nama_Owner.append(no)

    nk = input("Input Nama Kucing: ")
    Nama_Kucing.append(nk)

    bbk = int(input("Input Berat Badan Kucing: "))
    BB_Kucing.append(bbk)

    pk = input("Input Penyakit Kucing: ")
    Penyakit_Kucing.append(pk)

    tk = input("Input Tanggal Kedatangan: ")
    Tgl_Kedatangan.append(tk)

    os.system("cls")
    print("Data berhasil ditambahkan")

    namaowner = makelist(Nama_Owner)
    namakucing = makelist(Nama_Kucing)
    bbkucing = makelist(BB_Kucing)
    penyakitkucing = makelist(Penyakit_Kucing)
    tglkedatangan = makelist(Tgl_Kedatangan)
    printlist(namaowner, namakucing, bbkucing, penyakitkucing, tglkedatangan)

def delete(): # Menghapus data
    while True:
        namaowner = makelist(Nama_Owner)
        namakucing = makelist(Nama_Kucing)
        bbkucing = makelist(BB_Kucing)
        penyakitkucing = makelist(Penyakit_Kucing)
        tglkedatangan = makelist(Tgl_Kedatangan)
        printlist(namaowner, namakucing, bbkucing, penyakitkucing, tglkedatangan)

        index = int(input("Input Index Pelanggan Ingin Dihapus : ")) 
        index = index - 1
        hapus = index
        if index == hapus:
            Nama_Owner.pop(index)
            print("Data berhasil dihapus")
            
            namaowner = makelist(Nama_Owner)
            namakucing = makelist(Nama_Kucing)
            bbkucing = makelist(BB_Kucing)
            penyakitkucing = makelist(Penyakit_Kucing)
            tglkedatangan = makelist(Tgl_Kedatangan)
            printlist(namaowner, namakucing, bbkucing, penyakitkucing, tglkedatangan)

            return
        else:
            print("Masukkan inputan yang benar!")

def menu():
    os.system("cls")
    ulang = "y"
    while(ulang == "y"):
        print("\n======= MENU =======")
        print(" 1. Input Data")
        print(" 2. View Data")
        print(" 3. Delete Data")
        print(" 4. Exit")
        print("="*20)
        
        choose = int(input("Masukan Pilihan Anda (1/2/3/4): "))
        if choose == 1: 
            os.system("cls") 
            insert()
        elif choose == 2:
            os.system("cls")  
            namaowner = makelist(Nama_Owner)
            namakucing = makelist(Nama_Kucing)
            bbkucing = makelist(BB_Kucing)
            penyakitkucing = makelist(Penyakit_Kucing)
            tglkedatangan = makelist(Tgl_Kedatangan)
            printlist(namaowner, namakucing, bbkucing, penyakitkucing, tglkedatangan)
        elif choose == 3:
            os.system("cls")
            delete()
        elif choose == 4:
            os.system("cls")
            print("\nProgram selesai.")
            exit()
        else:
            os.system("cls")
            print("Masukkan inputan yang benar")

# Start
menu()