import streamlit as st 
import numpy as np 
import statistics
import pandas as pd 
import plotly.express as px
import base64

# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

#################
st.set_page_config(
    page_icon="📊",
    page_title="Project Mengajar", 
    layout = "wide"
)
st.title("Simulasi Statistika Ekonomi UTS")
tab1, tab2, tab3, tab4 = st.tabs(["Descriptive Analytics 1", "Descriptive Analytics 2", "Price Index📇", "Probability 🤔"])
with tab1: 
    st.header("INTRODUCTION")
    st.subheader("Apa itu Statistika")
    st.markdown("Ilmu mengumpulkan, menata, menyajikan, menganalisis, dan menginterprestasikan data menjadi informasi untuk membantu pengambilan keputusan yang efektif (Lind).")
    st.subheader("Cabang Statistika")
    st.markdown("""
    - Descriptive : mendeskripsikan aspek penting dari dataset 
    - Inferential : mengambil suatu kesimpulan / estimasi / membuat prediksi suatu populasi dari sample yang dimiliki. 
    
    Notes:
    \n
    \t- Sample : Suatu bagian populasi tertentu yang menjadi perhatian. 
    \t- Populasi : Sebuah kumpulan dari semua kemungkinan orang-orang, benda-benda, dan ukuran lain dari objek. 
    \n
""")
    st.subheader("Jenis Data")
    st.markdown("""![jenis data](https://cdn1.byjus.com/wp-content/uploads/2021/12/Types-of-Data-in-Statistics.png)
    
    - Data Kualitatif : Nama, Jenis Kelamin, Kelas, Tingkat Kesetujuan, Nilai Matkul, ranking
                - Nominal (Angka yang diberikan hanya sebagai label saja): Nama, Jenis Kelamin
                - Ordinal (Angka mengandung pengertian tingkatan): Kelas, Tingkat Kesetujuan, Nilai Matkul, ranking
    - Data Kuantitatif : 
                - Diskrit : Integer, dihitung, istilahnya angka bulat (0, 1, 2, 3, -1). Contoh : Siswa yang ikut les
                - Continuous : Float, diukur, nggak ada batasan berapa (sehingga hanya dapat dihitung dalam interval). Contoh : panjang meja, suhu saat ini. Apakah bisa dihitung berapa banyak panjang meja 4 m ? tidak ada, karena pasti ada 4.0001, 4.0004. 
    """)
    st.markdown("""![Skala Pengukuran](https://omdik21.files.wordpress.com/2017/03/capture.png)
                [read more](https://perbedaan.net/perbedaan-skala-nominal-ordinal-interval-dan-rasio/)""")
    
    st.header("DESCRIPTIVE ANALYTICS 1")
    st.header("Central Tendensies & Dispersion")
    st.subheader("Ukuran Tengah")
    st.markdown("**Mean**")
    st.write("Rerata adalah jumlah nilai dibagi banyak data. (aritmatic mean)")
    st.latex(r"""\bar{x} = \frac{\sum{x_i}}{n}""")
    st.write("Geometric Mean")
    st.write("Geometric Mean adalah nilai rata-rata yang diperoleh dengan mengalikan semua data dalam suatu kelompok sampel.")
    st.latex(r'''GM = \left( \prod_{i=1}^{n} x_i \right)^{\frac{1}{n}} = \sqrt[n]{x_1 \cdot x_2 \cdot \dots \cdot x_n}''')
    st.markdown("**Median**")
    st.write("Median adalah “elemen tengah” ketika data disusun dalam urutan menaik/ascending (kecil ke besar).")
    st.markdown("""Tips: \n
    - Susunlah data dari yang terkecil ke yang terbesar. 
    - Tentukan angka di bagian tengah yang tepat.
                - Jika jumlah titik data ganjil, median akan menjadi angka di tengah-tengah absolut.
                - Jika jumlah titik data genap, median adalah rata-rata dari dua titik data tengah, yang berarti kedua nilai tengah harus dijumlahkan dan dibagi 2.
    """)
    st.markdown("**Modus**")
    st.write("Modus adalah pengukuran yang paling sering muncul dalam kumpulan data. Mungkin terdapat satu mode; beberapa mode, jika lebih dari satu angka yang paling sering muncul; atau tidak ada mode sama sekali, jika setiap angka hanya muncul satu kali.")
    st.markdown("""Tips: \n
    - Letakkan data secara berurutan dari yang terkecil hingga terbesar, seperti yang Anda lakukan untuk menemukan median.
    - Cari nilai apa pun yang muncul lebih dari satu kali.
    - Tentukan nilai mana dari Langkah 2 yang paling sering muncul
    """)
    st.subheader("Dispersion")
    st.markdown("""adalah bagaimana data tersebar, menggambarkan variabilitas data set. Ingatlah ukuran dispersi diantaranya:\n- Range (fokus pada nilai ekstrim). Formulanya : Maximum Value - Minimum Value
\n- MAD (Mean Absolute Deviation). Gimana data tersebar dari mean nya (nah dispersinya di absolute kan). 
\n- Variance. rata-rata deviasi kuadrat dari rata-rata aritmatika.
\n- Standar Devuasi. akar dari variance. 
\n- Coefficient of Variance. Koefisien Variasi (CV) menyesuaikan deviasi dalam besaran rata-rata.""")
    st.write("Formula: ")
    st.latex(r'''MAD = \frac{1}{n} \sum_{i=1}^{n} \left| x_i - \bar{x} \right|''')
    st.markdown(r'''Untuk selanjutnya, ingatlah bahwa \bar{x} adalah rerata sample, μ adalah rerata populasi, s adalah standar deviasi sample, dan σ adalah standar deviasi populasi. ''')
    col1, col2 = st.columns(2)
    with col1: 
        st.write("Population")
        st.latex(r'''\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2''')
        st.latex(r'''\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}''')
        st.latex(r'''CV = \frac{\sigma}{\mu} \times 100\%''')
    with col2: 
        st.write("Sample")
        st.latex(r'''s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2''')
        st.latex(r'''s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}''')
        st.latex(r'''CV = \frac{s}{\bar{x}} \times 100\%''')
    st.write("Semakin kecil dispersi semakin baik datanya, karena semakin seragam. Hal itu membaut ukuran pusat data lebih bisa dipercaya.")
    st.write("****")
    st.subheader("Latihan Ukuran Tengah & Dispersi: ")
    st.markdown("""carilah \n
a. rerata aritmatik, \n
b. modus, \n
c. median, \n
d. MAD, \n
e. Standar Deviasi Populasi,\n
f. coefficient of variance, \n
dengan diketahui data 17, 10, 9, 14, 13, 17, 12, 20, 14""")
    # a
    u_so = st.number_input(label="Rerata Aritmatik")
    rerata = np.mean([17, 10, 9, 14, 13, 17, 12, 20, 14])
    if u_so:
        if u_so == rerata:
            st.write("Jawaban Anda Benar !", rerata)
        else: 
            st.write("Belum Tepat")
    # b
    u_so = st.number_input(label="Modus")
    s_so = statistics.mode([17, 10, 9, 14, 13, 17, 12, 20, 14])
    if u_so:
        if u_so == s_so:
            st.write("Jawaban Anda Benar !", s_so)
        else: 
            st.write("Belum Tepat")
    # c
    u_so = st.number_input(label="Median")
    s_so = statistics.median([17, 10, 9, 14, 13, 17, 12, 20, 14])
    if u_so:
        if u_so == s_so:
            st.write("Jawaban Anda Benar !", s_so)
        else: 
            st.write("Belum Tepat")
    # d
    u_so = st.number_input(label="MAD (Mean Absolute Deviation)")
    def mad(arrays, rerata): 
        jumlah = 0
        for i in arrays: 
            jumlah += np.abs(i - rerata)
        return jumlah / len(arrays)

    s_so = mad([17, 10, 9, 14, 13, 17, 12, 20, 14], rerata)
    if u_so:
        if np.round(u_so, 1) == np.round(s_so, 1):
            st.write("Jawaban Anda Benar !", s_so)
        else: 
            st.write("Belum Tepat")
    # e
    u_so = st.number_input(label="Standar Deviasi Populasi")
    def std_dev(arrays, rerata): 
        jumlah = 0
        for i in arrays:
            jumlah += (i-rerata)**2
        return np.sqrt(jumlah/len(arrays))
    sigma = std_dev([17, 10, 9, 14, 13, 17, 12, 20, 14], rerata)
    if u_so:
        if np.round(u_so, 1) == np.round(sigma, 1):
            st.write("Jawaban Anda Benar !", sigma)
        else: 
            st.write("Belum Tepat")
    # f 
    u_so = st.number_input(label="Coefficient of Variance Population, dalam satuan ya (bukan %)")
    s_so = sigma/rerata
    # st.write(s_so)
    if u_so:
        if np.round(u_so, 1) == np.round(s_so, 1):
            st.write("Jawaban Anda Benar !", s_so)
        else: 
            st.write("Belum Tepat")

    st.header("Data Tabular dan Metode Grafik")
    st.subheader("Summarize Qualitative Data")
    st.write("""Untuk melakukan pengorganisasian data kualitatif disini akan dibuat 2 distribusi.\n
    1. Distribusi Frekuensi : Distribusi frekuensi untuk data kualitatif mengelompokkan data ke dalam dan mencatat berapa banyak pengamatan yang masuk ke dalam setiap kategori.\n
    2. Frekuensi Relatif: proporsi dalam setiap kategori. Untuk menemukan frekuensi relatif adalah dengan membagi frekuensi setiap kelompok dengan ukuran sampel.""")
    st.write("Contoh Data: ")
    st.markdown("![cuaca](https://github.com/user-attachments/assets/f8e5623a-91d1-4c16-900e-324ba9289eb9)")
    cuaca = ["rainy", "rainy", "sunny", "sunny", 
            "rainy", "rainy", "rainy", "sunny", 
            "rainy", "cloudy", "rainy", "rainy", 
            "rainy", "rainy",  "sunny","rainy",
            "rainy", "rainy", "sunny", "rainy", 
            "rainy", "rainy", "sunny", "rainy", 
            "rainy", "rainy", "sunny", "rainy"]
    st.write("Solusi")
    cuaca_df = pd.DataFrame(cuaca, columns=["cuaca"]).value_counts().reset_index()
    cuaca_df = cuaca_df.rename({0: 'frequency'}, axis=1)
    jumlah_data = sum(cuaca_df['frequency'])
    cuaca_df['relative'] = cuaca_df['frequency']/jumlah_data
    st.table(cuaca_df)

    st.subheader("Visualisasi")
    st.write("Untuk data qualitatif, dapat dilakukan 2 visualisasi yang umum dilakukan. Yaitu Pie Chart dan Bar Chart")
    col1, col2 = st.columns(2)
    with col1: 
        st.write("Pie Chart")
        st.write("adalah lingkaran tersegmentasi yang segmen-segmennya menggambarkan frekuensi relatif (proporsi/pecahan) dari kategori-kategori beberapa variabel kualitatif")
        fig = px.pie(cuaca_df, values='relative', names='cuaca', color='cuaca', 
                    title=f'Pie Chart Cuaca')    
        fig.update_traces(textfont=dict(color="black"))
        st.plotly_chart(fig, theme="streamlit")

    with col2: 
        st.write("Bar Chart")
        st.write("menggambarkan frekuensi atau frekuensi relatif untuk setiap kategori data kualitatif sebagai batang yang naik secara vertikal dari sumbu horizontal.")
        fig = px.bar(cuaca_df, y='frequency', x='cuaca', color='cuaca', 
                    title=f'Bar Chart Sebaran Banyak Tipe Cuaca')    
        fig.update_traces(textfont=dict(color="black"))
        st.plotly_chart(fig, theme="streamlit")

    st.subheader("Summarize Quantitative Data")
    st.write("**Penentual Width Class**")
    st.latex(r'''\text{Width of Class} = \frac{\text{Range}}{\text{Number of Classes}} = \frac{\text{Max Value} - \text{Min Value}}{k}''')
    st.write("**Visualizing Quantitative Data**")
    st.write("Untuk data quanitatif, banyak sekali visualisasi yang dapat dilakukan. Dalam analisis univariate, disini akan diberikan contoh tiga visualisasinya yaitu Histogram, Polygon, dan Ogive.")
    st.write("Contoh Data: skor nilai kuis statek kelas B : 45, 46, 56, 51, 57, 65, 67, 68, 69, 76, 78, 71, 83, 89")
    st.write("Solusi")
    st.write("Jika lebar / width kelas adalah 10 maka dapat digambarkan sebagai berikut")
    data_kuis = [45, 46, 56, 51, 57, 65, 67, 68, 69, 76, 78, 71, 83, 89]
    data_kuis_range = {"40-50": 0, "50-60": 0, "60-70": 0, "70-80": 0, "80-90": 0}
    for i in data_kuis: 
        if i // 10 == 4: 
            data_kuis_range["40-50"] += 1
        elif i // 10 == 5: 
            data_kuis_range["50-60"] += 1
        elif i // 10 == 6: 
            data_kuis_range["60-70"] += 1
        elif i // 10 == 7: 
            data_kuis_range["70-80"] += 1
        elif i // 10 == 8: 
            data_kuis_range["80-90"] += 1
    data_kuis_df = pd.DataFrame(list(data_kuis_range.items()), columns=['kelas', 'frequency'])
    data_kuis_df['relative'] = data_kuis_df['frequency']/sum(data_kuis_df['frequency'])
    data_kuis_df['cumulative'] = data_kuis_df['relative'].cumsum()
    data_kuis_df['min_point'] = [45, 55, 65, 76, 85]
    data_kuis_df['upper_limit'] = [50, 60, 70, 80, 90]
    st.table(data_kuis_df)

    col1, col2 = st.columns(2)
    with col1: 
        st.write("**Histogram**")
        st.write("serangkaian persegi panjang di mana lebar dan tinggi setiap persegi panjang mewakili lebar kelas dan frekuensi (atau frekuensi relatif) dari masing-masing kelas.")
        fig = px.histogram(x=data_kuis, title="Sebaran Data berdasar Frequency")    
        fig.update_traces(textfont=dict(color="black"))
        st.plotly_chart(fig, theme="streamlit")

    with col2: 
        st.write("**Polygon**")
        st.write("menghubungkan serangkaian titik yang bertetangga di mana setiap titik mewakili titik tengah dari kelas tertentu dan frekuensi yang terkait atau frekuensi relatif.")
        fig = px.line(data_kuis_df, y='relative', x='min_point', 
                    title=f'Polygon relative frequency')    
        fig.update_traces(textfont=dict(color="black"))
        st.plotly_chart(fig, theme="streamlit")

    col1, col2 = st.columns(2)
    with col1: 
        st.write("**Ogive**")
        st.write("grafik yang memplot frekuensi kumulatif atau frekuensi relatif kumulatif setiap kelas terhadap batas atas kelas yang sesuai.")
        fig = px.line(data_kuis_df, y='cumulative', x='upper_limit', 
                    title=f'Ogive relative frequency')    
        fig.update_traces(textfont=dict(color="black"))
        st.plotly_chart(fig, theme="streamlit")
    
