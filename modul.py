# pip install secure-smtplib
import smtplib
import smtplib
from email.message import EmailMessage

import string
import random
import sqlite3
import os
import time

import streamlit as st
import numpy as np
from datetime import datetime
import pytz
# Function


def sender_email(type, email, password, to, subject, text, key, real_text):
    # Variables containing your email address and password
    EMAIL_ADDRESS = str(email)
    EMAIL_PASSWORD = str(password)

    # Create an instance of the EmailMessage class
    msg = EmailMessage()
    # Define the 'Subject' of the email
    msg['Subject'] = str(subject)
    # Define 'From' (your email address)
    msg['From'] = EMAIL_ADDRESS
    # Define 'To' (to whom is it addressed)
    msg['To'] = str(to)
    # The email content (your message)
    if key != '':
        content_text = str(f"===== {str(type)} Encryption Email =====\n") + str(text) + str(
            f'\n Encryption Key : {key}') + str("\n===== Go To : https://cryptography-caesar-viginere-chipper.streamlit.app/")
    else:
        content_text = str(f"===== {str(type)} Encryption Email =====\n") + \
            str(text) + str("\n===== Go To : https://cryptography-caesar-viginere-chipper.streamlit.app/")

    msg.set_content(str(content_text))
    files = os.listdir('File/')
    if len(files) > 0:
        files = files[0]
        with open('File/' + str(files), 'rb') as attach:
            msg.add_attachment(attach.read(), maintype='application',
                               subtype='octet-stream', filename=attach.name)

    # Establishing a secure connection (SSL), login to your email account and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    files = os.listdir('File/')
    if len(files) > 0:
        path_file = os.path.join(os.getcwd(), 'File')
        files = os.listdir(path_file)[0]
        os.remove(os.path.join(path_file, files))

    # Send Database (Sender)
    sqliteConnection = sqlite3.connect('enkripsi.db')
    cursor = sqliteConnection.cursor()
    now = datetime.now(pytz.timezone('Asia/Jakarta'))

    sqlite_insert_query = f"""INSERT INTO sender
                            VALUES 
                            (?, ?, ?, ?, ?, ?);
                            """
    data_tuple = (np.nan, email, to, real_text,
                  now.strftime("%d/%m/%Y %H:%M:%S"), 'Sender')

    cursor.execute(sqlite_insert_query, data_tuple)
    sqliteConnection.commit()

    # Check Database Receiver
    data_valid = False
    statement = f"SELECT Email FROM akun WHERE Email='{email}';"
    row_count_admin = cursor.execute(statement)
    data_acount = cursor.fetchone()

    if not data_acount:
        data_valid = False
    else:
        data_valid = True

    if data_valid == True:
        # Insert Receiver
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()
        now = datetime.now(pytz.timezone('Asia/Jakarta'))

        sqlite_insert_query = f"""INSERT INTO sender
                                VALUES 
                                (?, ?, ?, ?, ?, ?);
                                """
        data_tuple = (np.nan, email, to, content_text,
                      now.strftime("%d/%m/%Y %H:%M:%S"), 'Receiver')

        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()

    cursor.close()


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


def caesar_decrypt(message, key):
    alpha = [chr(i) for i in range(65, 91)]
    beta = [chr(i) for i in range(97, 123)]
    simbol = [chr(i) for i in range(1, 48)] + [chr(i) for i in range(58, 65)] + [chr(i)
                                                                                 for i in range(91, 97)] + [chr(i) for i in range(123, 128)]
    simbol.remove(" ")
    number = [chr(i) for i in range(48, 58)]

    alpha = "".join(i for i in alpha)
    beta = "".join(i for i in beta)
    simbol = "".join(i for i in simbol)
    number = "".join(i for i in number)
    result = ""

    for letter in message:
        if letter in simbol:  # if the letter is actually a letter
            # find the corresponding ciphertext letter in the simbolbet
            letter_index = (simbol.find(letter) - key) % len(simbol)

            result = result + simbol[letter_index]

        elif letter in number:
            letter_index = (number.find(letter) - key) % len(number)

            result = result + number[letter_index]

        elif letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]

        elif letter in beta:
            letter_index = (beta.find(letter) - key) % len(beta)

            result = result + beta[letter_index]

        else:
            result = result + letter

    return result


