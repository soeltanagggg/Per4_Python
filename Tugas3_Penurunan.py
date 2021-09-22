class Olahraga():
    def __init__(self, nama, nomorpunggung, negara):
        self.nama = nama
        self.nomor = nomorpunggung
        self.negara = negara

    def cek_identitas_pemain(self):
        print('nama:', self.nama,'\nNomor Punggung:', self.nomor,'\nAsal Negara:', self.negara)

    

class Sepakbola(Olahraga):
    def __init__(self, nama, nomorpunggung, negara, posisi, ):
        super().__init__(nama, nomorpunggung, negara)
        self.posisi = posisi

class Club(Sepakbola):
    def __init__(self, nama, nomorpunggung, negara, posisi, gaji, kontrak, club):
        super().__init__(nama, nomorpunggung, negara, posisi, )
        self.gaji=gaji
        self.durasi_kontrak=kontrak
        self.nama_club=club

    def identitasbola(self):
        print('Nama Pemain      :',self.nama)
        print('Nomor Punggung   :',self.nomor)
        print('Negara Asal      :',self.negara)
        print('Posisi Bermain   :',self.posisi)
        print('Durasi Kontrak   :',self.durasi_kontrak)
        print('Gaji Pemain      :',self.gaji)
        print('Club sekarang    :',self.nama_club)

class Bulutangkis(Olahraga):
    def __init__(self, nama, nomorpunggung, negara, tipe_game):
        super().__init__(nama, nomorpunggung, negara)
        self.gaya_bermain = tipe_game
    
    def identitasbultang(self):
        print('Nama Pemain      :',self.nama)
        print('Nomor Punggung   :',self.nomor)
        print('Negara Asal      :',self.negara)
        print('Gaya Bermain     :',self.gaya_bermain)

class Basket(Olahraga):
    def __init__(self, nama, nomorpunggung, negara, tinggi):
        super().__init__(nama, nomorpunggung, negara)
        self.tinggi=tinggi
        

class Tim(Basket):
    def __init__(self, nama, nomorpunggung, negara, tinggi, club, gaji, kontrak):
        super().__init__(nama, nomorpunggung, negara, tinggi)
        self.nama_club=club
        self.gaji=gaji
        self.durasi_kontrak=kontrak
        self.nama_club=club

    def identitasbasket(self):
        print('Nama Pemain      :',self.nama)
        print('Nomor Punggung   :',self.nomor)
        print('Negara Asal      :',self.negara)
        print('Tinggi Pemain    :',self.tinggi)
        print('Durasi Kontrak   :',self.durasi_kontrak)
        print('Gaji Pemain      :',self.gaji)

atlet1=Club('Robaldo',7,'Portugal','LW/ST','5 Tahun','69 Pounds','Manchaster United')
atlet2=Bulutangkis('Kevin Sanjaya',14,'Indonesia','Ganda Putra')
atlet3=Tim('Lebron James',20,'America','200','Lakers','1,6 Billons','5 Tahun')

print("ATLET TERKENAL")
print("==============")
atlet1.cek_identitas_pemain()
print('')
atlet2.cek_identitas_pemain()
print('')
atlet3.cek_identitas_pemain()
print('')
print('DETAIL PEMAIN')
print("=============")
atlet1.identitasbola()
print('')
atlet2.identitasbultang()
print('')
atlet3.identitasbasket()





