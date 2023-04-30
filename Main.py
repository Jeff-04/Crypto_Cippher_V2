import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import base64
from pathlib import Path
import os
import hydralit_components as hc

import modul

st.set_page_config(layout='wide')

# Styling Text
st.markdown("""
<style>
.text-font {
    font-size:18px !important;
    allign='justify';
}
</style>
""", unsafe_allow_html=True)

# Session
if 'login' not in st.session_state:
    st.session_state['login'] = ''



if st.session_state['login'] == '':
    buffer, col1, col2, col3 = st.columns([.75, 3.5, .5, 4])
    with col1:
        st.markdown("<h3 align='center'> Sistem Pengamanan Pesan Email Menggunakan Enkripsi Chaesar Chipper dan Vigenere Chipper</h3>", unsafe_allow_html=True)
        for i in range(3):
            st.write("")
        
        # st.markdown("<h3 align='center'>Login</h3>", unsafe_allow_html=True)
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
                            st.success("Login Berhasil")
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
                            st.success("Signup Berhasil")
                        else:
                            st.warning("Signup Gagal !")
            

    with col3:
        st.image("https://test114.my.canva.site/videos/26d7319b7613888df6f8c3bcae1f2bf5.gif",width=540)


else:
    selected = ''
    with st.sidebar:
        selected = option_menu(
        menu_title = None,
        options = ['Beranda', 'Encryption', 'Message Box', 'Setup Email', 'Logout'],
        icons = ["house", "file-earmark-lock-fill", 'chat-left-text', 'envelope', "box-arrow-left"],
        menu_icon = 'cast',
        orientation = "vertical",
        styles={
        "container" : {"background-color" : '#eee', 'color' : 'white'},#fafafa
        "nav-link-selected": {"background-color": '#fafafa', 'color' : 'rgb(10,21,29)'},
        "nav-link" : {"--hover-color": "#eee"}
        }
        )
    
    if selected == "Beranda":
        st.markdown('''
        <h3 align='center'> Sistem Pengamanan Pesan Email Menggunakan Enkripsi</h3>
        ''', unsafe_allow_html=True)

        st.markdown('''
        <h3 align='center'> Chaesar Chipper dan Vigenere Chipper</h3>
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
            
            st.markdown("<h4> 1. Chaesar Chipper </h4>", unsafe_allow_html=True)
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

    elif selected == "Encryption":
        buffer, col1, col2 = st.columns([2, 6, 2])
        with col1:
            choose = st.selectbox('', ('Enkripsi', 'Dekripsi'))
            st.write("")
            option_data = [
                {'label':"Caesar Chipper"},
                {'label':"Viginere Chipper"},
                {'label':"Combined Chipper (Caesar & Viginere)"},
                {'label' : "Viginere dengan Key Caesar"}
            ]

            # override the theme, else it will use the Streamlit applied theme
            over_theme = {'txc_inactive': 'black','menu_background':'#eee','txc_active':'black','option_active':'#fafafa'}
            font_fmt = {'font-class':'h2','font-size':'150%'}

            # display a horizontal version of the option bar
            op = hc.option_bar(option_definition=option_data,key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)
        if choose == 'Enkripsi':
            if str(op) == "Caesar Chipper":
                st.markdown("<h3 align='center'>Enkripsi Chaesar Chipper</h3>", unsafe_allow_html=True)
                buffer, col1, col2 = st.columns([2, 6, 2])
                with col1:
                    encryption_form = st.empty()
                    with encryption_form.form('Enkripsi'):
                        to = st.text_input("To", placeholder="example@gmail.com")
                        subject = st.text_input("Subject")
                        text = st.text_area("Body")
                        number_encrypt = st.number_input('Key Number', step=1, min_value=1, max_value=25)
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
                                    data_encrypt = modul.caesar_encrypt(str(text), number_encrypt)
                                    st.success("Sukses")
                                    st.success(data_encrypt)
                                    modul.sender_email("Caesar Chipper", str(st.session_state['login']),str(check_key[1]), str(to), str(subject), str(data_encrypt), number_encrypt, text)
                                else:
                                    st.warning("Setup Email Terlebih Dahulu !")

            elif str(op) == "Viginere Chipper":
                st.markdown("<h3 align='center'>Enkripsi Viginere Chipper</h3>", unsafe_allow_html=True)
                buffer, col1, col2 = st.columns([2, 6, 2])
                with col1:
                    encryption_form = st.empty()
                    with encryption_form.form('Enkripsi'):
                        to = st.text_input("To", placeholder="example@gmail.com")
                        subject = st.text_input("Subject")
                        text = st.text_area("Body")
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
                                    data_encrypt = modul.viginere_encrypt(str(text), str(number_encrypt))
                                    st.success("Sukses")
                                    st.success(data_encrypt)
                                    modul.sender_email("Viginere Chipper", str(st.session_state['login']),str(check_key[1]), str(to), str(subject), str(data_encrypt), number_encrypt, text)
                                    
                                else:
                                    st.warning("Setup Email Terlebih Dahulu !")
            
            elif str(op) == "Viginere dengan Key Caesar":
                st.markdown("<h3 align='center'>Viginere dengan Key Caesar</h3>", unsafe_allow_html=True)
                buffer, col1, col2 = st.columns([2, 6, 2])
                with col1:
                    encryption_form = st.empty()
                    with encryption_form.form('Enkripsi'):
                        to = st.text_input("To", placeholder="example@gmail.com")
                        subject = st.text_input("Subject")
                        text = st.text_area("Body")
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
                                    key_caesar = modul.caesar_encrypt(str(number_encrypt), 3)
                                    data_encrypt = modul.viginere_encrypt(str(text), str(key_caesar))
                                    st.success("Sukses")
                                    st.success(data_encrypt)
                                    modul.sender_email("Viginere dengan Key Caesar", str(st.session_state['login']),str(check_key[1]), str(to), str(subject), str(data_encrypt), str(number_encrypt), text)
                                else:
                                    st.warning("Setup Email Terlebih Dahulu !")

            else:
                st.markdown("<h3 align='center'>Enkripsi Chaesar Chipper & Viginere Chipper</h3>", unsafe_allow_html=True)
                buffer, col1, col2 = st.columns([2, 6, 2])
                with col1:
                    encryption_form = st.empty()
                    with encryption_form.form('Enkripsi'):
                        to = st.text_input("To", placeholder="example@gmail.com")
                        subject = st.text_input("Subject")
                        text = st.text_area("Body")
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
                                    data_encrypt = modul.encrypt_combined_chipper(str(text), str(number_encrypt))
                                    st.success("Sukses")
                                    st.success(data_encrypt)
                                    modul.sender_email("Combined Chipper (Caesar & Viginere)", str(st.session_state['login']),str(check_key[1]), str(to), str(subject), str(data_encrypt), number_encrypt, text)
                                else:
                                    st.warning("Setup Email Terlebih Dahulu !")

        else:
            if str(op) == "Caesar Chipper":
                st.markdown("<h3 align='center'>Dekripsi Chaesar Chipper</h3>", unsafe_allow_html=True)
                buffer, col1, col2 = st.columns([2, 6, 2])
                with col1:
                    decryption_form = st.empty()

                    with decryption_form.form('Dekripsi'):
                        text = st.text_area("Masukan Text")
                        number_encrypt = st.number_input('Key Number', step=1, min_value=1, max_value=25)
                        submit = st.form_submit_button("Dekripsi")

                        if submit:
                            if str(text) == "":
                                st.warning("Text tidak boleh kosong !")
                            
                            else:
                                st.success("Sukses")
                                data_encrypt = modul.caesar_decrypt(str(text), number_encrypt)
                                st.success(data_encrypt)

            elif str(op) == "Viginere Chipper":
                st.markdown("<h3 align='center'>Dekripsi Viginere Chipper</h3>", unsafe_allow_html=True)
                buffer, col1, col2 = st.columns([2, 6, 2])
                with col1:
                    decryption_form = st.empty()

                    with decryption_form.form('Dekripsi'):
                        text = st.text_area("Masukan Text")
                        enkripsi_number = st.text_input("Key Decryption")
                        submit = st.form_submit_button("Enkripsi")

                        if submit:
                            if str(text) == "":
                                st.warning("Text tidak boleh kosong !")
                            
                            else:
                                st.success("Sukses")
                                data_encrypt = modul.viginere_decrypt(str(text), str(enkripsi_number))
                                st.success(data_encrypt)
            
            elif str(op) == "Viginere dengan Key Caesar":
                st.markdown("<h3 align='center'>Dekripsi Viginere dengan Key Caesar</h3>", unsafe_allow_html=True)
                buffer, col1, col2 = st.columns([2, 6, 2])
                with col1:
                    decryption_form = st.empty()

                    with decryption_form.form('Dekripsi'):
                        text = st.text_area("Masukan Text")
                        enkripsi_number = st.text_input("Key Decryption")
                        submit = st.form_submit_button("Enkripsi")

                        if submit:
                            if str(text) == "":
                                st.warning("Text tidak boleh kosong !")
                            
                            else:
                                st.success("Sukses")
                                key_caesar = modul.caesar_encrypt(str(enkripsi_number), 3)
                                data_encrypt = modul.viginere_decrypt(str(text), str(key_caesar))
                                st.success(data_encrypt)

            else:
                st.markdown("<h3 align='center'>Dekripsi Chaesar Chipper & Viginere Chipper</h3>", unsafe_allow_html=True)
                buffer, col1, col2 = st.columns([2, 6, 2])
                with col1:
                    decryption_form = st.empty()

                    with decryption_form.form('Dekripsi'):
                        text = st.text_area("Masukan Text")
                        enkripsi_number = st.text_input("Key Decryption")
                        submit = st.form_submit_button("Enkripsi")

                        if submit:
                            if str(text) == "":
                                st.warning("Text tidak boleh kosong !")
                            
                            else:
                                st.success("Sukses")
                                data_encrypt = modul.decrypt_combined_chipper(str(text), str(enkripsi_number))
                                st.success(data_encrypt)

    elif selected == "Message Box":
        option_data = [
                {'label':"Inbox"},
                {'label':"Notification"}
            ]

        # override the theme, else it will use the Streamlit applied theme
        over_theme = {'txc_inactive': 'black','menu_background':'#eee','txc_active':'black','option_active':'#fafafa'}
        font_fmt = {'font-class':'h2','font-size':'150%'}

        # display a horizontal version of the option bar
        op = hc.option_bar(option_definition=option_data,key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

        if str(op) == "Notification":
            # Get Data From Database
            data =  modul.get_notification(str(st.session_state['login']))
            for i in range(len(data)):
                if str(data[i][5]) == 'Sender':
                    out = str(data[i][2]).replace('@gmail.com', '')
                    text = "Anda Mengirim Pesan ke {} pada Jam {}".format(out, data[i][4])
                    with st.expander(str(text)):
                        st.text_area(label = '', value=data[i][3], key=i)
                else:
                    if str(data[i][2]) == str(st.session_state['login']):
                        st.info(f"Anda Mendapatkan Pesan dari {data[i][1]} pada Jam {data[i][4]}")
        
        if str(op) == "Inbox":
            data =  modul.get_notification(str(st.session_state['login']))
            for i in range(len(data)):
                if str(data[i][5]) == "Receiver":
                    if str(data[i][2]) == str(st.session_state['login']):
                        inp = str(data[i][2]).replace('@gmail.com', '')
                        text = f"Anda Mendapatkan Pesan dari {inp} pada Jam {data[i][4]}"
                        with st.expander(str(text)):
                            st.text_area(label = '', value=data[i][3], key=i)


    elif selected == "Setup Email":
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
                st.warning("Note : Harus Menggunakan Email yang sama pada saat login sistem !")
                st.markdown("<p>Link : <a href='https://myaccount.google.com/apppasswords?rapt=AEjHL4NIjmy_-vtL7RcXyRnksDTxUbGll8i8UrXYD-jQKXoDab3FRHfG5MJL3MJfroNIK32MXQd1Nqnk4Urk27wJGe0OPf3qYg'>Klik disini<a></p>", unsafe_allow_html=True)
                generate_password = st.text_input("Generate Key", type='password')
                submit = st.form_submit_button("Send Key")

                if submit:
                    test_key = modul.send_key(str(st.session_state['login']), str(generate_password))

                    if test_key == True:
                        st.success("Berhasil Menginputkan Key !")
                    else:
                        st.warning("Gagal Menginputkan Key !")

    else:
        st.success("Berhasil Logout !")
        st.session_state['login'] = ''

