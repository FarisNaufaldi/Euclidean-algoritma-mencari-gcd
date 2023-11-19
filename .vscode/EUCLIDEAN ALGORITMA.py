def euclidean_algoritma(angkapertama,angkakeduadibelakangkoma):
    while angkapertama%angkakeduadibelakangkoma != 0:
        a = angkapertama//angkakeduadibelakangkoma
        b = a * angkakeduadibelakangkoma
        c = angkapertama - b
        angkapertama = angkakeduadibelakangkoma
        angkakeduadibelakangkoma = c
    print(c)
#Masukkan kedua bilangan dibawah sini    
euclidean_algoritma(1701,3768)
  