# REFERENSI 
# https://intranet.missouriwestern.edu/cas/wp-content/uploads/sites/17/2020/05/Measures-of-Central-Tendency-2014.pdf
# ASISTENSI HOSEA

with tab2: 
    st.header("DISPLAYING AND EXPLORING DATA")
    st.subheader("Dot Plot")
    c1, c2 = st.columns((2, 1))
    with c1:
        st.markdown("""
        - Metode ini mengelompokkan data sesedikit mungkin sehingga kita tidak kehilangan identitas pengamatan individu.
        - Hal ini memungkinkan kita untuk melihat bentuk distribusi, nilai yang cenderung mengelompok, dan pengamatan terbesar dan terkecil.
        - Lebih berguna untuk set data yang lebih kecil. Sebaliknya,
        gunakan histogram untuk set data yang besar.\n""")
    with c2: 
        st.markdown("""![Dot Plot](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfXJsaXIo_F_e4BzMFHnMergQVjZikcTCOBQ&s)""")

    st.subheader("Steam and Leaf")
    st.write("Batang dan daun, daun adalah satuan sedangkan batang adalah sisa angka selain satuan. Ini menggambarkan gimana datanya tersebar.")
    st.markdown("""![Steam Leaf](https://www.wikihow.com/images/thumb/9/9f/Read-a-Stem-and-Leaf-Plot-Step-1.jpg/v4-460px-Read-a-Stem-and-Leaf-Plot-Step-1.jpg.webp)""")

    st.subheader("Sebelum ke Boxplot -> Spread by Location")
    st.write("Yang paling sering digunakan untuk menggambarkan dispersi data adalah standar deviasi. Tapi akan diperkenalkan Cara alternatif untuk menggambarkan penyebaran data termasuk menentukan lokasi nilai yang membagi sekumpulan pengamatan menjadi beberapa bagian yang sama.")
    st.write("**Quartile-Percentile-Desil**")
    st.markdown("""
- Quartile : membagi data yang terurut menjadi empat bagian yang sama besar. Terdapat tiga quartile utama: Q1, Q2, Q3
- Percentile : membagi data yang terurut menjadi 100 bagian yang sama besar. Percentile menunjukkan posisi data dalam distribusi relatif terhadap 100 bagian. Persentil tertentu menunjukkan persentase data yang berada di bawah nilai tersebut.
- Decile : membagi data yang terurut menjadi 10 bagian yang sama besar. Decile menunjukkan posisi data dalam distribusi relatif terhadap 10 bagian.
    \nNotes:\n
                untuk selanjutnya akan berfokus pada persentile karena yang dapat menggambarkan quartile maupun decile. Misal decile 1 = percentile 10, quartile 1 = percentile 25.
                """)
    st.write("**Step 1**: Urutkan Data dalam urutan menaik (ascending)")
    st.write("**Step 2**: Cari lokasi data pth dengan formula berikut:")
    st.latex(r"L_p = \frac{p}{100} \times (n + 1)")
    st.write("n adalah banyaknya observasi, dan p adalah persentil yang dicari. ")
    st.markdown("""Note: 
- Jika Lp integer, maka pengamatan Lpth dalam set data yang diurutkan adalah persentil ke-p.
- Jika tidak, kemudian melakukan interpolasi antara dua pengamatan yang sesuai untuk memperkirakan persentil ke-p. Interpolasi dilakukan dengan integer + fraksi_sisa*selisih data""")
    st.subheader("Box Plot")
    st.markdown("""
- (box-and-whisker plot) adalah cara untuk menampilkan nilai terkecil (S), kuartil (Q1, Q2, dan Q3), dan nilai terbesar (L).
- Outlier nanti akan kelihatan di Box Plot. Adapun Outlier itu adalah data yang jauh dari pusat data. Definisinya adalah data: 
""")
    st.latex(r'x_i < Q_1 - 1.5 \times \text{IQR}')  # Lower Bound
    st.latex(r'x_i > Q_3 + 1.5 \times \text{IQR}')  # Upper Bound
    st.write('IQR = Q3- Q1')
    st.markdown("""
- Boxplotnya nanti misal tidak ada outlier, batas atas dan bawah adalah max dan min data
- Jika ada outlier, batas atas dan bawar adalah batas toleransi outlier. 
""")
    data_kuis = [0, 45, 46, 56, 51, 57, 65, 67, 68, 69, 76, 78, 71, 83, 89]
    fig = px.box(data_kuis)
    st.plotly_chart(fig, theme="streamlit")
    st.write("Contoh Data: skor nilai kuis statek kelas B : 0, 45, 46, 56, 51, 57, 65, 67, 68, 69, 76, 78, 71, 83, 89")

    st.subheader("Sebelum ke Scatterplot -> Contingency Tables")
    st.markdown("""
- Tabel kontingensi adalah tabel yang digunakan untuk mengklasifikasikan pengamatan menurut dua karakteristik yang dapat diidentifikasi.
- Untuk menggunakan tabel kontingensi secara efektif, kedua variabel harus dalam skala Nominal atau Ordinal. """)
    st.markdown("""![contingency table](https://i0.wp.com/statisticsbyjim.com/wp-content/uploads/2021/02/contingency_table_marginal_probabilities.png)""")
    
    st.subheader("Scatterplots")
    st.write("ini adalah alat bantu grafis untuk menentukan apakah dua variabel berhubungan dengan cara yang sistematis atau tidak.")
    st.write("Contoh Data: skor nilai kuis statek kelas B : 0, 45, 46, 56, 51, 57, 65, 67, 68, 69, 76, 78, 71, 83, 89. Dengan diketahui umur setiap anak kelas B berturut-turut: 12, 14, 15, 16, 17, 17, 18, 17, 18, 19, 22, 21, 21, 20, 24")
    data_umur = [12, 14, 15, 16, 17, 17, 18, 17, 18, 19, 22, 21, 21, 20, 24]
    fig = px.scatter(x=data_umur, y=data_kuis, title="Hubungan Umur dengan nilai kuis")
    fig.update_layout(xaxis_title='Umur', yaxis_title='Nilai Kuis')
    st.plotly_chart(fig, theme="streamlit")
    st.write("Gimana Ngitung Kekuatan Hubungannya ?")
    st.write("**Covariance**")
    st.write("Covariance adalah ukuran statistik yang menunjukkan hubungan linear 2 variabel tapi tidak untuk ukur kekutan. ")
    st.latex(r'\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})')
    st.write("**Correlation**")
    st.write("Mengukur arah & kekuatan hubungan linear antar 2 variabel")
    st.latex(r'''r = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{\frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sigma_X \sigma_Y}''')
    st.markdown("adapun klasifikasi hubungan dari besaran korelasi dapat ditampilkan sebagai berikut: ![klasifikasi korelasi](https://elearningmath27.wordpress.com/wp-content/uploads/2014/05/koef-korelasi.jpg?w=391)")
    st.write("**Karl Pearson Skewness**")
    st.write("Koefisien skewness mengukur asimetri distribusi data.")
    st.latex(r'\text{Skewness} = \frac{3(\bar{X} - \text{Median})}{\sigma}')
    st.markdown("""![skewness](https://github.com/user-attachments/assets/01b687be-67c6-4b25-8e02-41092ea43e6d)""")
    st.subheader("Coba Hitunglah masing-masing kovarian, korelasi, dan skewness antara umur dan nilai kuis !")
    st.caption("Ingatlah untuk menggunakan sample daripada populasi")
    def covariance(a_x, a_y): 
        jumlah = 0
        mean_x, mean_y = np.mean(a_x), np.mean(a_y)
        for i in range(0, 15): 
            jumlah += (a_x[i] - mean_x) * (a_y[i] - mean_y)
        return jumlah/(len(a_x)-1)
    cov_xy = covariance(data_umur, data_kuis)

    def std_dev_sample(arrays): 
        rerata = np.mean(arrays)
        jumlah = 0
        for i in arrays:
            jumlah += (i-rerata)**2
        return np.sqrt(jumlah/(len(arrays)-1))
    
    std_x = std_dev_sample(data_umur)
    std_y = std_dev_sample(data_kuis)
    def correlation(cov_xy, std_x, std_y): 
        return cov_xy/(std_x*std_y)
    cor_xy = correlation(cov_xy, std_x, std_y)

    # coefficient skewness
    def skew(array_a): 
        rerata = np.mean(array_a)
        median = np.median(array_a)
        stdev = std_dev_sample(array_a)
        return 3*(rerata-median)/stdev
    
    skew_umur = skew(data_umur)
    skew_kuis = skew(data_kuis)
    c1, c2, c3, c4 = st.columns(4)
    with c1: 
        u1 = st.number_input(label="Covariance Umur-Kuis")
        if u1:
            if np.round(u1, 1) == np.round(cov_xy, 1):
                 st.write("Jawaban Anda Benar !", cov_xy)
            else:
                st.write("Belum benar, coba lagi")
    with c2: 
        u2 = st.number_input(label="Correlation Umur-Kuis")
        if u2:
            if np.round(u2, 1) == np.round(cor_xy, 1):
                 st.write("Jawaban Anda Benar !", cor_xy)
            else:
                st.write("Belum benar, coba lagi")
    with c3: 
        u3= st.number_input(label="Koefisien Skewness Umur")
        if u3:
            if np.round(u3, 1) == np.round(skew_umur, 1):
                 st.write("Jawaban Anda Benar !", skew_umur)
            else:
                st.write("Belum benar, coba lagi")
    with c4: 
        u4 = st.number_input(label="Koefisien Skewness kuis") 
        if u4:
            if np.round(u4, 1) == np.round(skew_kuis, 1):
                 st.write("Jawaban Anda Benar !", skew_kuis)   
            else:
                st.write("Belum benar, coba lagi")
    st.header('Soal UTS')
    st.subheader("2021")
    st.markdown("![1_2021](https://github.com/user-attachments/assets/32b11b51-c477-4f87-960e-6360c90d17b8)")
    tinggi_badan = [147, 148, 148, 149, 152, 154, 154, 154, 155, 155, 
                    156, 157, 157, 159, 161, 162, 163, 164, 165, 166, 
                    167, 168, 170, 171, 171, 174, 175, 175, 180, 180, 
                    188]
    if st.button("Solution"):
        st.write("**Solution: **")
        st.markdown("a. ![solusi_a](https://github.com/user-attachments/assets/d0b8e1b7-72ec-4183-8864-bde97b247621)")
        tinggi_badan_16 = []
        for i in tinggi_badan: 
            if i // 10 == 16: 
                tinggi_badan_16.append(i)

        def skew_pop(array_a, stdev): 
            rerata = np.mean(array_a)
            median = np.median(array_a)
            return 3*(rerata-median)/stdev

        st.markdown(f"""b. Mean: {np.mean(tinggi_badan_16)},
                    Median: {np.median(tinggi_badan_16)}, 
                    Mode: {statistics.mode(tinggi_badan_16)}.  
                    """)
        st.markdown("c. ")
        fig = px.box(tinggi_badan)
        st.plotly_chart(fig, theme="streamlit")
        st.markdown(f"""e. \n
    Mean: {np.mean(tinggi_badan)}, \n
    Median: {np.median(tinggi_badan)}, \n
    sigma: {std_dev(tinggi_badan, np.mean(tinggi_badan))}, \n
    Skewness = 3*(mean - median)/stdev = {skew_pop(tinggi_badan, std_dev(tinggi_badan, np.mean(tinggi_badan)))}\n 
    Dengan demikian distribusinya adalah positive skew""")


    st.caption("Credits : Asistensi Hosea")
