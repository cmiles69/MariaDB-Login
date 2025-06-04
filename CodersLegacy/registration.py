#!/usr/bin/env python3
# coding = utf-8

# Original Credit: coderslegacy.com
# https://coderslegacy.com/python-tkinter-project-with-mysql-database/
# https://www.youtube.com/watch?v=SOU4TubaDf0

# This File
# Craig Miles: -> trocoxijaxe@gmail.com

import os
import customtkinter
import logging
import pprint
import database
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk

os.chdir( os.path.dirname( __file__ ))  # Change directory to this file's location

logging.basicConfig( filename = 'Registration.log',
                     level = logging.INFO,
                     format = '%(asctime)s - %(levelname)s - %(message)s',
                     datefmt = '%Y-%B-%d %H:%M:%S' )

class RegistrationWindow( customtkinter.CTk ):
    def __init__( self ):
        super().__init__()
        self.geometry( '1000x600' )
        self.title( 'Registration Information For MariaDB' )
        self.resizable( width = False, height = False )
        self.configure( fg_color = '#00EEFF' )
        self.center_root()
        self.create_fonts()
        self.create_root_icon()
        self.create_background()
        self.create_entry_fields()
        self.create_buttons()

#=============================================================================

    def create_fonts( self ):
            self.login_font = customtkinter.CTkFont( family = 'Asul',
                                                     size = 25,
                                                     weight = 'bold' )

            self.heading_font = customtkinter.CTkFont( family = 'Cormorant Upright', #'Liberation Serif'
                                                       size = 35,
                                                       weight = 'bold' )

            self.ent_font = customtkinter.CTkFont( family = 'Liberation Serif',
                                                   size = 25,
                                                   weight = 'bold' )

            self.tmp_font = customtkinter.CTkFont( family = 'Chivo', #'Hack',
                                                            size = 25,
                                                            weight = 'normal' )

            self.registration_font = customtkinter.CTkFont( family = 'Yatra One',
                                                            size = 25,
                                                            weight = 'normal' )

