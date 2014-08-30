#!/usr/bin/env python26

import sqlite3
import sys
import time
from color import *


class AddressBook(object):
    def __init__(self):
        self.conn = sqlite3.connect('address_book.db')

    def displayUserMenu(self):
        try:
            print("=======Address Book=========")
            print("1. Add data")
            print("2. Delete data")
            print("3. Get list of data")
            print("4. Edit data")

            while True:
                option = raw_input("Choose your option:")
                 
                if(int(option) > 3 or int(option) < 1):
                    raise ValueError("Please choose right number from list!")
                    continue
                else:
                    return option
                    break
        except Exception as e:
            print "Error is %s" % (e)

    def lastChoice(self):
        color_me = getColor()
        while True:
            last_choice = raw_input("Do you want to do something else?(Yes/No)")
            if(last_choice == 'Yes' or last_choice == 'yes'):
                self.main()

            elif(last_choice == 'No' or last_choice == "no"):
                print "Closing database connection..."
                time.sleep(4)
                print color_me.greenText("[OK!]")
                print "Exiting...."
                time.sleep(3)
                self.conn.close()
                sys.exit(0)
            else:
                print "Choose yes or no!"
                continue

    def createAddressTable(self):
        
        self.conn.execute('''CREATE TABLE IF NOT EXISTS "Address_book" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        "Username" TEXT NOT NULL, 
        "Surname" TEXT NOT NULL, 
        "Phone" INTEGER NOT NULL);''')
        
    def addDataToTable(self, username, surname, phone):
        try:
            self.conn.execute("INSERT INTO ADDRESS_BOOK (USERNAME,SURNAME,PHONE) \
                VALUES (?, ?, ?)", (username, surname, phone));

            self.conn.commit()
            print "Records added successfully!"
        except Exception as e:
            print "Error is %s" % (e)

    def getAllData(self):
        
        cursor = self.conn.execute("SELECT id,username, surname, phone  from ADDRESS_BOOK")
        for row in cursor:
            print "Id = %s, Username = %s, Surname = %s, Phone = %s" % (row[0], row[1], row[2], row[3])

        if(cursor == ''):
            print "There is no data on your database!"

    def getUserDataFromShell(self):

        while True:
            try:
                username = raw_input("Input users name:")
            
                if(len(username) > 10):
                    print "Username is too long!"
                    raise ValueError("This number is too long, try again!")
                elif(len(username) < 10):
                    continue
            except ValueError as e:
                print "Error is %s" % (e)

            #surname = raw_input("Input users surname:")
            #phone = raw_input("Input users phone:")

       
        
        self.addDataToTable(username, surname, phone)

    def main(self):

        menu = self.displayUserMenu()
        if(menu == '1'):
            self.createAddressTable()
            self.getUserDataFromShell()
            self.lastChoice()
        elif(menu == '3'):
            self.getAllData()
            self.lastChoice()

address_book = AddressBook()
address_book.main()