with tab3: 
    ppt_url = "https://docs.google.com/presentation/d/1UWww6ieEJ4yhHfkeh7B8EyTaYAUonw6l"
    st.header("Price Index")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(ppt_url, "**Price Index (1 page)**"), unsafe_allow_html=True)
    show_pdf("price_index_hosea.pdf")
    with open("price_index_hosea.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Materials (1 page)",
            data=file,
            file_name="price_index_hosea.pdf",
            mime="application/pdf"
        )
    st.header("Soal UTS")
    st.subheader("2021")
    st.markdown("![uts_2 2021](https://github.com/user-attachments/assets/537aecb0-efac-4fab-a8bd-721c15b1c369)")
    st.caption("Credits : Asistensi Hosea")
    if st.button("Solution 2"):
        st.write("a. ")
        a_2015 = 1.08*116
        a_2016 = 1.09*a_2015
        c_2017 = (140-a_2016)/a_2016
        c_2018 = (148-140)/140
        c_2019 = (10)/148
        tabel_lkp = {'tahun' : [2014, 2015, 2016, 2017, 2018, 2019], 
                    'IHK-2012(100)': [116, a_2015, a_2016, 140, 148, 158], 
                    'Gaji (Rp juta)': [6, 6.3, 6.5, 6.9, 7.1, 7.4], 
                    'Inflasi%': [7, 8, 9, round(c_2017*100, 2), round(c_2018*100, 2), round(c_2019*100, 2)]}
        tabel_lengkap_df = pd.DataFrame.from_dict(tabel_lkp)
        st.table(tabel_lengkap_df)
        
        def geo_mean(iterable):
            a = np.array(iterable)
            return a.prod()**(1.0/len(a))
        st.write(f"b. {round(geo_mean(tabel_lengkap_df['Inflasi%']/100)*100, 2)}%")
        st.markdown("![2_b](https://github.com/user-attachments/assets/1f761f36-7428-4b52-b2b1-fb05ed448bec)")
        st.markdown("c. Gaji_i * IHK_2017 / IHK_i -> gaji berdasarkan harga 2017 dengan tetap merefleksikan harga tahun i")
        tabel_lengkap_df['gaji_rill_2017'] = tabel_lengkap_df['Gaji (Rp juta)']*(140/tabel_lengkap_df['IHK-2012(100)'])
        st.table(tabel_lengkap_df)
        st.write(f"d. Indeks 2018 = 100")
        st.write("Dilakukan dengan IHK_i / IHK_2018 * 100")
        tabel_lengkap_df['IHK-2018(100)'] = tabel_lengkap_df["IHK-2012(100)"]/148*100
        st.table(tabel_lengkap_df)

