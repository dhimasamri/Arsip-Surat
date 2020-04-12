#NILATIL MOENA (131318002)
#Ilmu Komputer 2018
#Assignment 1_Web 112
#Arsip Surat

from PIL import ImageTk,Image
import Tkinter
import tkMessageBox
import time
import ttk
from Tkinter import Toplevel
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect('arsip_surat')

def start():
    window = Tkinter.Tk()
    desktop = Login(window)
    window.mainloop()

class Login:
    def __init__(self, jendela):
        self.jendela = jendela
        self.jendela.wm_iconbitmap("arsipsurat.ico")
        self.jendela.title("Arsip Surat")
        self.jendela.geometry("500x650")

        self.labelUsername = Tkinter.Label(self.jendela, text = "Username :")
        self.labelUsername.config(font=("Verdana", 15))
        self.entryUsername = Tkinter.Entry(self.jendela, width = 40)
        self.labelUsername.place(x = 60, y = 282)
        self.entryUsername.place(x = 190, y = 290)

        self.labelPassword = Tkinter.Label(self.jendela, text = "Password  :")
        self.labelPassword.config(font=("Verdana", 15))
        self.entryPassword = Tkinter.Entry(self.jendela, width = 40, show = '*')
        self.labelPassword.place(x = 60, y = 322)
        self.entryPassword.place(x = 190, y = 330)

        self.img = ImageTk.PhotoImage(file="arsip-surat.jpg")
        self.display = Tkinter.Label(self.jendela, image=self.img)
        self.display.place(y = 70)

        self.tombolLogin = Tkinter.Button(self.jendela, text = "Login", bg = "#87cdde", width = 36,
                                          command = self.login)
        self.tombolLogin.config(font=("Verdana", 12))
        self.tombolLogin.place(x = 60, y = 400)

        self.tombolLogged = Tkinter.Button(self.jendela, text = "Logged in as a User", bg = "#87cdde", width = 36,
                                          command = self.newWindow)
        self.tombolLogged.config(font=("Verdana", 12))
        self.tombolLogged.place(x = 60, y = 450)

        self.tombolKeluar = Tkinter.Button(self.jendela, text = "Keluar", bg = "#eb8a8a", width = 36,
                                           command = self.jendela.destroy)
        self.tombolKeluar.config(font=("Verdana", 12))
        self.tombolKeluar.place(x = 60, y = 500)

    def login(self):
        if self.entryUsername.get() == "" or self.entryPassword.get() == "":
            tkMessageBox.showwarning("Warning", "Username dan Password wajib terisi!")
        elif self.entryUsername.get() == "admin" and self.entryPassword.get() == "12345":
            tkMessageBox.showinfo("Info", "Login berhasil!")
            login = Tkinter.Tk()
            login.wm_iconbitmap("arsipsurat.ico")
            login.title("Arsip Surat - Admin")
            login.geometry("500x650")
            tabControl = ttk.Notebook(login)
        #Menu Home
            tab1 = ttk.Frame(tabControl)
            tabControl.add(tab1, text="Home")
            #Jam
            def jam():
                waktu = time.localtime()
                tahun = waktu[0]
                bulan = waktu[1]
                tanggal = waktu[2]
                jam = waktu[3]
                menit = waktu[4]
                detik = waktu[5]
                labelJam["text"] = "%02d/%02d/%4d %02d:%02d:%02d" % \
                                   (tanggal, bulan, tahun, jam, menit, detik)
            labelJam = Tkinter.Label(tab1, text = "Tanggal hari ini?")
            tombolJam = Tkinter.Button(tab1, text = "Cek Tanggal", bg = "#87cdde", width = 10,
                                       command = jam)
            labelJam.place(x = 290, y = 12)
            tombolJam.place(x = 405, y = 10)
            #Tentang Arsip Surat
            labelTentang = Tkinter.Label(tab1, text = "T E N T A N G   A R S I P   S U R A T", fg = "#256d80")
            labelTentang.config(font=("Verdana 12 bold"))
            labelTentang.place(x = 13, y = 50)
            messageTentang = Tkinter.Message(tab1, text = 'Arsip Surat merupakan aplikasi desktop '
                                             'untuk mengarsipkan surat masuk dan surat keluar yang '
                                             'ada pada sebuah instansi dengan tujuan untuk arsipan '
                                             'yang lebih rapih.', width = 460)
            messageTentang.config(font=("Verdana", 12))
            messageTentang.place(x = 10, y = 80)
            #Surat Masuk
            labelMasuk = Tkinter.Label(tab1, text = "S U R A T   M A S U K", fg = "#256d80")
            labelMasuk.config(font=("Verdana 12 bold"))
            labelMasuk.place(x = 13, y = 180)
            messageMasuk = Tkinter.Message(tab1, text = 'Surat Masuk adalah surat-surat yang diterima '
                                           'oleh suatu instansi yang berasal dari seseorang atau '
                                           'dari suatu instansi.', width = 460)
            messageMasuk.config(font=("Verdana", 12))
            messageMasuk.place(x = 10, y = 210)
            #Surat Keluar
            labelKeluar = Tkinter.Label(tab1, text = "S U R A T   K E L U A R", fg = "#256d80")
            labelKeluar.config(font=("Verdana 12 bold"))
            labelKeluar.place(x = 13, y = 300)
            messageKeluar = Tkinter.Message(tab1, text = 'Surat Keluar adalah surat-surat yang dikeluarkan/ '
                                            'dibuat oleh suatu instansi untuk dikirimkan kepada pihak  lain, '
                                            'perseorangan maupun kelompok.', width = 460)
            messageKeluar.config(font=("Verdana", 12))
            messageKeluar.place(x = 10, y = 330)
            #Keluar
            tombolKeluar1 = Tkinter.Button(tab1, text = "Keluar", bg = "#eb8a8a", width = 10,
                                           command = login.destroy)
            tombolKeluar1.place(x = 210, y = 550)
        #Menu Surat Masuk
            tab2 = ttk.Frame(tabControl)
            tabControl.add(tab2, text="Surat Masuk")
            labelSM = Tkinter.Label(tab2, text = "Daftar Surat Masuk Yang Telah Diarsipkan :", fg = "#256d80")
            labelSM.config(font=("Verdana 13 bold"))
            labelSM.place(x = 13, y = 13)
            labelInput = Tkinter.Label(tab2, text = "Nama      nomor/instansi/kegiatan/perihal/bulan/tahun")
            labelInput.config(font=("Verdana 11"))
            labelInput.place(x = 13, y = 50)
            labelInput1 = Tkinter.Label(tab2, text = "Nilatil        15/BEMF/RKB/Undangan/III/2020")
            labelInput1.config(font=("Verdana 10"))
            labelInput1.place(x = 13, y = 80)
            labelInput2 = Tkinter.Label(tab2, text = "Nilatil        30/LLMP/Dialog/Undangan/IV/2020")
            labelInput2.config(font=("Verdana 10"))
            labelInput2.place(x = 13, y = 110)
            labelInput2 = Tkinter.Label(tab2, text = "Nilatil        30/LLMP/Dialog/Undangan/IV/2020")
            labelInput2.config(font=("Verdana 10"))
            labelInput2.place(x = 13, y = 140)
            labelInputdst = Tkinter.Label(tab2, text = "....           ....")
            labelInputdst.config(font=("Verdana 10"))
            labelInputdst.place(x = 13, y = 170)
            def hide():
                kanvas = Tkinter.Canvas(tab2, height = 15, width = 350)
                kanvas.place(x = 13, y = 140)
            tombolDelete1 = Tkinter.Button(tab2, text = "x", bg = "#eb8a8a", width = 1)
            tombolDelete1.place(x = 450, y = 80)
            tombolDelete2 = Tkinter.Button(tab2, text = "x", bg = "#eb8a8a", width = 1)
            tombolDelete2.place(x = 450, y = 110)
            tombolDelete3 = Tkinter.Button(tab2, text = "x", bg = "#eb8a8a", width = 1,
                                          command = hide)
            tombolDelete3.place(x = 450, y = 140)
            #Keluar
            tombolKeluar2 = Tkinter.Button(tab2, text = "Keluar", bg = "#eb8a8a", width = 10,
                                           command = login.destroy)
            tombolKeluar2.place(x = 210, y = 550)
        #Menu Surat Keluar
            tab3 = ttk.Frame(tabControl)
            tabControl.add(tab3, text="Surat Keluar")
            labelSK = Tkinter.Label(tab3, text = "Daftar Surat Keluar Yang Telah Diarsipkan :", fg = "#256d80")
            labelSK.config(font=("Verdana 13 bold"))
            labelSK.place(x = 13, y = 13)
            labelOutput = Tkinter.Label(tab3, text = "Nama      nomor/instansi/kegiatan/perihal/bulan/tahun")
            labelOutput.config(font=("Verdana 11"))
            labelOutput.place(x = 13, y = 50)
            labelOutput1 = Tkinter.Label(tab3, text = "Nilatil        1/BEM/PKMP/Pemberitahuan/9/2019")
            labelOutput1.config(font=("Verdana 10"))
            labelOutput1.place(x = 13, y = 80)
            labelOutput2 = Tkinter.Label(tab3, text = "Nilatil        2/BEM/PKMP/Peminjaman/9/2019")
            labelOutput2.config(font=("Verdana 10"))
            labelOutput2.place(x = 13, y = 110)
            labelOutput3 = Tkinter.Label(tab3, text = "Nilatil        3/BEM/PKMP/Sertifikat/9/2019")
            labelOutput3.config(font=("Verdana 10"))
            labelOutput3.place(x = 13, y = 140)
            labelOutputdst = Tkinter.Label(tab3, text = "....           ....")
            labelOutputdst.config(font=("Verdana 10"))
            labelOutputdst.place(x = 13, y = 170)
            tombolDeleteSK1 = Tkinter.Button(tab3, text = "x", bg = "#eb8a8a", width = 1)
            tombolDeleteSK1.place(x = 450, y = 80)
            tombolDeleteSK2 = Tkinter.Button(tab3, text = "x", bg = "#eb8a8a", width = 1)
            tombolDeleteSK2.place(x = 450, y = 110)
            tombolDeleteSK3 = Tkinter.Button(tab3, text = "x", bg = "#eb8a8a", width = 1)
            tombolDeleteSK3.place(x = 450, y = 140)
            #Keluar
            tombolKeluar = Tkinter.Button(tab3, text = "Keluar", bg = "#eb8a8a", width = 10,
                                          command = login.destroy)
            tombolKeluar.place(x = 210, y = 550)
        #Menu Profile
            tab4 = ttk.Frame(tabControl)
            tabControl.add(tab4, text="Profile")
            labelAdmin = Tkinter.Label(tab4, text = "H E L L O   A D M I N", fg = "#256d80")
            labelAdmin.config(font=("Verdana 24 bold"))
            labelAdmin.place(x = 50, y = 30)
            messageAdmin = Tkinter.Message(tab4, text = '   Admin dapat mengakses daftar surat yang '
                                             'telah diarsipkan sebelumnya oleh user yang bersifat private, '
                                             'dan dapat menghapus input an user jika terjadi ketidaksengajaan '
                                             'double input, sehingga diperlukan log in menggunakan username dan '
                                             'password untuk mengamankan data.', width = 460)
            messageAdmin.config(font=("Verdana", 15))
            messageAdmin.place(x = 10, y = 100)
            tabControl.pack(expand=1, fill='both')
            #Keluar
            tombolKeluar4 = Tkinter.Button(tab4, text = "Keluar", bg = "#eb8a8a", width = 10,
                                           command = login.destroy)
            tombolKeluar4.place(x = 210, y = 550)
        else :
            tkMessageBox.showerror("Error", "Username dan Password yang anda masukkan salah!")

    def newWindow(self):
        self.jendelaBaru = Toplevel(self.jendela)
        self.app=User(self.jendelaBaru)
            
