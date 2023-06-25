from streamlit_antd_components import antd_menu, MenuItem
import streamlit as st
import pandas as pd
import hydralit_components as hc
import modul
import base64
from pathlib import Path
import os
import time


st.set_page_config(layout='wide')

# Session
if 'login' not in st.session_state:
    st.session_state['login'] = ''

if 'type_encrypt' not in st.session_state:
    st.session_state['type_encrypt'] = ''

if 'type_decrypt' not in st.session_state:
    st.session_state['type_decrypt'] = ''

# Styling Text
st.markdown("""
<style>
.text-font {
    font-size:18px !important;
    allign='justify';
}
</style>
""", unsafe_allow_html=True)

# Background
modul.add_bg_from_local('background.jpg')

# Remove title link
st.markdown("""
<style>
    [class="css-13ss8fl e16nr0p32"]{
        display : none;
    }
    
    [class="css-1viaosz e19lei0e1"]{
        display : none;
    }
</style>""", unsafe_allow_html=True)

# Setting Color
page_bg_img="""
<style>
[data-testid="stHeader"]{
background-color : rgba(0, 0, 0, 0);
}

div.stButton > button:first-child{
background-color : #9CC4FF;
}

.title {
    color: black;
}

[data-testid="column"]{
background-color : rgba(0, 0, 0, 0);
}

[data-testid="stForm"] {
    background-color: rgba(255, 255, 255, .7);
    border-radius: 15px;
}
[class="css-15pt459 edgvbvh10"] {
    background-color: rgba(255, 255, 255, .7);
}
[class="navbar navbar-mainbg parent"] {
    background-color: rgba(255, 255, 255, .7);
    border-radius: 15px;
}

[data-baseweb="base-input"] {
    background-color: rgb(255, 255, 255);
    color: black;
}
[data-baseweb="input"] {
    background-color: rgb(255, 255, 255);
    color: black;
</style>
"""

def caesar_encrypt(message, key):
    simbol = [chr(i) for i in range(1, 48)] + [chr(i) for i in range(58, 65)] + [chr(i)
                                                                                 for i in range(91, 97)] + [chr(i) for i in range(123, 128)]
    simbol.remove(" ")

    alpha = "".join(chr(i) for i in range(65, 91))
    beta = "".join(chr(i) for i in range(97, 123))
    simbol = "".join(i for i in simbol)
    number = "".join(chr(i) for i in range(48, 58))
    result = ""

    # print("===== Data Caesar =====")
    # print("==== Alpha\n{}\n\nBeta\n{}\n\nSimbol\n{}\n\nNumber\n{}\n\n".format(
    #     alpha, beta, simbol, number
    # ))

    for letter in message:
        if letter in simbol:  # if the letter is actually a letter
            # find the corresponding ciphertext letter in the simbolbet
            letter_index = (simbol.find(letter) + key) % len(simbol)

            result = result + simbol[letter_index]

        elif letter in number:
            letter_index = (number.find(letter) + key) % len(number)

            result = result + number[letter_index]

        elif letter in alpha:
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]

        elif letter in beta:
            letter_index = (beta.find(letter) + key) % len(beta)

            result = result + beta[letter_index]

        else:
            result = result + letter

    return result

st.markdown(page_bg_img, unsafe_allow_html=True)

if st.session_state['login'] == '':
    buffer, col1, col2, col3 = st.columns([.75, 3.5, .5, 4])
    with col1:
        st.markdown("<h3 align='center'> Sistem Pengamanan Pesan Email Menggunakan Enkripsi Caesar Cipher dan Vigenere Cipher</h3>", unsafe_allow_html=True)
        for i in range(3):
            st.write("")
        
        option = st.selectbox("", ('Login', 'Signup'))

        if option == "Login":
            form_login = st.empty()

            with form_login.form('login_form'):
                email = st.text_input("Email")
                password = st.text_input("Password", type='password')
                submit = st.form_submit_button(option)

                if submit:
                    if str(email).__contains__("@"):
                        login_func = modul.login(email, password)

                        if login_func == True:
                            st.markdown("<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> Login Berhasil ! </p>",unsafe_allow_html=True) 
                            st.session_state['login'] = email
                        else:
                            st.warning("Login Gagal !")
                    else:
                        st.warning("Masukan Email dengan benar !")
        
        else:
            form_signup = st.empty()

            with form_signup.form('signup'):
                email = st.text_input("Email")
                nama = st.text_input("Nama Lengkap")
                password = st.text_input("Password", type='password')
                konfirmasi_pass = st.text_input("Konfirmasi Password", type='password')
                submit = st.form_submit_button(option)

                if submit:
                    if str(email) == '' or str(nama) == '' or str(password) == '' or str(konfirmasi_pass) == '':
                        st.warning("Data Tidak Boleh Kosong !")

                    
                    elif str(password) != str(konfirmasi_pass):
                        st.warning("Password Harus Sesuai dengan Konfirmasi Password !")
                    
                    elif not str(email).__contains__("@"):
                        st.warning("Masukan Email dengan benar !")


                    else:
                        signup_func = modul.signup(email, nama, password)

                        if signup_func == True:
                            st.markdown("<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> Signup Berhasil ! </p>",unsafe_allow_html=True) 
                        else:
                            st.warning("Signup Gagal !")
            

    with col3:
        st.image("https://test114.my.canva.site/videos/26d7319b7613888df6f8c3bcae1f2bf5.gif",width=540)


