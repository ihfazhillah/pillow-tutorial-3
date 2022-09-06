# pillow-tutorial-3

Source code dari video

<div align="center">
  <a href="https://www.youtube.com/watch?v=xVbLv4uaIr8"><img src="https://img.youtube.com/vi/xVbLv4uaIr8/0.jpg" alt="IMAGE ALT TEXT"></a>
</div>

d

Video ini masih berkaitan dengan 2 video sebelumnya:

- https://youtu.be/Uo2U4dLy0S4
- https://youtu.be/x5_wbrT_VKI

Nah, kali ini kita akan gabungkan beberapa kata yang awalnya dalam satu bounding box untuk setiap kata, menjadi seperti kriteria berikut:
- bila kata ada di special words, maka kita gabungkan
- bila tidak, maka kita keep bounding box nya untuk tiap kata tersebut.

Ya, kita menggunakan bahasa python untuk solve problem kita. Saya menggunakan python 3.9 di video ini.

Lebih dari itu, kita berkenalan dengan beberapa hal:

- regex di python secara ringkas, contoh regex, dan untuk apa biasanya regex digunakan. Kamu akan menemukan “aha” untuk regex.
- kita juga belajar bagaimana mengurutkan data menggunakan sorted, dan grouping data setelah di sort menggunakan itertools.groupby . Module default dari python
- di akhir, kita juga belajar bagaimana bikin highlight menggunakan python pillow. tool yang kita gunakan untuk manipulasi gambar. Apa triknya supaya tidak jadi seperti “difference” kalau diistilah graphic (paling tidak inkscape yah)

Video ini kita pelajari step by step dari masalah, input, step sampai output.

Links:

- regex101.com
- https://github.com/ihfazhillah/pillow-tutorial-3
- https://youtu.be/Uo2U4dLy0S4
- https://youtu.be/x5_wbrT_VKI

Daftar Isi:
00:00 Intro
01:00 Repository sumber kode
01:33 Definisi yang lebih spesifik
03:24 Alur penyelesaian masalah dari saya
04:30 Alur 1 lebih detail: pecah text
05:20 Alur 2 lebih detail: Transformasi
05:38 Alur 3 lebih detail: Gabung satu baris
06:43 Hasil gambar yang kita inginkan
07:24 Coding alur 1: Pecah text
07:28 Pengenalan ringkas regex
14:27 Coding alur 2: Transform value
15:07 Coding alur terakhir: Merge Line
16:35 Bagaimana menampilkan outlined box
16:55 Bagaimana menampilkan filled box
18:06 Bagaimana highlight hanya kata kata terpilih saja
18:50 Bagaimana caranya menyelesaikan masalah
