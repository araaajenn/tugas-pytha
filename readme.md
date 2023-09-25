# Program Segitiga - README

## Flowchart Program

Berikut adalah Flowchart dari program yang saya buat:

![Flowchart](https://i.ibb.co/zxBJn46/ara-drawio-1.png)

## Deskripsi Program

Program ini adalah program sederhana yang meminta pengguna untuk melakukan login dengan nama dan NIM. Jika login berhasil, pengguna akan diberi akses ke beberapa pilihan penghitungan sisi segitiga berdasarkan input yang diberikan.

## Penjelasan Output

Berikut adalah penjelasan singkat untuk setiap output yang mungkin muncul:

1. **Login Gagal**
   - Jika login gagal, program akan mencetak pesan "Login gagal maz, ulang dong".
   - Pengguna diminta untuk memasukkan kembali nama dan NIM.
   
   ![Login Gagal](https://i.ibb.co/y0QRvdC/Screenshot-9.png)

2. **Login Berhasil**
   - Jika login berhasil, program akan mencetak pesan "Berhasil Login maz!".
   - Pengguna akan diberikan opsi untuk memilih sisi segitiga yang ingin dihitung.
   
   ![Login Berhasil](https://i.ibb.co/n7wLpQn/Screenshot-10.png)

3. **Pilihan Sisi Segitiga**
   - Setelah login berhasil dan pengguna memilih pilihan (1, 2, atau 3), program akan mencetak pesan "Pilih sisi yang mau Kamu hitung :" diikuti oleh daftar opsi:
     - "1. Alas"
     - "2. Sisi Tegak"
     - "3. Sisi Miring"
   - Pengguna diminta untuk memasukkan nomor pilihan (1, 2, atau 3).
   
   ![Pilihan Sisi Segitiga](https://i.ibb.co/n7wLpQn/Screenshot-10.png)

4. **Penghitungan Sisi Segitiga**
   a. Jika pengguna memilih "1" (Alas):
      - Pengguna diminta untuk memasukkan panjang sisi tegak dan sisi miring.
      - Panjang alas segitiga akan dihitung dan dicetak.
   
      ![Penghitungan Alas](https://i.ibb.co/MnnDsRR/Screenshot-11.png)

   b. Jika pengguna memilih "2" (Sisi Tegak):
      - Pengguna diminta untuk memasukkan panjang alas dan sisi miring.
      - Panjang sisi tegak segitiga akan dihitung dan dicetak.
   
      ![Penghitungan Sisi Tegak](https://i.ibb.co/0yJwpdz/Screenshot-12.png)

   c. Jika pengguna memilih "3" (Sisi Miring):
      - Pengguna diminta untuk memasukkan panjang alas dan sisi tegak.
      - Panjang sisi miring segitiga akan dihitung dan dicetak.
   
      ![Penghitungan Sisi Miring](https://i.ibb.co/GtSqnfn/Screenshot-13.png)

5. **Pilihan Tidak Valid**
   - Jika pengguna memasukkan nomor pilihan yang tidak valid (bukan 1, 2, atau 3), program akan mencetak pesan "Cuma boleh isi 1, 2, atau 3. Sisanya tidak Valid maz".
   
   ![Pilihan Tidak Valid](https://i.ibb.co/cwVG7sn/Screenshot-15.png)

## Catatan

Program ini akan terus berjalan sampai pengguna berhasil login atau memilih keluar, dan akan kembali ke langkah awal setelah setiap percobaan login yang gagal.
