#!/usr/bin/env python3
# Author: WittsEnd2
# Contributors: 

import angr
import claripy


def main():
    base_addr = 0x00100000 # define the offset 
    p = angr.Project("./a.out", main_opts={'base_addr':base_addr}) # set the binary we are working with and the offset
    arg_chars = [claripy.BVS('flag-{%d' % i, 8) for i in range(0x10)] # what to look for (and the length)
    arg = claripy.Concat(*arg_chars + [claripy.BVV(b'\n')]) 
    
    st = p.factory.entry_state(args=["./a.out"], add_options=angr.options.unicorn,  STDIN=arg) # What to actually run and ensure that we are working with  STDIN.
    for k in arg_chars:
        st.solver.add(k > 0x20)
        st.solver.add(k < 0x7f)

    sm = p.factory.simulation_manager(st)
    sm.run()
    for i in sm.deadended:

        print(i.solver.eval(arg, cast_to=bytes))

if __name__ == "__main__":
    main()