#=============================================================================

    def center_root( self ):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        pos_right = \
        int( self.winfo_screenwidth() // 2 - window_width // 2 )
        pos_down = \
        int( self.winfo_screenheight() // 2 - window_height // 2 )
        self.geometry( '{}x{}+{}+{}'
        .format( window_width, window_height, pos_right, pos_down ))

#=============================================================================

    def create_root_icon( self ):
        self.ximage = Image.open( os.path.join( 'images/registration_root_icon-24.png'))
        self.icn_image = ImageTk.PhotoImage( self.ximage )
        self.iconphoto( True, self.icn_image )

#=============================================================================

    def create_background( self ):
        img = customtkinter.CTkImage(
            Image.open( os.path.join( 'images/registration_background.jpg' )),
            size = ( 1000, 600 ))
        img_lbl = customtkinter.CTkLabel( self, image = img, text = '' )
        img_lbl.place( x = 0, y = 0 )

#=============================================================================

    def create_entry_fields( self ):
        self.firstname_ent = customtkinter.CTkEntry( self,
                                                     font = self.registration_font,
                                                     fg_color = '#90599a',
                                                     text_color = '#e4b114',
                                                     justify = customtkinter.CENTER,
                                                     width = 345,
                                                     placeholder_text = 'Enter Your First Name')
        self.firstname_ent.place( x = 30, y = 30 )

        self.lastname_ent = customtkinter.CTkEntry( self,
                                                    font = self.registration_font,
                                                    fg_color = '#90599a',
                                                    text_color = '#e4b114',
                                                    justify = customtkinter.CENTER,
                                                    width = 345,
                                                    placeholder_text = 'Enter Your Last Name')
        self.lastname_ent.place( x = 30, y = 80 )

        self.password_ent = customtkinter.CTkEntry( self,
                                                    font = self.registration_font,
                                                    fg_color = '#90599a',
                                                    text_color = '#e4b114',
                                                    justify = customtkinter.CENTER,
                                                    width = 345,
                                                    placeholder_text = 'Enter Your Password',
                                                    show = '*' )
        self.password_ent.place( x = 30, y = 130 )

        self.email_ent = customtkinter.CTkEntry( self,
                                                 font = self.registration_font,
                                                 fg_color = '#90599a',
                                                 text_color = '#e4b114',
                                                 justify = customtkinter.CENTER,
                                                 width = 345,
                                                 placeholder_text = 'Enter Your Email Address')
        self.email_ent.place( x = 30, y = 180 )

        self.gender_lbl = customtkinter.CTkLabel( master = self,
                                                  font = ( 'Mono', 25 ),
                                                  fg_color = '#90599a',
                                                  text_color = '#e4b114',
                                                  text = 'Select Your Gender:' )
        self.gender_lbl.place( x = 400, y = 35 )

        self.gender_options = ['','Male', 'Female' ]

        self.gender_cbx = customtkinter.CTkComboBox( self,
                                        font = self.registration_font,
                                        fg_color = '#90599a',
                                        text_color = '#e4b114',
                                        dropdown_fg_color = '#90599a',
                                        dropdown_font = ( 'Mono', 25 ),
                                        justify = customtkinter.CENTER,
                                        width = 190,
                                        values = self.gender_options,
                                        state = 'readonly' )
        self.gender_cbx.place( x = 708, y = 32 )

        self.age_ent = customtkinter.CTkEntry( self,
                                               font = self.registration_font,
                                               fg_color = '#90599a',
                                               text_color = '#e4b114',
                                               justify = customtkinter.CENTER,
                                               width = 286,
                                               placeholder_text = 'Enter Your Age')
        self.age_ent.place( x = 400, y = 77 )

        self.address_tbox = customtkinter.CTkTextbox( self,
                                                      font = self.registration_font,
                                                      wrap = 'word',
                                                      fg_color = '#90599a',
                                                      text_color = '#e4b114',
                                                      width = 500,
                                                      height = 95 )
        self.address_tbox.place( x = 400, y = 130 )

        self.address_lbl = customtkinter.CTkLabel( master = self,
                                                   font = ( 'Mono', 25 ),
                                                   fg_color = '#90599a',
                                                   text_color = '#e4b114',
                                                   width = 190,
                                                   text = 'Address:' )
        self.address_lbl.place( x = 708, y = 82 )

#=============================================================================

    def back_to_welcome( self ):
        from welcome import WelcomeWindow
        self.destroy()
        WelcomeWindow()

#=============================================================================

    def registration_submit( self ):
        data = {}
        data['firstname'] = self.firstname_ent.get()
        data['lasttname'] = self.lastname_ent.get()
        data['pword'] = self.password_ent.get()
        data['email'] = self.email_ent.get()
        data['gender'] = self.gender_cbx.get()
        data['age'] = self.age_ent.get()
        data['address'] = self.address_tbox.get( 1.0, customtkinter.END )

        #pprint.pp( 'Data is ->', data )

        #conn, cursor = database.initialize_connection( prepared = True )

        conn, cursor = database.initialize_connection()

        self.registration_insert( conn, cursor, data )

        pprint.pp( data )

#=============================================================================

    def registration_insert( self, conn, cursor, data ):
        # cursor.executemany( '''INSERT IGNORE INTO users( firstname,
                                                         # lastname,
                                                         # pword,
                                                         # email,
                                                         # gender,
                                                         # age,
                                                         # address )
                               # VALUES( ?, ?, ?, ?, ?, ?, ? )''', ( data, ))
        # conn.commit()

        sql_insert_query = '''INSERT IGNORE INTO users( firstname,
                                                        lastname,
                                                        pword,
                                                        email,
                                                        gender,
                                                        age,
                                                        address )
                               VALUES( ?, ?, ?, ?, ?, ?, ? )'''

        data_insert = ( data['firstname'],
                        data['lasttname'],
                        data['pword'],
                        data['email'],
                        data['gender'],
                        data['age'],
                        data['address'] )

        cursor.execute( sql_insert_query, data_insert )
        conn.commit()

        if cursor.lastrowid:
            logging.info( 'Inserting User Into Database --> {0}'.format( data ))
            msg = CTkMessagebox( title = 'Information',
                                 message = 'Successfull Insertion {0}'.format( data ),
                                 icon = 'check', option_1 = 'OK', option_2 = 'Cancel' )
            if msg.get() == 'OK':
                self.back_to_welcome()
            else:
                return



    def create_buttons( self ):
        self.back_btn = customtkinter.CTkButton( master = self,
                                                 font = self.login_font,
                                                 text = 'Back To Welcome',
                                                 cursor = 'hand2',
                                                 fg_color = 'green3',
                                                 hover_color = 'gold',
                                                 text_color = 'black',
                                                 width = 200,
                                                 command = self.back_to_welcome )
        self.back_btn.place( x = 30, y = 520 )

        self.register_btn = customtkinter.CTkButton( master = self,
                                                     font = self.login_font,                                                     text = 'Submit Regististration',
                                                     cursor = 'hand2',
                                                     fg_color = 'mediumorchid1',
                                                     hover_color = 'sea green',
                                                     text_color = 'black',
                                                     width = 200,
                                                     command = self.registration_submit )
        self.register_btn.place( x = 620, y = 520 )

#=============================================================================


if __name__ == '__main__':
     app = RegistrationWindow()
     app.mainloop()

