def kira_merit_upu():
    nilai_gred_utama = {
        'A+': 11.25, 'A': 10, 'A-': 8.75,
        'B+': 7.5, 'B': 6.25,
        'C+': 5, 'C': 3.75,
        'D': 2.5, 'E': 1.25, 'G': 0
    }
    nilai_gred_terbaik_pakej = {
        'A+': 16.88, 'A': 15.00, 'A-': 13.13,
        'B+': 11.25, 'B': 9.38,
        'C+': 7.50, 'C': 5.63,
        'D': 3.75, 'E': 1.88, 'G': 0
    }
    nilai_gred_terbaik = {
        'A+': 5.63, 'A': 5.00, 'A-': 4.38,
        'B+': 3.75, 'B': 3.13,
        'C+': 2.50, 'C': 1.88,
        'D': 1.25, 'E': 0.63, 'G': 0
    }


    print("--- KALKULATOR MERIT UPU (SPM) ---")
    print("Sila masukkan gred (Contoh: A+, A, B+)\n")

    try:
        subjek = ['BAHASA MELAYU', 'BAHASA INGGERIS', 'MATEMATIK', 'SEJARAH']
        subjek_utama = []
        for i in range(len(subjek)):
            gred = input(f"Masukkan gred {subjek[i]}: ").upper()
            subjek_utama.append(nilai_gred_utama[gred])

        subjek_terbaik_pakej = []
        for i in range(1, 3):
            gred = input(f"Masukkan gred Subjek Terbaik Pakej {i}: ").upper()
            subjek_terbaik_pakej.append(nilai_gred_terbaik_pakej[gred])

        subjek_terbaik = []
        for i in range(1, 3):
            gred = input(f"Masukkan gred Subjek Terbaik {i}: ").upper()
            subjek_terbaik.append(nilai_gred_terbaik[gred])


        markah_koko = float(input("\nMasukkan Markah Kokurikulum (0-10): "))


        skor_akademik = sum(subjek_utama) + sum(subjek_terbaik_pakej) + sum(subjek_terbaik)


        jumlah_merit = skor_akademik + markah_koko

        print("\n--- KEPUTUSAN ---")
        print(f"Skor Akademik (90%): {skor_akademik:.2f}")
        print(f"Markah Kokurikulum (10%): {markah_koko:.2f}")
        print(f"---------------------------")
        print(f"JUMLAH MERIT UPU: {jumlah_merit:.2f} %")
        print(f"---------------------------")

    except KeyError:
        print("\nERROR: Sila pastikan gred yang dimasukkan adalah betul (A+, A, A-, dsb).")
    except ValueError:
        print("\nERROR: Sila masukkan nombor yang betul untuk markah kokurikulum.")


kira_merit_upu()