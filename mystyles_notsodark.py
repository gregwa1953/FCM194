#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     mystyles_notsodark.py
#  ------------------------------------------------------
# Created for Learning PAGE
# Written by G.D. Walters
# Copyright © 2022, 2023  by G.D. Walters
# This source code is released under the MIT License
# ======================================================
# Version 2.05.7𝛽
# ======================================================
# Version history
#    Pre-2.0 proof of concept
#    2.02 - 29 November, 2022 - First Alpha release
#    2.03 - 29 November, 2022 - Changed globals to shared module
#    2.04 - 30 November, 2022 - Added Dark style, global color definitions
#    2.05 - 3 May, 2023 - fixed TEntry foreground and background colours
#    2.05.1 - 3 May, 2023 - Fixed TCombobox colours.
#               Added add_options function.  REQUIRES Toplevel to be passed as a parameter.
#    2.05.2 - 3 May, 2023 - Setup basic style for Treeview - subject to change
#    2.05.4𝛽 - 3 May, 2023 - Removed custom graphics from TCheckbutton and TRadiobutton
#    2.05.5𝛽 - 4 May, 2023 - Removed dead code
#    2.05.6𝛽 - 4 May, 2023 - Added Toolbutton style for TButton,
#                            Tweaked TSpinbox style,
#                            Tweaked Treeview style,
#                            Tweaked TMenubutton style,
#                            Added Global Toplevel color information
#    2.05.7𝛽 - 4 May, 2023 - Fixed TRadiobutton and TCheckbutton custom graphics
#    2.05.8𝛽 - 7 June, 2023 - Added support for tk_setPalette
#    2.05.9𝛽 - 9 June, 2023 - Modified some colours
# ======================================================
#  Still to do 3 May, 2023
# ------------------------------------------------------
# TLabel
# TButton Toolbutton
# TMenubutton
# Check AskFileOpen Dialog
# =======================================================
#  ttk Widgets currently supported 3 May, 2023
# -------------------------------------------------------
# Treeview
# TLabelframe
# TFrame
# TSpinbox
# TScale
# TProgressbar
# TRadiobutton
# TCheckbutton
# TEntry
# TCombobox
# TButton
# =======================================================

import sys
import shared
import tkinter as tk
import os.path

_script = sys.argv[0]
location = os.path.dirname(_script)
version = "2.05.9𝛽"
# ===================================================
# Global Color definitions
# ===================================================
_bgcolor = "#919191"
_fgcolor = "black"
_activebgcolor = "gray66"
_activefgcolor = "gray5"
_troughcolor = "gray43"
_barcolor = "gray82"
_darkcolor = _bgcolor
_lightcolor = _fgcolor
_disabledcolor = "gray42"
_disabledfgcolor = "gray3"
_fieldbgcolor = "gray20"
_fieldfgcolor = "gray79"
_bordercolor = "dimgray"
_tvwindow = "lightgoldenrod3"
_tvwindowdisabled = "peachpuff3"
_selectbackground = "#93ba45"
_selectforeground = "black"
_highlightBackground = _bgcolor
_highlightColor = "black"
_InsertBackground = "black"
_selectColor = "#93ba45"


