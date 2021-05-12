from tkinter.constants import GROOVE
import zhongli as zt
import diona as dt
import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        TALENT_LEVELS = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13]
        
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        # Zhongli
        self.zhongli_label = tk.Label(parent, text="Zhongli", justify="center")

        self.zhongli_hp = tk.Entry(parent, width=10, justify="center")
        self.zhongli_hp.insert(0, "HP")

        self.zhongli_talent = ttk.Combobox(parent, justify="center", state="readonly", values=TALENT_LEVELS)
        self.zhongli_talent.set("Talent Level")

        self.button_calc_zhon = ttk.Button(parent, text="Calculate", command=self.set_shield_zhongli)

        self.zhongli_shield_label = tk.Label(parent, text="0", justify="center", relief=GROOVE, bd=3, width=7)
        
        # Diona
        self.diona_label = tk.Label(parent, text="Diona", justify="center")

        self.diona_hp = tk.Entry(parent, width=10, justify="center")
        self.diona_hp.insert(0, "HP")

        self.diona_talent = ttk.Combobox(parent, justify="center", state="readonly", values=TALENT_LEVELS)
        self.diona_talent.set("Talent Level")

        self.hold_var = tk.IntVar()
        self.diona_hold = ttk.Checkbutton(parent, text="Hold", variable=self.hold_var)

        self.const_var = tk.IntVar()
        self.diona_const = ttk.Checkbutton(parent, text="C2", variable=self.const_var)

        self.button_calc_diona = ttk.Button(parent, text="Calculate", command=self.set_shield_diona)

        self.diona_shield_label = tk.Label(parent, text="0", justify="center", relief=GROOVE, bd=3, width=7)
        
        # Layout
        self.zhongli_label.grid(row=0, column=0, padx=5, pady=5)
        self.zhongli_hp.grid(row=0, column=1, padx=5, pady=5)
        self.zhongli_talent.grid(row=0, column=2, padx=5, pady=5)
        self.button_calc_zhon.grid(row=0, column=3, padx=5, pady=5)
        self.zhongli_shield_label.grid(row=0, column=4, padx=5, pady=5)
        self.diona_label.grid(row=1, column=0)
        self.diona_hp.grid(row=1, column=1)
        self.diona_talent.grid(row=1, column=2)
        self.diona_hold.grid(row=1, column=3)
        self.diona_const.grid(row=1, column=4)
        self.button_calc_diona.grid(row=1, column=5, padx=5, pady=5)
        self.diona_shield_label.grid(row=1, column=6, padx=5, pady=5)
        
        
    def set_shield_zhongli(self):
        self.hp = int(self.zhongli_hp.get())
        self.talent_lvl = int(self.zhongli_talent.get())
        self.zhongli_shield_label["text"] = zt.zhongli_shield(self.hp, self.talent_lvl)
    
    def set_shield_diona(self):
        self.hp = int(self.diona_hp.get())
        self.talent_lvl = int(self.diona_talent.get())
        self.hold = bool(self.hold_var.get())
        self.constellation = bool(self.const_var.get())
        self.diona_shield_label["text"] = dt.diona_shield(self.hp, self.talent_lvl, self.hold, self.constellation)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Shield Calculator")
    root.iconbitmap("shield_pencil.ico")
    MainApplication(root)
    root.mainloop()