class User:
    def __init__(self,jendela):
        self.jendela = jendela
        self.jendela.wm_iconbitmap("arsipsurat.ico")
        self.jendela.title("Arsip Surat - User")
        self.jendela.geometry("500x650")

        tabControl = ttk.Notebook(jendela)
    #Menu Home
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="Home")
        #Jam
        def jam():
            waktu = time.localtime()
            tahun = waktu[0]
            bulan = waktu[1]
            tanggal = waktu[2]
            jam = waktu[3]
            menit = waktu[4]
            detik = waktu[5]
            labelJam["text"] = "%02d/%02d/%4d %02d:%02d:%02d" % \
                               (tanggal, bulan, tahun, jam, menit, detik)
        labelJam = Tkinter.Label(tab1, text = "Tanggal hari ini?")
        tombolJam = Tkinter.Button(tab1, text = "Cek Tanggal", bg = "#87cdde", width = 10,
                                   command = jam)
        labelJam.place(x = 290, y = 12)
        tombolJam.place(x = 405, y = 10)
        #Tentang Arsip Surat
        labelTentang = Tkinter.Label(tab1, text = "T E N T A N G   A R S I P   S U R A T", fg = "#256d80")
        labelTentang.config(font=("Verdana 12 bold"))
        labelTentang.place(x = 13, y = 50)
        messageTentang = Tkinter.Message(tab1, text = 'Arsip Surat merupakan aplikasi desktop '
                                         'untuk mengarsipkan surat masuk dan surat keluar yang '
                                         'ada pada sebuah instansi dengan tujuan untuk arsipan '
                                         'yang lebih rapih.', width = 460)
        messageTentang.config(font=("Verdana", 12))
        messageTentang.place(x = 10, y = 80)
        #Surat Masuk
        labelMasuk = Tkinter.Label(tab1, text = "S U R A T   M A S U K", fg = "#256d80")
        labelMasuk.config(font=("Verdana 12 bold"))
        labelMasuk.place(x = 13, y = 180)
        messageMasuk = Tkinter.Message(tab1, text = 'Surat Masuk adalah surat-surat yang diterima '
                                       'oleh suatu instansi yang berasal dari seseorang atau '
                                       'dari suatu instansi.', width = 460)
        messageMasuk.config(font=("Verdana", 12))
        messageMasuk.place(x = 10, y = 210)
        #Surat Keluar
        labelKeluar = Tkinter.Label(tab1, text = "S U R A T   K E L U A R", fg = "#256d80")
        labelKeluar.config(font=("Verdana 12 bold"))
        labelKeluar.place(x = 13, y = 300)
        messageKeluar = Tkinter.Message(tab1, text = 'Surat Keluar adalah surat-surat yang dikeluarkan/ '
                                        'dibuat oleh suatu instansi untuk dikirimkan kepada pihak  lain, '
                                        'perseorangan maupun kelompok.', width = 460)
        messageKeluar.config(font=("Verdana", 12))
        messageKeluar.place(x = 10, y = 330)
        #Keluar
        tombolKeluar1 = Tkinter.Button(tab1, text = "Keluar", bg = "#eb8a8a", width = 10,
                                       command = jendela.destroy)
        tombolKeluar1.place(x = 210, y = 550)
    #Menu Surat Masuk
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text="Surat Masuk")
        #Nama
        labelNama = Tkinter.Label(tab2, text = "Nama :")
        labelNama.config(font=("Verdana", 11))
        entryNama = Tkinter.Entry(tab2, width = 65)
        labelNama.place(x = 10, y = 10)
        entryNama.place(x = 80, y = 13)
        #Nomor Surat
        labelNomor = Tkinter.Label(tab2, text = "Nomor Surat :")
        labelNomor.config(font=("Verdana", 11))
        spinbox = Tkinter.Spinbox(tab2, from_ = 1, to = 300, increment = 1, width = 55)
        labelNomor.place(x = 10, y = 50)
        spinbox.place(x = 130, y = 53)
        #Instansi
        labelInstansi = Tkinter.Label(tab2, text = "Instansi :")
        labelInstansi.config(font=("Verdana", 11))
        entryInstansi = Tkinter.Entry(tab2, width = 63)
        labelInstansi.place(x = 10, y = 90)
        entryInstansi.place(x = 90, y = 93)
        #Kegiatan
        labelKegiatan = Tkinter.Label(tab2, text = "Kegiatan :")
        labelKegiatan.config(font=("Verdana", 11))
        entryKegiatan = Tkinter.Entry(tab2, width = 62)
        labelKegiatan.place(x = 10, y = 130)
        entryKegiatan.place(x = 95, y = 133)
        #Perihal Surat
        labelPerihal = Tkinter.Label(tab2, text = "Perihal Surat :")
        labelPerihal.config(font=("Verdana", 11))
        entryPerihal = Tkinter.Entry(tab2, width = 57)
        labelPerihal.place(x = 10, y = 170)
        entryPerihal.place(x = 127, y = 173)
        #Bulan dikeluarkannya Surat
        labelBulan = Tkinter.Label(tab2, text = "Bulan dikeluarkannya Surat :")
        labelBulan.config(font=("Verdana", 11))
        spinboxbln = Tkinter.Spinbox(tab2, from_ = 1, to = 12, increment = 1, width = 38)
        labelBulan.place(x = 10, y = 210)
        spinboxbln.place(x = 230, y = 213)
        #Tahun dikeluarkannya Surat
        labelTahun = Tkinter.Label(tab2, text = "Tahun dikeluarkannya Surat :")
        labelTahun.config(font=("Verdana", 11))
        spinboxThn = Tkinter.Spinbox(tab2, from_ = 2018, to = 2022, increment = 1, width = 37)
        labelTahun.place(x = 10, y = 250)
        spinboxThn.place(x = 235, y = 253)
        #Konfirmasi
        messageKonfirm = Tkinter.Message(tab2, text = '*Mohon pastikan kembali bahwa semua data '
                                         'telah terisi dan benar.', width = 450, fg = "red")
        messageKonfirm.config(font=("Verdana", 10))
        messageKonfirm.place(x = 10, y = 330)
        #Submit ke DATABASE
        tombolSubmit = Tkinter.Button(tab2, text = "Submit", bg = "#91e88a", width = 10,
                                      command = lambda:[dbinputSM()])
        tombolSubmit.place(x = 210, y = 450)
        def dbinputSM():
            cqlsh = "INSERT INTO surat(nomor, bulan, instansi, kegiatan, perihal, tahun) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (int(spinbox.get()), int(spinboxbln.get()), entryInstansi.get(), entryKegiatan.get(), entryPerihal.get(), int(spinboxThn.get()))
            session.execute(cqlsh,values)
            print "Surat Masuk Berhasil di Input"
        #Keluar
        tombolKeluar2 = Tkinter.Button(tab2, text = "Keluar", bg = "#eb8a8a", width = 10,
                                       command = jendela.destroy)
        tombolKeluar2.place(x = 210, y = 550)
    #Menu Surat Keluar
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text="Surat Keluar")
        #Nama
        labelNamaSK = Tkinter.Label(tab3, text = "Nama :")
        labelNamaSK.config(font=("Verdana", 11))
        entryNamaSK = Tkinter.Entry(tab3, width = 65)
        labelNamaSK.place(x = 10, y = 10)
        entryNamaSK.place(x = 80, y = 13)
        #Nomor Surat
        labelNomorSK = Tkinter.Label(tab3, text = "Nomor Surat :")
        labelNomorSK.config(font=("Verdana", 11))
        spinboxSK = Tkinter.Spinbox(tab3, from_ = 1, to = 300, increment = 1, width = 55)
        labelNomorSK.place(x = 10, y = 50)
        spinboxSK.place(x = 130, y = 53)
        #Instansi
        labelInstansiSK = Tkinter.Label(tab3, text = "Instansi :")
        labelInstansiSK.config(font=("Verdana", 11))
        entryInstansiSK = Tkinter.Entry(tab3, width = 63)
        labelInstansiSK.place(x = 10, y = 90)
        entryInstansiSK.place(x = 90, y = 93)
        #Kegiatan
        labelKegiatanSK = Tkinter.Label(tab3, text = "Kegiatan :")
        labelKegiatanSK.config(font=("Verdana", 11))
        entryKegiatanSK = Tkinter.Entry(tab3, width = 62)
        labelKegiatanSK.place(x = 10, y = 130)
        entryKegiatanSK.place(x = 95, y = 133)
        #Perihal Surat
        labelPerihalSK = Tkinter.Label(tab3, text = "Perihal Surat :")
        labelPerihalSK.config(font=("Verdana", 11))
        entryPerihalSK = Tkinter.Entry(tab3, width = 57)
        labelPerihalSK.place(x = 10, y = 170)
        entryPerihalSK.place(x = 127, y = 173)
        #Bulan dikeluarkannya Surat
        labelBulanSK = Tkinter.Label(tab3, text = "Bulan dikeluarkannya Surat :")
        labelBulanSK.config(font=("Verdana", 11))
        entryBulanSK = Tkinter.Entry(tab3, width = 40)
        labelBulanSK.place(x = 10, y = 210)
        entryBulanSK.place(x = 230, y = 213)
        #Tahun dikeluarkannya Surat
        labelTahunSK = Tkinter.Label(tab3, text = "Tahun dikeluarkannya Surat :")
        labelTahunSK.config(font=("Verdana", 11))
        spinboxThnSK = Tkinter.Spinbox(tab3, from_ = 2018, to = 2022, increment = 1, width = 38)
        labelTahunSK.place(x = 10, y = 250)
        spinboxThnSK.place(x = 235, y = 253)
        #Konfirmasi
        messageKonfirmSK = Tkinter.Message(tab3, text = '*Mohon pastikan kembali bahwa semua data '
                                           'telah terisi dan benar.', width = 450, fg = "red")
        messageKonfirmSK.config(font=("Verdana", 10))
        messageKonfirmSK.place(x = 10, y = 330)
        #Submit ke DATABASE
        tombolSubmitSK = Tkinter.Button(tab3, text = "Submit", bg = "#91e88a", width = 10,
                                      command = lambda:[dbinputSK()])
        tombolSubmitSK.place(x = 210, y = 450)
        def dbinputSK():
            cqlshSK = "INSERT INTO surat(nomor, bulan, instansi, kegiatan, perihal, tahun) VALUES (%s,%s,%s,%s,%s,%s)"
            valuesSK = (int(spinboxSK.get()), int(entryBulanSK.get()), entryInstansiSK.get(), entryKegiatanSK.get(), entryPerihalSK.get(), int(spinboxThnSK.get()))
            session.execute(cqlshSK,valuesSK)
            print "Surat Keluar Berhasil di Input"
        #Keluar
        tombolKeluar3 = Tkinter.Button(tab3, text = "Keluar", bg = "#eb8a8a", width = 10,
                                       command = jendela.destroy)
        tombolKeluar3.place(x = 210, y = 550)
    #Menu Profile
        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text="Profile")
        labelUser = Tkinter.Label(tab4, text = "H E L L O   U S E R", fg = "#256d80")
        labelUser.config(font=("Verdana 24 bold"))
        labelUser.place(x = 50, y = 30)
        messageUser = Tkinter.Message(tab4, text = '   User/pengguna hanya dapat menginput data '
                                       'surat yang ingin diarsipkan dan tidak dapat melihat daftar '
                                       'surat yang telah diarsipkan sebelumnya, sehingga tidak '
                                       'diperlukan log in menggunakan username dan password.', width = 460)
        messageUser.config(font=("Verdana", 15))
        messageUser.place(x = 10, y = 100)
        tabControl.pack(expand=1, fill='both')
        #Keluar
        tombolKeluar4 = Tkinter.Button(tab4, text = "Keluar", bg = "#eb8a8a", width = 10,
                                       command = jendela.destroy)
        tombolKeluar4.place(x = 210, y = 550)
        tabControl.pack(expand=1, fill='both')
        
if __name__ == '__main__':
    start()