def create_styles(sty):
    # ===================================================
    # Apply a "generic" Toplevel style
    # ===================================================
    # sty.configure(
    #     ".",
    #     bgcolor=_bgcolor,
    #     fgcolor=_fgcolor,
    #     activebgcolor=_activebgcolor,
    #     activefgcolor=_activefgcolor,
    #     troughcolor=_troughcolor,
    #     barcolor=_barcolor,
    #     _darkcolor=_bgcolor,
    #     _lightcolor=_fgcolor,
    #     disabledcolor=_disabledcolor,
    #     disabledfgcolor=_disabledfgcolor,
    #     fieldbgcolor=_fieldbgcolor,
    #     fieldfgcolor=_fieldfgcolor,
    #     bordercolor=_bordercolor,
    #     tvwindow=_tvwindow,
    #     tvwindowdisabled=_tvwindowdisabled,
    #     selectbackground=_selectbackground,
    #     selectforeground=_selectforeground,
    #     highlightBackground=_bgcolor,
    #     highlightColor=_highlightColor,
    #     InsertBackground=_InsertBackground,
    #     selectColor=_selectColor,
    # )
    sty.map(
        ".",
        background=[("disabled", _disabledcolor), ("active", _activebgcolor)],
        foreground=[("disabled", _disabledfgcolor)],
        selectbackground=[("!focus", _selectbackground)],
        selectforeground=[("!focus", "white")],
        embossed=[("disabled", 1)],
    )
    # ===================================================
    # Style for ALL TLabel widgets
    # ===================================================
    sty.configure(
        "TLable",
        background=_bgcolor,
        foreground="black",
        font="Ubuntu 9 bold",
    )
    # ===================================================
    # Style for ALL TButton widgets
    # ===================================================
    sty.map(
        "TButton",
        background=[("disabled", "#d9d9d9"), ("active", _activebgcolor)],
        foreground=[("disabled", _disabledfgcolor), ("active", _activefgcolor)],
    )
    sty.configure(
        "TButton",
        foreground=_fgcolor,
        background=_bgcolor,
        padding=[4, 4, 4, 4],
        font="Ubuntu 12 bold",
    )
    # ===================================================
    # Style for Exit button
    # ===================================================
    sty.configure(
        "Custom.TButton",
        foreground=_fgcolor,
        background=_bgcolor,
        pading=[10, 10, 10, 10],
        font="Veranda 12 bold",
    )
    sty.map(
        "Custom.TButton",
        background=[("disabled", "#d9d9d9"), ("active", _activebgcolor)],
        foreground=[("disabled", "snow"), ("active", _activefgcolor)],
    )

    sty.configure(
        "Toolbutton",
        anchor="center",
        background=_bgcolor,
        foreground=_fgcolor,
        relief="flat",
        highlightcolor=_bordercolor,
        shiftrelief=2,
        highlightthickness=2,
        padding=2,
        font="Veranda 12 bold",
    )
    sty.map(
        "Toolbutton",
        background=[
            ("disabled", _bgcolor),
            ("active", "gray49"),
            ("selected", _tvwindow),
        ],
        foreground=[("disabled", _disabledfgcolor), ("active", _activefgcolor)],
    )

    # ===================================================
    # Style for ALL TCheckbutton
    # ===================================================
    shared.con_image = tk.PhotoImage(
        file=os.path.join(location, "Assets", "chk24x16.png")
    )
    shared.coff_image = tk.PhotoImage(
        file=os.path.join(location, "Assets", "unchk24x16.png")
    )
    shared.cdis_image = tk.PhotoImage(
        file=os.path.join(location, "Assets", "blank24x16.png")
    )
    sty.element_create(
        "custom.CBindicator",
        "image",
        shared.coff_image,
        ("selected", shared.con_image),
        ("disabled", shared.cdis_image),
    )
    sty.configure(
        "TCheckbutton",
        background=_bgcolor,
        foreground=_fgcolor,
        indicatormargin=[6, 6, 6, 6],
        padding=[6, 6, 6, 6],
        font="Ubuntu 12 bold",
    )
    sty.layout(
        "TCheckbutton",
        [
            (
                "Checkbutton.padding",
                {
                    "sticky": "nswe",
                    "children": [
                        ("custom.CBindicator", {"side": "left", "sticky": ""}),
                        (
                            "Checkbutton.focus",
                            {
                                "side": "left",
                                "sticky": "e",
                                "children": [("Checkbutton.label", {"sticky": "nse"})],
                            },
                        ),
                    ],
                },
            )
        ],
    )
    sty.map(
        "TCheckbutton",
        background=[
            ("disabled", _bgcolor),
            ("pressed", _activebgcolor),
            ("active", _activebgcolor),
            ("hover", _activebgcolor),
            # ("selected", tvwindow),
        ],
        foreground=[
            ("disabled", _disabledfgcolor),
            ("pressed", _activefgcolor),
            ("active", _activefgcolor),
            ("hover", _activefgcolor),
        ],
    )

    # ===================================================
    # Style for ALL TRadiobuttons
    # ===================================================
    shared.Ron_image = tk.PhotoImage(
        file=os.path.join(location, "Assets", "RadioSelected24x16.png")
    )
    shared.Roff_image = tk.PhotoImage(
        file=os.path.join(location, "Assets", "RadioUnSelected24x16.png")
    )
    shared.Rdis_image = tk.PhotoImage(
        file=os.path.join(location, "Assets", "blank24x16.png")
    )
    sty.element_create(
        "custom.indicator",
        "image",
        shared.Roff_image,
        ("selected", shared.Ron_image),
        ("disabled", shared.Rdis_image),
    )
    sty.configure(
        "TRadiobutton",
        background=_bgcolor,
        foreground=_fgcolor,
        indicatormargin=[6, 6, 6, 6],
        padding=[6, 6, 6, 6],
        font="Ubuntu 12 bold",
    )
    sty.layout(
        "TRadiobutton",
        [
            (
                "Radiobutton.padding",
                {
                    "sticky": "nswe",
                    "children": [
                        ("custom.indicator", {"side": "left", "sticky": ""}),
                        (
                            "Radiobutton.focus",
                            {
                                "side": "left",
                                "sticky": "",
                                "children": [("Radiobutton.label", {"sticky": "nswe"})],
                            },
                        ),
                    ],
                },
            )
        ],
    )
    sty.map(
        "TRadiobutton",
        background=[
            ("disabled", _bgcolor),
            ("pressed", _activebgcolor),
            ("active", _activebgcolor),
            ("hover", _activebgcolor),
            # ("selected", "springgreen3"),
        ],
        foreground=[
            ("disabled", _disabledfgcolor),
            ("pressed", _activefgcolor),
            ("active", _activefgcolor),
            ("hover", _activefgcolor),
        ],
    )

    # ===================================================
    # Style for ALL TProgressbars
    # ===================================================

    sty.configure(
        "bar.Horizontal.TProgressbar",
        troughcolor=_troughcolor,
        bordercolor=_troughcolor,
        background=_barcolor,
        lightcolor=_barcolor,
        darkcolor=_barcolor,
    )

    # ===================================================
    # Style for TCombobox (in progress)
    # ===================================================
    sty.configure(
        "TCombobox",
        background=_activebgcolor,
        foreground="black",
        fieldbackground=_tvwindow,
        fieldforeground="black",
        arrowcolor="black",
    )
    sty.configure(
        "ComboboxPopdownFrame",
        background=_bgcolor,
        foreground=_fgcolor,
        fieldbackground=_tvwindow,
        fieldforeground="black",
        borderwidth=2,
        relief="sunken",
    )

    # ===================================================
    # Style for ALL TScale widgets
    # ===================================================

    sty.configure(
        "bar.Horizontal.TScale",
        troughcolor=_troughcolor,
        bordercolor=_troughcolor,
        background=_barcolor,
        lightcolor=_barcolor,
        darkcolor=_barcolor,
    )
    # ===================================================
    # Style for ALL TSpinbox Widgets
    # ===================================================
    sty.configure(
        "TSpinbox",
        arrowsize=11,
        bordercolor=_bordercolor,
        background=_activebgcolor,
        foreground="black",
        lightcolor=_lightcolor,
        darkcolor=_darkcolor,
        selectbackground="springgreen2",
        selectforeground="black",
        fieldbackground=_tvwindow,
        fieldforeground="black",
        arrowcolor="black",
    )

    # ===================================================
    # Style for ALL TEntry widgets
    # ===================================================
    sty.configure("TEntry", foreground="black", fieldbackground=_tvwindow)

    # ===================================================
    # Style for ALL TFrame widgets
    # ===================================================
    sty.configure("TFrame", background=_bgcolor, relief=tk.GROOVE, borderwidth=2)

    # ===================================================
    # Style for ALL TLabelframe widgets
    # ===================================================
    sty.configure(
        "TLabelframe",
        background=_bgcolor,
        bordercolor=_bordercolor,
        borderwidth=3,
        darkcolor=_darkcolor,
        labelmargins=10,
        labeloutside=False,
        lightcolor=_lightcolor,
        relief=tk.GROOVE,
    )
    sty.configure(
        "TLabelframe.Label",
        font=("Ubuntu 10 bold"),
        foreground=_fgcolor,
        background=_bgcolor,
        padding=[12, 6],
    )

    # ===================================================
    # Style for ALL ScrolledTreeview widgets
    # ===================================================
    sty.configure(
        "Treeview",
        background=_tvwindow,
        foreground="black",
        selected=_selectbackground,
        fieldbackground=_tvwindow,
        # fieldforeground="black",
        font="Ubuntu 11 bold",
    )
    sty.configure(
        "heading", relief="sunken", background=_bgcolor, font="Ubuntu 11 bold"
    )
    sty.configure("item", foreground="black", padding=[3, 3])
    sty.configure("cell", padding=[6, 6])
    # ===================================================
    # Style for ALL TMenuButton
    # ===================================================
    sty.configure(
        "TMenubutton",
        background=_bgcolor,
        foreground=_fgcolor,
        width=25,
        padding=2,
        relief="raised",
        font="Ubuntu 9 bold",
    )

    # ===================================================
    # Style for ALL TPanedwindow
    # ===================================================
    sty.configure("TPanedwindow", background=_bgcolor)
    sty.configure(
        "Sash",
        background=_troughcolor,
        bordercolor=_bordercolor,
        lightcolor=_bordercolor,
        handlepad=10,
        handlesize=5,
        sashpad=12,
        sashthickness=8,
        gripcount=10,
    )

    # ===================================================
    # Style for ALL TScrollbars
    # ===================================================
    sty.configure("TScrollbar", gripcount=10)


