#!/usr/bin/env python3
# coding = utf-8

# This File
# Craig Miles: -> trocoxijaxe@gmail.com

# 25:50

import os
import logging
import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk

os.chdir( os.path.dirname( __file__ ))  # Change directory to this file's location

logging.basicConfig( filename = 'Login.log',
                     level = logging.INFO,
                     format = '%(asctime)s - %(levelname)s - %(message)s',
                     datefmt = '%Y-%B-%d %H:%M:%S' )

class Login( customtkinter.CTk ):
    def __init__( self ):
        super().__init__()
        self.geometry( '930x478' )
        self.title( 'Login Page' )
        self.resizable( width = False, height = False )
        self.configure( fg_color = '#111119' ) #45087b
        self.center_root()
        self.create_fonts()
        self.create_root_icon()
        self.create_background()
        self.create_entry_fields()
        self.create_login_button()
        self.create_back_button()

    def create_fonts( self ):
        self.id_font = customtkinter.CTkFont( family = 'Asul',
                                              size = 25,
                                              weight = 'bold' )

        self.heading_font = customtkinter.CTkFont( family = 'Cormorant Upright', #'Liberation Serif'
                                               size = 35,
                                               weight = 'bold' )

        self.ent_font = customtkinter.CTkFont( family = 'Liberation Serif',
                                               size = 25,
                                               weight = 'bold' )

        self.label_font = customtkinter.CTkFont( family = 'Chivo', #'Hack',
                                                 size = 45,
                                                 weight = 'normal' )

        self.title_font = customtkinter.CTkFont( family = 'Yatra One',
                                                 size = 15,
                                                 weight = 'normal' )

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

    def create_root_icon( self ):
        self.ximage = Image.open( os.path.join( 'images/login-24.png'))
        self.icn_image = ImageTk.PhotoImage( self.ximage )
        self.iconphoto( True, self.icn_image )

    def create_background( self ):
        img = customtkinter.CTkImage(
            Image.open( os.path.join(
               'images/earthday.png' )), size = ( 930, 478 ))
        img_lbl = customtkinter.CTkLabel( self, image = img, text = '' )
        img_lbl.place( x = 0, y = 0 )

    def create_entry_fields( self ):
        self.uname = customtkinter.CTkEntry( self,
                                             font = self.id_font,
                                             fg_color = '#90599a',
                                             text_color = '#e4b114',
                                             justify = customtkinter.CENTER,
                                             width = 275,
                                             placeholder_text = 'Enter Your Username')
        self.uname.place( x = 90, y = 240 )
        self.pword = customtkinter.CTkEntry( self,
                                             font = self.id_font,
                                             fg_color = '#90599a',
                                             text_color = '#e4b114',
                                             justify = customtkinter.CENTER,
                                             width = 275,
                                             placeholder_text = 'Enter Your Password',
                                             show = '*' )
        self.pword.place( x = 90, y = 290 )

    def create_login_button( self ):
        self.btn_login = customtkinter.CTkButton( self,
                                                  font = self.id_font,
                                                  fg_color = '#e7b636',
                                                  text_color = '#361f40',
                                                  text = 'Login',
                                                  width = 275,
                                                  command = self.login_callback )
        self.btn_login.place( x = 90, y = 340 )

    def create_back_button( self ):
        self.btn_back = customtkinter.CTkButton( self,
                                                 font = self.id_font,
                                                 fg_color = '#e7b636',
                                                 text_color = '#361f40',
                                                 text = 'Back To Welcome',
                                                 width = 275,
                                                 command = self.back_to_welcome )
        self.btn_back.place( x = 90, y = 390 )

    def clear_login( self ):
        self.uname.delete( 0, customtkinter.END )
        self.pword.delete( 0, customtkinter.END )
        self.uname.focus()

    def login_callback( self ):
        if self.uname.get() == '' or self.pword.get() == '':
            msg = CTkMessagebox( title = 'Error',
                      message = 'All Fields Are Required!',
                          icon = 'cancel',
                              option_1 = 'OK' )
            if msg.get() == 'OK':
                self.clear_login()

        elif self.uname.get() == 'miles' and self.pword.get() == '1234':
            msg = CTkMessagebox( title = 'Success',
                      message = 'Login Was Successfull!',
                          icon = 'check',
                              option_1 = 'OK' )
            if msg.get() == 'OK':
                self.clear_login()
                self.destroy()
                from welcome import WelcomeWindow
                WelcomeWindow()

        else:
            msg = CTkMessagebox( title = 'Error',
                      message = 'Wrong Credentials',
                          icon = 'cancel',
                              option_1 = 'OK' )
            if msg.get() == 'OK':
                self.clear_login()

        logging.info( 'Just Testing login callback' )

#=============================================================================

    def back_to_welcome( self ):
        from welcome import WelcomeWindow
        self.destroy()
        WelcomeWindow()

#=============================================================================

if __name__ == '__main__':
     app = Login()
     app.mainloop()