with tab4: 
    st.header("Probabilitas")
    st.markdown("""
- Angka dengan kisaran 0-1 yang menunjukkan kemungkinan sesuatu terjadi. 
- Angka tersebut didapat dari suatu **experiment** dimana semua kemungkinannya ada di **sample space**. 
- Adapun subset dari experiment itu dinamakan **event**. 
- Peristiwa yang saling eksklusif (mutually exclusive) adalah peristiwa dalam probabilitas sedemikian rupa sehingga dua peristiwa dapat terjadi pada saat yang sama. Di sisi lain, kejadian lengkap (mutually exhautive) adalah sekumpulan kejadian dalam ruang sampel sedemikian rupa sehingga salah satu dari kejadian tersebut wajib terjadi saat melakukan percobaan.
""")
    st.markdown("![events](https://ars.els-cdn.com/content/image/1-s2.0-S1568494617302375-gr2.jpg)")
    st.write('Oleh karena itu, suatu kejadian yang mutually exclusive juga mutually exhautive jumlah probabilitasnya adalah 1')
    st.write("Berdasarkan uraian, rumus probabilitas adalah: ")
    st.latex(r'P(A) = \frac{Outcome A}{Outcome S}')
    
    st.subheader("Aturan Probabilitas")
    st.write("**Aturan Komplemen**: Kejadian dimana A tidak terjadi")
    st.latex(r'P(A^c) = 1 - P(A)')
    st.write("**Aturan Perkalian (Conditional Probability)**: Probabilitas dua kejadian")
    st.latex(r'P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0')
    st.latex(r'P(A \cap B) = P(A \mid B) \cdot P(B)')
    st.write("Note: Rumus tersebut jika manipulasi menjadi P(A irisan B)= P(A|B) P(B) Jika A dan B saling independen maka P(A irisan B)=P(A)P(B)")
    st.write("**Aturan Penjumlahan:** Aturan penjumlahan digunakan untuk menghitung probabilitas kejadian A atau B atau keduanya A dan B terjadi")
    st.latex(r'P(A \cup B) = P(A) + P(B) - P(A \cap B)')
    st.write("**Aturan Probabilitas Total:** ")
    st.markdown(r'''Jika \{B_1, B_2,..., B_n\} adalah partisi ruang sample S, maka: ''')
    c1, c2 = st.columns(2)
    with c1:
        st.latex(r'P(A) = \sum_{i=1}^{n} P(A \mid B_i) \cdot P(B_i)')
    with c2: 
        st.markdown("![Total Prob](https://github.com/user-attachments/assets/e7b243ee-4bc3-4ffc-88f9-4e275d3a7256)")

    st.markdown(r"**Teorema Bayes**: Jika \{B_1, B_2,..., B_n\} adalah partisi ruang sample S, maka: ")
    st.latex(r'P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}, \quad P(B) > 0')
    st.write("**Catatan Kejadian Independen**")
    st.markdown("![independen](https://github.com/user-attachments/assets/5bced8ff-0cd1-4d94-9e96-fbf878573f86)")
    st.write("Contoh soal: ")
    st.write("Suatu pabrik mempunyai 3 mesin A, B dan C. masing-masing peluang berproduksi adalah 60%, 30% dan 10%. Persentase kerusakan produksi yang disebabkan oleh masing-masing mesin 2%, 3% dan 4%. Misal dipilih satu unit produksi dan diketahui rusak. Maka hitung probabilitas bahwa kerusakan produk yang diambil dari mesin C!")
    bayesian = st.number_input(label = "Hint: Produk C dengan diketahui produk rusak ")
    c_given_r = 0.1*0.04 / ((0.6)*(0.02)+(0.3)*(0.03)+(0.1)*(0.04))
    if bayesian:
        if np.round(bayesian, 1) == np.round(c_given_r, 1):
            st.write("Jawaban Anda Benar !", c_given_r)
        else:
            st.write("Belum benar, buka solusi")
            if st.button("Solusi"): 
                st.latex(r"""P(C \mid R) = \frac{P(C \cap R)}{P(R)}""")
                st.latex(r'P(C \mid R) = \frac{P(C) . P(R \mid C)}{P(R)}')
                st.latex(r'P(C \mid R) = \frac{0.01 * 0.04}{(0.6)*(0.02)+(0.3)*(0.03)+(0.1)*(0.04)}')
                st.latex(r'P(C \mid R) = 0.16')
    st.caption("Credits : Staff UNS")
    #https://getut.staff.uns.ac.id/files/2016/08/Bab-2_2-2016.pdf
    st.header("Soal UTS")
    st.subheader("2021")
    st.markdown("![uts_3 2021](https://github.com/user-attachments/assets/62e9b9e5-95f2-40a1-969e-1d67546af3ee)")
    if st.button("Solusi 3"): 
        st.write("*Solusi*")
        st.markdown("![solusi_3_2021](https://github.com/user-attachments/assets/767aa9b5-dc1a-4c39-9d92-f55386fea75a)")
    st.header("Distribusi Probabilitas Diskrit dan Binomial")
    st.markdown("""
- Random Variabel: kejadian suatu experimen, misal P(X=1) ?
- Probability Mass Function : Random Variabel diskrit, kayak tadi P(X=1)
- Cumulative Distributive Function : Continous misal P(X<= 1)
                """)
    st.subheader("**Discrete Probability Distribution**")
    st.latex(r'E(X) = \sum_{i=1}^{n} x_i \cdot p_i')
    st.latex(r'\text{Var}(X) = \sum_{i=1}^{n} (x_i - E(X))^2 \cdot p_i')
    st.latex(r'\sigma_X = \sqrt{\text{Var}(X)}')
    st.subheader("Counting Rules")
    st.markdown(""" ![counting rules](https://images.slideplayer.com/32/9965822/slides/slide_25.jpg)
- Permutation : berhubungan dengan pengaturan objek-objek di mana urutan sangat penting. Dalam permutasi, kita menanyakan berapa banyak cara untuk mengatur sejumlah objek dari himpunan, di mana urutan memengaruhi hasil.
- Kombinasi : berhubungan dengan pemilihan objek-objek di mana urutan tidak penting. Dalam kombinasi, kita menanyakan berapa banyak cara untuk memilih sejumlah objek dari himpunan tanpa memperhatikan urutannya.
""")
    st.subheader("Binominal (Juga Probabilitas Diskrit)")
    st.markdown("""
Distribusi Probabilitas Binomial berbicara tentang probabilitas keberhasilan atau kegagalan suatu hasil dalam serangkaian peristiwa. Distribusi Binomial Probabilitas memetakan hasil yang diperoleh dalam bentuk sukses atau gagal, ya atau tidak, benar atau salah, dan sebagainya. Setiap percobaan yang dilakukan untuk mendapatkan hasil sukses atau gagal disebut Percobaan Bernoulli dan distribusi probabilitas untuk setiap Percobaan Bernoulli disebut Distribusi Bernoulli. Mari kita pelajari definisi dan pengertian Distribusi Binomial.
1. Fixed Number of Trials: Ada sejumlah percobaan atau eksperimen (dilambangkan dengan n), seperti melempar koin sebanyak 10 kali.
2. Two Possible Outcomes: Setiap percobaan hanya memiliki dua kemungkinan hasil, yang sering diberi label “sukses” dan “gagal”. Misalnya, mendapatkan kepala atau ekor dalam lemparan koin.
3. Independent Trials: Hasil dari setiap percobaan tidak bergantung pada percobaan lainnya, artinya hasil dari satu percobaan tidak memengaruhi hasil percobaan lainnya.
4. Constant Probability: Probabilitas keberhasilan (dilambangkan dengan p) tetap sama untuk setiap percobaan. Misalnya, jika Anda melempar koin, probabilitas untuk mendapatkan kepala selalu 0,5.
                """)
    st.latex(r'P(X = k) = \frac{n!}{k! (n - k)!} p^k (1 - p)^{n - k}')
    st.latex(r'E(X) = n \cdot p')
    st.latex(r'\text{Var}(X) = n \cdot p \cdot (1 - p)')
    st.latex(r'\sigma_X = \sqrt{n \cdot p \cdot (1 - p)}')
    st.write("Contoh soal: ")
    st.write("Sebuah survei kebersihan gigi memperlihatkan bahwa 2 dari 5 orang sudahpergi ke dokter gigi dalam beberapa bulan terakhir. Apabila ada 12 orangterpilih secara acak, hitunglah probabilitas 4 diantaranya pergi ke dokterdua bulan lalu?")
    so_s = 0.21284
    binomial = st.number_input(label="Probabilitas 4 orang: ")
    if binomial:
        if np.round(binomial, 1) == np.round(so_s, 1):
            st.write("Jawaban Anda Benar !", so_s)
        else:
            st.write("Belum benar")
    st.header("Soal UTS")
    st.subheader('UTS 2021')
    st.markdown("![uts_4 2021](https://github.com/user-attachments/assets/0af8bd4a-7cca-4e99-a992-e5fcc5d26698)")
    if st.button("Solusi 4"): 
        st.write("*Solusi*")
        st.markdown("""a. Metode nya adalah Binomial, hal itu dikarenakan\n
- Sejumlah y percobaan dilakukan (diskrit fixed number of trials)\n
- Hanya akan ada 2 kemungkinan (mengenai target -> sukses, dengan tidak kena target -> gagal)\n
- Independent (Satu percobaan tidak mengenai yang lain)\n
- Constant : probabilitas nya selalu sama
                    """)
        st.markdown("![solusi_4_2021](https://github.com/user-attachments/assets/be46ffd7-1884-4c67-9ee4-19fc32eb78a1)")
    st.subheader('UTS 2023')
    # st.markdown("![uts_4 2021]()")
    show_pdf("uts_2023.pdf")
    with open("uts_2023.pdf", "rb") as file:
        btn = st.download_button(
            label="Download UTS (1 page)",
            data=file,
            file_name="uts_2023.pdf",
            mime="application/pdf"
        )
    st.header("Semangat UTS semoga memuaskan !")
st.markdown("*Copyright © 2024 Ludy Hasby Aulia*")