def add_options(toplevel):
    toplevel.option_add("*TCombobox*Listbox*Background", _tvwindow)
    toplevel.option_add("*TCombobox*Listbox*Foreground", "black")
    toplevel.option_add("*TCombobox*Listbox*selectBackground", _selectbackground)
    toplevel.option_add("*TCombobox*Listbox*selectForeground", _selectforeground)
    toplevel.option_add("TkFDialog*Foreground", "black")
    toplevel.option_add("TkChooseDir*Foreground", "black")


def set_palette(toplevel):
    # https://www.tcl-lang.org/man/tcl8.6/TkCmd/palette.htm
    toplevel.tk_setPalette(
        activeBackground=_activebgcolor,
        activeForeground=_activefgcolor,
        background=_bgcolor,
        disabledForeground=_disabledfgcolor,
        foreground=_fgcolor,
        highlightBackground=_bgcolor,
        highlightColor=_fgcolor,
        InsertBackground=_fgcolor,
        selectColor=_selectbackground,
        selectBackground=_selectbackground,
        selectForeground=_selectforeground,
    )


def reset_palette(toplevel):
    # https://www.tcl-lang.org/man/tcl8.6/TkCmd/palette.htm
    toplevel.tk_setPalette(
        activeBackground="#c3c3c3",
        activeForeground="black",
        background="#d9d9d9",
        disabledForeground="gray40",
        foreground="black",
        highlightBackground="#d9d9d9",
        highlightColor="black",
        InsertBackground="black",
        selectColor="#c4c4c4",
        selectBackground="#c4c4c4",
        selectForeground="black",
    )


def get_version():
    print(f"{version=}")
