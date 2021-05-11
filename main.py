from tkinter.constants import BOTTOM, GROOVE, RAISED, TOP
import zhongli as zt
import diona as dt
import tkinter as tk
from tkinter import ttk

TALENT_LEVELS = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13]


window = tk.Tk()
window.resizable(False, False)
window.title("Shield Calculator")
window.iconbitmap("shield_pencil.ico")


frame_z = tk.Frame(window)
frame_z.pack(fill=tk.BOTH, side=TOP)

def set_shield_zhongli():
    hp = int(zhongli_hp.get())
    talent_lvl = int(zhongli_talent.get())
    zhongli_shield_label["text"] = zt.zhongli_shield(hp, talent_lvl)

zhongli_label = tk.Label(frame_z, text="Zhongli", justify="center")
zhongli_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

zhongli_hp = tk.Entry(frame_z, width=10, justify="center")
zhongli_hp.insert(0, "HP")
zhongli_hp.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

zhongli_talent = ttk.Combobox(frame_z, justify="center", state="readonly", values=TALENT_LEVELS)
zhongli_talent.set("Talent Level")
zhongli_talent.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

button_calc_zhon = ttk.Button(frame_z, text="Calculate", command=set_shield_zhongli)
button_calc_zhon.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

zhongli_shield_label = tk.Label(frame_z, text="0", justify="center", relief=GROOVE, bd=3, width=7)
zhongli_shield_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)


frame_d = tk.Frame(window)
frame_d.pack(fill=tk.BOTH, side=BOTTOM)

def set_shield_diona():
    hp = int(diona_hp.get())
    talent_lvl = int(diona_talent.get())
    hold = bool(hold_var.get())
    constellation = bool(const_var.get())
    diona_shield_label["text"] = dt.diona_shield(hp, talent_lvl, hold, constellation)

diona_label = tk.Label(frame_d, text="Diona", justify="center")
diona_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=(5, 15), pady=5)

diona_hp = tk.Entry(frame_d, width=10, justify="center")
diona_hp.insert(0, "HP")
diona_hp.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

diona_talent = ttk.Combobox(frame_d, justify="center", state="readonly", values=TALENT_LEVELS)
diona_talent.set("Talent Level")
diona_talent.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

hold_var = tk.IntVar()
diona_hold = ttk.Checkbutton(frame_d, text="Hold", variable=hold_var)
diona_hold.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

const_var = tk.IntVar()
diona_const = ttk.Checkbutton(frame_d, text="C2", variable=const_var)
diona_const.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

button_calc_diona = ttk.Button(frame_d, text="Calculate", command=set_shield_diona)
button_calc_diona.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

diona_shield_label = tk.Label(frame_d, text="0", justify="center", relief=GROOVE, bd=3, width=7)
diona_shield_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)


window.mainloop()