else:
    items = [
        MenuItem('Beranda', 'beranda', icon='house'),
        MenuItem('Cryptography', 'cryptography', icon='file-earmark-lock-fill', children=[
            MenuItem('Enkripsi', 'enkripsi', icon='lock-fill'),
            MenuItem('Dekripsi', 'dekripsi', icon='unlock-fill'),
        ]),
        MenuItem('Message Box', 'message box', icon='chat-left-text'),
        MenuItem('Setup Email', 'setup email', icon='envelope'),
        MenuItem('Logout', 'logout', icon='box-arrow-left'),

    ]
    with st.sidebar.container():
        nama = modul.get_nama(st.session_state['login'])
        st.success(f"# Selamat Datang ..\n#### {nama[1]}\n###### {str(st.session_state['login'])}")
        item = antd_menu(
            items=items,
            selected_key='beranda',
        )

    if str(item) == "beranda":
        st.markdown('''
        <h3 align='center'> Sistem Pengamanan Pesan Email Menggunakan Enkripsi</h3>
        ''', unsafe_allow_html=True)

        st.markdown('''
        <h3 align='center'> Caesar Cipher dan Vigenere Cipher</h3>
        ''', unsafe_allow_html=True)

        buffer, col1, col2 = st.columns([2, 6, 2])
        with col1:
            for i in range(2):
                st.write("")
            st.image("encryption_img_crop.png")
            st.write("")  

        buffer, col1, col2 = st.columns([1.5, 6, 1.5])
        with col1:
            st.markdown("<h3> Enkripsi Data </h3>", unsafe_allow_html=True)

            st.markdown("<p class='text-font', align='justify'>Istilah enkripsi menjadi istilah yang tidak cukup asing baik bagi para penggeliat dunia teknologi informasi ataupun masyarakat pada umumnya. Enkripsi adalah metode pengubahan bentuk data menjadi sejumlah kode yang sulit diterjemahkan, sehingga data tidak dapat dibaca oleh sembarang pihak. Data yang telah dienkripsi hanya akan dapat dibaca oleh si penerima dengan menggunakan kunci-kunci tertentu. Kunci ini bisa didapatkan langsung oleh si pembuat dokumen atau data.", unsafe_allow_html=True)

            st.markdown("<h3> Metode Enkripsi Data</h3>", unsafe_allow_html=True)
            
            st.markdown("<h4> 1. Caesar Cipher </h4>", unsafe_allow_html=True)
            st.markdown("<p class='text-font', align='justify'>Penggunaan sandi substitusi yang paling awal diketahui dan paling sederhana adalah oleh Julius Caesar. Caesar Cipher melibatkan mengganti (subtitusi) setiap huruf alfabet dengan huruf berdiri tiga tempat lebih jauh ke bawah alphabet [5]. Dalam kriptografi, tidak mengenal cara menyandikan huruf dan angka desimal. Solusinya adalah mengubah huruf tersebut menjadi deretan bilangan bulat (integer). Misal huruf A menjadi angka 1, huruf B menjadi angka 2, dan seterusnya hingga huruf Z menjadi angka 26. Sebagai Contoh :", unsafe_allow_html=True)
            df = pd.DataFrame.from_dict({
                'No' : [1, 2],
                'Pesan' : ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'],
                'Key' : [1, 2],
                'Enrkipsi' : ['bcdefghijklmnopqrstuvwxyza', 'cdefghijklmnopqrstuvwxyzab']
            })
            df = df.set_index(['No'])
            st.table(df)

            st.markdown("<h4> 2. Vigenere Cipher </h4>", unsafe_allow_html=True)
            st.markdown("<p class='text-font', align='justify'>Vigenere Cipher adalah suatu algoritma kriptografi klasik yang ditemukan oleh Giovan Battista Bellaso. Beliau menuliskan metodenya tersebut pada bukunya yang berjudul La Cifra del. Sig. Giovan Battista Bellaso pada tahun 1553. Nama vigenere sendiri diambil dari seorang yang bernama Blaisede Vigenere. Nama vigenere diambil sebagai nama algoritma ini karena beliau menemukan kunci yang lebih kuat lagi untuk algoritma ini dengan metode autokey cipher meskipun algoritma dasarnya telah ditemukan lebih dahulu oleh Giovan Battista Bellaso.", unsafe_allow_html=True)


    elif str(item) == "enkripsi":
        buffer, col1, col2 = st.columns([2, 6, 2])
        with col1:
            option_data = [
                        {'label':"Caesar Cipher"},
                        {'label':"Viginere Cipher"},
                        {'label':"Combined Cipher (Caesar & Viginere)"},
                        {'label' : "Viginere dengan Key Caesar"}
                    ]

            over_theme = {'txc_inactive': 'black','menu_background':'#ECF5FE','txc_active':'black','option_active':'#fafafa'}
            font_fmt = {'font-class':'h2','font-size':'150%'}

            op = hc.option_bar(option_definition=option_data,key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

        if str(op) == "Caesar Cipher":
            st.session_state['type_encrypt'] = "Caesar Cipher"

        if str(op) == "Viginere Cipher":
            st.session_state['type_encrypt'] = "Viginere Cipher"

        if str(op) == "Combined Cipher (Caesar & Viginere)":
            st.session_state['type_encrypt'] = "Combined Cipher (Caesar & Viginere)"

        if str(op) == "Viginere dengan Key Caesar":
            st.session_state['type_encrypt'] = "Viginere dengan Key Caesar"

        st.markdown(f"<h3 align='center'>Enkripsi {str(st.session_state['type_encrypt'])}</h3>", unsafe_allow_html=True)
        buffer, col1, col2 = st.columns([2, 6, 2])
        with col1:
            encryption_form = st.empty()
            with encryption_form.form('Enkripsi', clear_on_submit=True):
                to = st.text_input("To", placeholder="example@gmail.com")
                subject = st.text_input("Subject")
                text = st.text_area("Body")
                if st.session_state['type_encrypt'] == "Caesar Cipher":
                    number_encrypt = st.number_input("Key", min_value=1, max_value=25, step=1)
                else:
                    number_encrypt = st.text_input('Key')
                uploaded_file = st.file_uploader("Choose a file")
                submit = st.form_submit_button("Enkripsi")

                if submit:
                    if str(text) == "" or str(to) == "" or str(subject) == "":
                        st.warning("Form tidak boleh kosong !")
                    
                    else:
                        if uploaded_file != None:
                            save_folder = os.getcwd() + '/File/'
                            save_path = Path(save_folder, uploaded_file.name)
                            with open(save_path, mode='wb') as w:
                                w.write(uploaded_file.getvalue())

                        check_key = modul.check_key(str(st.session_state['login']))
                        if type(check_key) != bool:
                            data_encrypt = ""
                            if str(st.session_state['type_encrypt']) == "Caesar Cipher":
                                start = time.perf_counter()
                                data_encrypt = modul.caesar_encrypt(str(text), number_encrypt)
                                end = time.perf_counter()

                            if str(st.session_state['type_encrypt']) == "Viginere Cipher":
                                start = time.perf_counter()
                                data_encrypt = modul.viginere_encrypt(str(text), number_encrypt)
                                end = time.perf_counter()

                            if str(st.session_state['type_encrypt']) == "Viginere dengan Key Caesar":
                                start = time.perf_counter()
                                key_caesar = modul.caesar_encrypt(str(number_encrypt), 3)
                                data_encrypt = modul.viginere_encrypt(str(text), str(key_caesar))
                                end = time.perf_counter()
                                
                            if str(st.session_state['type_encrypt']) == "Combined Cipher (Caesar & Viginere)":
                                start = time.perf_counter()
                                data_encrypt = modul.encrypt_combined_chipper(str(text), str(number_encrypt))
                                end = time.perf_counter()

                            duration = (end - start) * 1000
                            st.markdown("<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'>Sukses</p>",unsafe_allow_html=True)
                            st.markdown(f"<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> {data_encrypt} </p>",unsafe_allow_html=True)
                            st.markdown(f"<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> Waktu Proses : {float(duration)} </p>",unsafe_allow_html=True) 
                 
                            modul.sender_email(str(st.session_state['type_encrypt']), str(st.session_state['login']),str(check_key[1]), str(to), str(subject), str(data_encrypt), number_encrypt, text)

                            with st.expander("Penjelasan Algoritma.."):
                                sample_data = text.split(" ")[0]

                                if str(st.session_state['type_encrypt']) == "Caesar Cipher":
                                    st.markdown(f"<h4 align='center'> Enkripsi {st.session_state['type_encrypt']} </h4>", unsafe_allow_html=True)
                                    st.markdown("<h5>==Info Enkripsi==", unsafe_allow_html=True)
                                    st.write(f"##### Text Sample : {sample_data}")
                                    st.write(f"##### Key : {number_encrypt}")
                                    data_encrypt = modul.caesar_encrypt_explain(str(sample_data), number_encrypt)

                                if str(st.session_state['type_encrypt']) == "Viginere Cipher":
                                    st.markdown(f"<h4 align='center'> Enkripsi {st.session_state['type_encrypt']} </h4>", unsafe_allow_html=True)
                                    st.markdown("<h5>==Info Enkripsi==", unsafe_allow_html=True)
                                    data_encrypt = modul.viginere_encrypt_explain(str(sample_data), number_encrypt)

                                if str(st.session_state['type_encrypt']) == "Combined Cipher (Caesar & Viginere)":
                                    st.markdown(f"<h4 align='center'> Enkripsi Text Caesar Cipher </h4>", unsafe_allow_html=True)
                                    st.markdown("<h5>==Info Enkripsi==", unsafe_allow_html=True)
                                    st.write(f"##### Text Sample : {sample_data}")
                                    st.write(f"##### Key : 3")
                                    key_caesar = modul.caesar_encrypt_explain(str(sample_data), 3)
                                    st.markdown(f"<h4 align='center'> Enkripsi Viginere Cipher dengan key text Caesar</h4>", unsafe_allow_html=True)
                                    st.markdown("<h5>==Info Enkripsi==", unsafe_allow_html=True)
                                    data_encrypt = modul.viginere_encrypt_explain(str(sample_data), str(key_caesar))
   
                                if str(st.session_state['type_encrypt']) == "Viginere dengan Key Caesar":
                                    st.markdown(f"<h4 align='center'> Enkripsi Key Caesar Cipher </h4>", unsafe_allow_html=True)
                                    st.markdown("<h5>==Info Enkripsi==", unsafe_allow_html=True)
                                    st.write(f"##### Text Sample : {number_encrypt}")
                                    st.write(f"##### Key : 3")
                                    key_caesar = modul.caesar_encrypt_explain(str(number_encrypt), 3)
                                    st.markdown(f"<h4 align='center'> Enkripsi Viginere Cipher dengan Key Caesar</h4>", unsafe_allow_html=True)
                                    st.markdown("<h5>==Info Enkripsi==", unsafe_allow_html=True)
                                    data_encrypt = modul.viginere_encrypt_explain(str(sample_data), str(key_caesar))
                                # st.markdown(f"<h4 align='center'> Enkripsi {st.session_state['type_encrypt']} </h4>", unsafe_allow_html=True)
                                # data_sample = text.split(" ")
                                # st.write(f"Sample Kalimat : {data_sample[0]}")


                        else:
                            st.warning("Setup Email Terlebih Dahulu !")

    elif str(item) == "dekripsi":
        buffer, col1, col2 = st.columns([2, 6, 2])
        with col1:
            option_data = [
                        {'label':"Caesar Cipher"},
                        {'label':"Viginere Cipher"},
                        {'label':"Combined Cipher (Caesar & Viginere)"},
                        {'label' : "Viginere dengan Key Caesar"}
                    ]

            over_theme = {'txc_inactive': 'black','menu_background':'#ECF5FE','txc_active':'black','option_active':'#fafafa'}
            font_fmt = {'font-class':'h2','font-size':'150%'}

            op = hc.option_bar(option_definition=option_data,key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

        if str(op) == "Caesar Cipher":
            st.session_state['type_decrypt'] = "Caesar Cipher"

        if str(op) == "Viginere Cipher":
            st.session_state['type_decrypt'] = "Viginere Cipher"

        if str(op) == "Combined Cipher (Caesar & Viginere)":
            st.session_state['type_decrypt'] = "Combined Cipher (Caesar & Viginere)"

        if str(op) == "Viginere dengan Key Caesar":
            st.session_state['type_decrypt'] = "Viginere dengan Key Caesar"

        st.markdown(f"<h3 align='center'>Dekripsi {str(st.session_state['type_decrypt'])}</h3>", unsafe_allow_html=True)
        buffer, col1, col2 = st.columns([2, 6, 2])
        with col1:
            decryption_form = st.empty()

            with decryption_form.form('Dekripsi', clear_on_submit=True):
                text = st.text_area("Masukan Text")
                if str(st.session_state['type_decrypt']) == "Caesar Cipher":
                    number_encrypt = st.number_input('Key Number', step=1, min_value=1, max_value=25)
                else:
                    number_encrypt = st.text_input("Key Number")

                submit = st.form_submit_button("Dekripsi")

                if submit:
                    if str(text) == "":
                        st.warning("Text tidak boleh kosong !")
                    
                    else:
                        data_encrypt = ""
                        if str(st.session_state['type_decrypt']) == "Caesar Cipher":
                            start = time.perf_counter()
                            data_encrypt = modul.caesar_decrypt(str(text), number_encrypt)
                            end = time.perf_counter()

                        if str(st.session_state['type_decrypt']) == "Viginere Cipher":
                            start = time.perf_counter()
                            data_encrypt = modul.viginere_decrypt(str(text), number_encrypt)
                            end = time.perf_counter()

                        if str(st.session_state['type_decrypt']) == "Viginere dengan Key Caesar":
                            start = time.perf_counter()
                            key_caesar = modul.caesar_encrypt(str(number_encrypt), 3)
                            data_encrypt = modul.viginere_decrypt(str(text), str(key_caesar))
                            end = time.perf_counter()
                            
                        if str(st.session_state['type_decrypt']) == "Combined Cipher (Caesar & Viginere)":
                            start = time.perf_counter()
                            data_encrypt = modul.decrypt_combined_chipper(str(text), str(number_encrypt))
                            end = time.perf_counter()
                        
                        st.markdown("<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'>Sukses</p>",unsafe_allow_html=True)
                        st.markdown(f"<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> {data_encrypt} </p>",unsafe_allow_html=True) 
                        st.markdown(f"<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> Waktu Proses : {(end - start) * 1000} </p>",unsafe_allow_html=True)
                        with st.expander("Penjelasan Algoritma.."):
                            sample_data = text.split(" ")[0]
                            if str(st.session_state['type_decrypt']) == "Caesar Cipher":
                                    st.markdown(f"<h4 align='center'> Dekripsi {st.session_state['type_decrypt']} </h4>", unsafe_allow_html=True)
                                    st.markdown("<h5>==Info Dekripsi==", unsafe_allow_html=True)
                                    st.write(f"##### Text Sample : {sample_data}")
                                    st.write(f"##### Key : {number_encrypt}")
                                    data_encrypt = modul.caesar_decrypt_explain(str(sample_data), number_encrypt)

                            if str(st.session_state['type_decrypt']) == "Viginere Cipher":
                                st.markdown(f"<h4 align='center'> Dekripsi {st.session_state['type_decrypt']} </h4>", unsafe_allow_html=True)
                                st.markdown("<h5>==Info Dekripsi==", unsafe_allow_html=True)
                                data_encrypt = modul.viginere_decrypt_explain(str(sample_data), number_encrypt)

                            if str(st.session_state['type_decrypt']) == "Combined Cipher (Caesar & Viginere)":
                                st.markdown(f"<h4 align='center'> Dekripsi Text Viginere Cipher</h4>", unsafe_allow_html=True)
                                st.markdown("<h5>==Info Dekripsi==", unsafe_allow_html=True)
                                key_caesar = modul.viginere_decrypt_explain(str(sample_data), number_encrypt)
                                st.markdown(f"<h4 align='center'> Dekripsi Caesar Cipher dengan key text Viginere</h4>", unsafe_allow_html=True)
                                st.markdown("<h5>==Info Dekripsi==", unsafe_allow_html=True)
                                st.write(f"##### Text Sample : {key_caesar}")
                                st.write(f"##### Key : 3")
                                data_encrypt = modul.caesar_decrypt_explain(str(key_caesar), 3)

                            if str(st.session_state['type_decrypt']) == "Viginere dengan Key Caesar":
                                st.markdown(f"<h4 align='center'> Dekripsi Key Caesar Cipher </h4>", unsafe_allow_html=True)
                                st.markdown("<h5>==Info Dekripsi==", unsafe_allow_html=True)
                                st.write(f"##### Text Sample : {number_encrypt}")
                                st.write(f"##### Key : 3")
                                key_caesar = modul.caesar_encrypt_explain(str(number_encrypt), 3)
                                st.markdown(f"<h4 align='center'> Dekripsi Viginere Cipher dengan Key Caesar</h4>", unsafe_allow_html=True)
                                st.markdown("<h5>==Info Dekripsi==", unsafe_allow_html=True)
                                data_encrypt = modul.viginere_decrypt_explain(str(sample_data), str(key_caesar))
                            
    elif str(item) == "message box":
        option_data = [
                    {'label':"Inbox"},
                    {'label':"Notification"}
                ]
        over_theme = {'txc_inactive': 'black','menu_background':'#eee','txc_active':'black','option_active':'#fafafa'}
        font_fmt = {'font-class':'h2','font-size':'150%'}

        op = hc.option_bar(option_definition=option_data,key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

        if str(op) == "Notification":
            data =  modul.get_notification(str(st.session_state['login']))
            for i in range(len(data)):
                if str(data[i][5]) == 'Sender':
                    out = str(data[i][2]).replace('@gmail.com', '')
                    text = "Anda Mengirim Pesan ke {} pada Jam {}".format(out, data[i][4])
                    with st.expander(str(text)):
                        st.text_area(label = '', value=data[i][3], key=i)
                else:
                    if str(data[i][2]) == str(st.session_state['login']):
                        st.markdown(f"<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> Anda Mendapatkan Pesan dari {data[i][1]} Pada Jam {data[i][4]}! </p>",unsafe_allow_html=True)
        
        if str(op) == "Inbox":
            data =  modul.get_notification(str(st.session_state['login']))
            for i in range(len(data)):
                if str(data[i][5]) == "Receiver":
                    if str(data[i][2]) == str(st.session_state['login']):
                        inp = str(data[i][2]).replace('@gmail.com', '')
                        text = f"Anda Mendapatkan Pesan dari {inp} pada Jam {data[i][4]}"
                        with st.expander(str(text)):
                            st.text_area(label = '', value=data[i][3], key=i)

    elif str(item)== "setup email":
        st.markdown("<h3 align='center'>Email Setup Key</h3>", unsafe_allow_html=True)
        buffer, col1, col2 = st.columns([2, 6, 2])
        with col1:
            data_email = st.empty()
            with data_email.form('data_email'):
                with st.expander("Demo"):
                    file_ = open("demo/demo.gif", "rb")
                    contents = file_.read()
                    data_url = base64.b64encode(contents).decode("utf-8")
                    file_.close()

                    st.markdown(
                        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                        unsafe_allow_html=True,
                    )
                st.markdown(f"<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> Note : Harus Menggunakan Email yang sama pada saat login sistem !! </p>",unsafe_allow_html=True)
                st.markdown("<p>Link : <a href='https://myaccount.google.com/apppasswords?rapt=AEjHL4NIjmy_-vtL7RcXyRnksDTxUbGll8i8UrXYD-jQKXoDab3FRHfG5MJL3MJfroNIK32MXQd1Nqnk4Urk27wJGe0OPf3qYg'>Klik disini<a></p>", unsafe_allow_html=True)
                generate_password = st.text_input("Generate Key", type='password')
                submit = st.form_submit_button("Send Key")

                if submit:
                    test_key = modul.send_key(str(st.session_state['login']), str(generate_password))

                    if test_key == True:
                        st.markdown(f"<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> Berhasil Menginputkan Key ! </p>",unsafe_allow_html=True)
                    else:
                        st.warning("Gagal Menginputkan Key !")

    elif str(item)=="logout":
        st.markdown("<p style='background-color:#C5ECE2; color:black; line-height:60px; padding-left:17px;'> Logout Berhasil ! </p>",unsafe_allow_html=True) 
        st.session_state['login'] = ''
