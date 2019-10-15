import indah
def main():
    print("TEGANGAN")
    R = float (input ("Masukkan Resistansi: "))
    I = float (input ("masukkan Arus: "))
    Tegangan = indah.Tegangan(R, I)
    print("Resistansi\t: ", R)
    print("Arus\t: ", I)
    print("Tegangan\t : ", Tegangan)
    print("\n")
    
    print("TEKANAN")
    F = float (input ("Masukkan Gaya : "))
    A = float (input ("Masukkan Luas : "))
    Tekanan = indah.Tekanan(F, A)
    print("Gaya\t: ", F)
    print("Luas\t: ", A)
    print("Tekanan\t : ", Tekanan)
    print("\n")

    print("GAYA")
    m = float (input ("Masukkan Massa: "))
    a = float (input ("Masukkan Percepatan Gravitasi:"))
    Gaya = indah.Gaya(m,a)
    print("Massa\t: ", m)
    print("Percepatan Gravitasi: ", a)
    print("Gaya\t : ", Gaya)

if __name__ == "__main__":
    main()