def viginere_encrypt(plaintext, key):
    try:
        alpha = "".join(chr(i) for i in range(65, 91))
        beta = "".join(chr(i) for i in range(97, 123))
        plain_new = plaintext.upper()
        key = key.upper()
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plain_new]
        ciphertext = []
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            if str(plain_new[i]) == " ":
                ciphertext.append(" ")
            elif str(plaintext[i]) not in alpha and str(plaintext[i]) not in beta:
                ciphertext.append(plaintext[i])
            else:
                ciphertext.append(chr(value + 65))
        for i in range(len(plaintext)):
            if str(plaintext[i]).islower() == True:
                ciphertext[i] = str(ciphertext[i]).lower()
        # Generate Random Number and Symbol
        result = "".join(i for i in ciphertext)
        return result

    except Exception as eror:
        print(eror)


def viginere_decrypt(plaintext, key):
    try:
        alpha = "".join(chr(i) for i in range(65, 91))
        beta = "".join(chr(i) for i in range(97, 123))
        plain_new = plaintext.upper()
        key = key.upper()
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plain_new]
        ciphertext = []
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] - key_as_int[i % key_length]) % 26
            if str(plain_new[i]) == " ":
                ciphertext.append(" ")
            elif str(plaintext[i]) not in alpha and str(plaintext[i]) not in beta:
                ciphertext.append(plaintext[i])
            else:
                ciphertext.append(chr(value + 65))
        for i in range(len(plaintext)):
            if str(plaintext[i]).islower() == True:
                ciphertext[i] = str(ciphertext[i]).lower()
        # Generate Random Number and Symbol
        result = "".join(i for i in ciphertext)
        return result

    except Exception as eror:
        print(eror)


def encrypt_combined_chipper(message: str, key: str):
    # Encrypt Caesar Chipper
    key_caesar = 3
    alpha = "".join(chr(i) for i in range(65, 91))
    beta = "".join(chr(i) for i in range(97, 123))
    result = ""

    for letter in message:

        if letter in alpha:
            letter_index = (alpha.find(letter) + key_caesar) % len(alpha)

            result = result + alpha[letter_index]

        elif letter in beta:
            letter_index = (beta.find(letter) + key_caesar) % len(beta)

            result = result + beta[letter_index]

        else:
            result = result + letter

    result_caesar = result

    # Viginere Chippper
    return viginere_encrypt(result_caesar, str(key))


def decrypt_combined_chipper(cipher, key):
    data_viginere = viginere_decrypt(cipher, key)

    # Decrypt Caesar
    key_caesar = 3
    alpha = "".join(chr(i) for i in range(65, 91))
    beta = "".join(chr(i) for i in range(97, 123))
    result = ""

    for letter in data_viginere:

        if letter in alpha:
            letter_index = (alpha.find(letter) - key_caesar) % len(alpha)

            result = result + alpha[letter_index]

        elif letter in beta:
            letter_index = (beta.find(letter) - key_caesar) % len(beta)

            result = result + beta[letter_index]

        else:
            result = result + letter

    return result


def get_notification(email_inp):
    try:
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()
        statement = f"SELECT * from sender WHERE From_Subject = '{email_inp}' OR To_Subject= '{email_inp}';"
        cursor.execute(statement)
        rows = cursor.fetchall()
        data_empty = []
        for row in rows:
            data_empty.append(row)

        cursor.close()
        return data_empty

    except sqlite3.Error as error:
        st.error(error)
        return False


def signup(email_inp, nama_inp, password_inp):
    try:
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_query = """INSERT INTO akun
                               VALUES 
                              (?, ?, ?);
                              """
        data_tuple = (email_inp, nama_inp, password_inp)

        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()
        return True

    except sqlite3.Error as error:
        return False

    finally:
        if sqliteConnection:
            sqliteConnection.close()


def login(emai_inp, password_inp):
    try:
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()
        statement = f"SELECT Email FROM akun WHERE Email='{emai_inp}' AND Password = '{password_inp}';"
        row_count_admin = cursor.execute(statement)
        data_admin = cursor.fetchone()
        if not data_admin:
            cursor.close()
            return False
        else:
            cursor.close()
            return True

    except sqlite3.Error as error:
        return False

    finally:
        if sqliteConnection:
            sqliteConnection.close()


def send_key(email_inp, key_inp):
    try:
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_query = """INSERT INTO key
                               VALUES 
                              (?, ?);
                              """
        data_tuple = (email_inp, key_inp)

        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()
        return True

    except sqlite3.Error as error:
        return False

    finally:
        if sqliteConnection:
            sqliteConnection.close()


def check_key(email_inp):
    try:
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()
        statement = f"SELECT key FROM key WHERE Email='{email_inp}'"
        row_count_admin = cursor.execute(statement)
        data_admin = cursor.fetchone()
        if not data_admin:
            cursor.close()
            return False
        else:
            data_admin = data_admin[0]
            cursor.close()
            return [True, data_admin]

    except sqlite3.Error as error:
        return False

    finally:
        if sqliteConnection:
            sqliteConnection.close()
