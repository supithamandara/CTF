#!/bin/env python3

import periodictable

el_list = ["Ag" , "Hg" , "Ta" , "Sb" , "Po" , "Pd" , "Hg" , "Pt" , "Lr"]

for el in el_list:
	print(chr(vars(periodictable)[el].number))

