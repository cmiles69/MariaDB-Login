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
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from login import Login
from registration import RegistrationWindow

os.chdir( os.path.dirname( __file__ ))  # Change directory to this file's location

logging.basicConfig( filename = 'Welcome.log',
                     level = logging.INFO,
                     format = '%(asctime)s - %(levelname)s - %(message)s',
                     datefmt = '%Y-%B-%d %H:%M:%S' )

class WelcomeWindow( customtkinter.CTk ):
    def __init__( self ):
        super().__init__()
        self.geometry( '600x478' )
        self.title( 'Welcome To MariaDB' )
        self.resizable( width = False, height = False )
        self.configure( fg_color = '#00EEFF' )
        self.center_root()
        self.create_fonts()
        self.create_root_icon()
        self.create_background()
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

            self.label_font = customtkinter.CTkFont( family = 'Chivo', #'Hack',
                                                     size = 45,
                                                     weight = 'normal' )

            self.title_font = customtkinter.CTkFont( family = 'Yatra One',
                                                     size = 15,
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
        self.ximage = Image.open( os.path.join( 'images/welcome-24.png'))
        self.icn_image = ImageTk.PhotoImage( self.ximage )
        self.iconphoto( True, self.icn_image )

#=============================================================================

    def create_background( self ):
        img = customtkinter.CTkImage(
            Image.open( os.path.join( 'images/welcome_background_3.jpg' )),
            size = ( 600, 478 ))
        img_lbl = customtkinter.CTkLabel( self, image = img, text = '' )
        img_lbl.place( x = 0, y = 0 )

#=============================================================================

    def create_buttons( self ):
        self.btn_login = customtkinter.CTkButton( self,
                                                  font = self.login_font,
                                                  fg_color = '#00EDFF',
                                                  text_color = '#361f40',
                                                  border_color = '#DAB38A',
                                                  text = 'Login',
                                                  width = 240,
                                                  corner_radius = 10,
                                                  command = self.open_login_window )
        self.btn_login.place( x = 30, y = 430 )

        self.btn_register = customtkinter.CTkButton( self,
                                                     font = self.login_font,
                                                     fg_color = '#00EDFF',
                                                     text_color = '#361f40',
                                                     border_color = '#DAB38A',
                                                     text = 'Register',
                                                     width = 240,
                                                     corner_radius = 10,
                                                     command = self.open_register_window )
        self.btn_register.place( x = 330, y = 430 )

#=============================================================================

    def open_login_window( self ):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        Login()

#=============================================================================

    def open_register_window( self ):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        RegistrationWindow()

#=============================================================================


if __name__ == '__main__':
     app = WelcomeWindow()
     app.mainloop()
