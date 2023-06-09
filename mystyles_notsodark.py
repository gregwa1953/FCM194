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
version = "2.05.7𝛽"
# ===================================================
# Global Color definitions
# ===================================================
bgcolor = "#919191"
fgcolor = "black"
activebgcolor = "gray66"
activefgcolor = "gray5"
troughcolor = "gray43"
barcolor = "gray82"
_darkcolor = bgcolor
_lightcolor = fgcolor
disabledcolor = "gray42"
disabledfgcolor = "gray3"
fieldbgcolor = "gray20"
fieldfgcolor = "gray79"
_bordercolor = "dimgray"
tvwindow = "lightgoldenrod3"
tvwindowdisabled = "peachpuff3"
selectbackground = "#93ba45"
selectforeground = "black"


def create_styles(sty, imgpath):
    # sty.configure(
    #     "Formatted.TLabel",
    #     font="Ubuntu 12 bold",
    #     # anchor=tk.CENTER,
    #     background=bgcolor,
    #     foreground=fgcolor,
    # )
    # ===================================================
    # Apply a "generic" Toplevel style
    # ===================================================
    sty.configure(
        ".",
        bgcolor="#919191",
        fgcolor="black",
        activebgcolor="gray66",
        activefgcolor="gray5",
        troughcolor="gray43",
        barcolor="gray82",
        _darkcolor=bgcolor,
        _lightcolor=fgcolor,
        disabledcolor="gray42",
        disabledfgcolor="gray3",
        fieldbgcolor="gray20",
        fieldfgcolor="gray79",
        _bordercolor="dimgray",
        tvwindow="lightgoldenrod3",
        tvwindowdisabled="peachpuff3",
        selectbackground="#93ba45",
        selectforeground="black",
    )
    sty.map(
        ".",
        background=[("disabled", disabledcolor), ("active", activebgcolor)],
        foreground=[("disabled", disabledfgcolor)],
        selectbackground=[("!focus", selectbackground)],
        selectforeground=[("!focus", "white")],
        embossed=[("disabled", 1)],
    )
    # ===================================================
    # Style for ALL TLabel widgets
    # ===================================================
    sty.configure(
        "TLable",
        background=bgcolor,
        foreground="black",
        font="Ubuntu 9 bold",
    )
    # ===================================================
    # Style for ALL TButton widgets
    # ===================================================
    sty.map(
        "TButton",
        background=[("disabled", "#d9d9d9"), ("active", activebgcolor)],
        foreground=[("disabled", disabledfgcolor), ("active", activefgcolor)],
    )
    sty.configure(
        "TButton",
        foreground=fgcolor,
        background=bgcolor,
        padding=[4, 4, 4, 4],
        font="Ubuntu 12 bold",
    )
    # ===================================================
    # Style for Exit button
    # ===================================================
    sty.configure(
        "Custom.TButton",
        foreground=fgcolor,
        background=bgcolor,
        pading=[10, 10, 10, 10],
        font="Veranda 12 bold",
    )
    sty.map(
        "Custom.TButton",
        background=[("disabled", "#d9d9d9"), ("active", activebgcolor)],
        foreground=[("disabled", "snow"), ("active", activefgcolor)],
    )

    sty.configure(
        "Toolbutton",
        anchor="center",
        background=bgcolor,
        foreground=fgcolor,
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
            ("disabled", bgcolor),
            ("active", "gray49"),
            ("selected", tvwindow),
        ],
        foreground=[("disabled", disabledfgcolor), ("active", activefgcolor)],
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
        background=bgcolor,
        foreground=fgcolor,
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
            ("disabled", bgcolor),
            ("pressed", activebgcolor),
            ("active", activebgcolor),
            ("hover", activebgcolor),
            # ("selected", tvwindow),
        ],
        foreground=[
            ("disabled", disabledfgcolor),
            ("pressed", activefgcolor),
            ("active", activefgcolor),
            ("hover", activefgcolor),
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
        background=bgcolor,
        foreground=fgcolor,
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
            ("disabled", bgcolor),
            ("pressed", activebgcolor),
            ("active", activebgcolor),
            ("hover", activebgcolor),
            # ("selected", "springgreen3"),
        ],
        foreground=[
            ("disabled", disabledfgcolor),
            ("pressed", activefgcolor),
            ("active", activefgcolor),
            ("hover", activefgcolor),
        ],
    )

    # ===================================================
    # Style for ALL TProgressbars
    # ===================================================

    sty.configure(
        "bar.Horizontal.TProgressbar",
        troughcolor=troughcolor,
        bordercolor=troughcolor,
        background=barcolor,
        lightcolor=barcolor,
        darkcolor=barcolor,
    )

    # ===================================================
    # Style for TCombobox (in progress)
    # ===================================================
    sty.configure(
        "TCombobox",
        background=activebgcolor,
        foreground="black",
        fieldbackground=tvwindow,
        fieldforeground="black",
        arrowcolor="black",
    )
    sty.configure(
        "ComboboxPopdownFrame",
        background=bgcolor,
        foreground=fgcolor,
        fieldbackground=tvwindow,
        fieldforeground="black",
        borderwidth=2,
        relief="sunken",
    )

    # ===================================================
    # Style for ALL TScale widgets
    # ===================================================

    sty.configure(
        "bar.Horizontal.TScale",
        troughcolor=troughcolor,
        bordercolor=troughcolor,
        background=barcolor,
        lightcolor=barcolor,
        darkcolor=barcolor,
    )
    # ===================================================
    # Style for ALL TSpinbox Widgets
    # ===================================================
    sty.configure(
        "TSpinbox",
        arrowsize=11,
        bordercolor=_bordercolor,
        background=activebgcolor,
        foreground="black",
        lightcolor=_lightcolor,
        darkcolor=_darkcolor,
        selectbackground="springgreen2",
        selectforeground="black",
        fieldbackground=tvwindow,
        fieldforeground="black",
        arrowcolor="black",
    )

    # ===================================================
    # Style for ALL TEntry widgets
    # ===================================================
    sty.configure("TEntry", foreground="black", fieldbackground=tvwindow)

    # ===================================================
    # Style for ALL TFrame widgets
    # ===================================================
    sty.configure("TFrame", background=bgcolor, relief=tk.GROOVE, borderwidth=2)

    # ===================================================
    # Style for ALL TLabelframe widgets
    # ===================================================
    sty.configure(
        "TLabelframe",
        background=bgcolor,
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
        foreground=fgcolor,
        background=bgcolor,
        padding=[12, 6],
    )

    # ===================================================
    # Style for ALL ScrolledTreeview widgets
    # ===================================================
    sty.configure(
        "Treeview",
        background=tvwindow,
        foreground="black",
        selected=selectbackground,
        fieldbackground=tvwindow,
        # fieldforeground="black",
        font="Ubuntu 11 bold",
    )
    sty.configure("heading", relief="sunken", background=bgcolor, font="Ubuntu 11 bold")
    sty.configure("item", foreground="black", padding=[3, 3])
    sty.configure("cell", padding=[6, 6])
    # ===================================================
    # Style for ALL TMenuButton
    # ===================================================
    sty.configure(
        "TMenubutton",
        background=bgcolor,
        foreground=fgcolor,
        width=25,
        padding=2,
        relief="raised",
        font="Ubuntu 9 bold",
    )

    # ===================================================
    # Style for ALL TPanedwindow
    # ===================================================
    sty.configure("TPanedwindow", background=bgcolor)
    sty.configure(
        "Sash",
        background=troughcolor,
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
    toplevel.option_add("*TCombobox*Listbox*Background", tvwindow)
    toplevel.option_add("*TCombobox*Listbox*Foreground", "black")
    toplevel.option_add("*TCombobox*Listbox*selectBackground", selectbackground)
    toplevel.option_add("*TCombobox*Listbox*selectForeground", selectforeground)
    toplevel.option_add("TkFDialog*Foreground", "black")
    toplevel.option_add("TkChooseDir*Foreground", "black")


def set_palette(toplevel):
    # https://www.tcl-lang.org/man/tcl8.6/TkCmd/palette.htm
    toplevel.tk_setPalette(
        activeBackground=activebgcolor,
        activeForeground=activefgcolor,
        background=bgcolor,
        disabledForeground=disabledfgcolor,
        foreground=fgcolor,
        # highlightBackground="",
        # highlightColor="",
        # InsertBackground="",
        # selectColor="",
        selectBackground=selectbackground,
        selectForeground=selectforeground,
        # troughColor="",
    )


def reset_palette(toplevel):
    # https://www.tcl-lang.org/man/tcl8.6/TkCmd/palette.htm
    toplevel.tk_setPalette(
        activeBackground="#c3c3c3",
        activeForeground="black",
        background="#d9d9d9",
        disabledForeground="gray40",
        foreground="black",
        # highlightBackground="",
        # highlightColor="",
        # InsertBackground="",
        selectColor="red",
        selectBackground="blue",
        selectForeground="white",
        # troughColor="",
    )


def get_version():
    print(f"{version=}")
