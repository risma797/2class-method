class Laptop:

  #static variable
  SSD = 256

  #instance variable
  def __init__(self, Nama_Merk, RAM, Tipe):
    self.Nama_Merk = Nama_Merk
    self.RAM = RAM
    self.Tipe = Tipe
    print(f'Spesifikasi Laptop sebagai berikut : {self.Nama_Merk}, {self.RAM},  {self.Tipe}' )
  
  @classmethod
  def Spesifikasi(cls):
    print(f'Laptop Dell mempunyai SSD {cls.SSD}' )


Laptop_Dell = Laptop('Dell', '8 GB', '7470')
Laptop_Dell.Spesifikasi()
Laptop.Spesifikasi()

