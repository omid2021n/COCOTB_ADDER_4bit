import cocotb
import logging
import random
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
from cocotb.utils import get_sim_time

@cocotb.test()
async def test(dut):
    error_count = 0  # Initialize the error count
    logging.getLogger().setLevel(logging.INFO)
    
    din_bin   = BinaryValue(value=0, n_bits=8, bigEndian=False)
    sel_bin   = BinaryValue(value=0, n_bits=3, bigEndian=False)
    dout_bin  = BinaryValue(value=0, n_bits=1, bigEndian=False)


    for _ in range(30):
        din = random.randint(0,255)   #randomize  din
        sel = random.randint(0, 7)    #randomize  sel
        din_bin.integer = din    # convert  intiger  to  binnary 
        sel_bin.integer = sel    #convert   intiger  to binnary 
        
        dut.din.value = din_bin
        dut.sel.value = sel_bin
        
        await Timer(10, 'ns')
        
        dout = dut.dout.value
        dout_bin.integer = dout
        
        print('din:', din_bin,'sel:',sel_bin, 'dout:', dout_bin)
        print('exp_dout:', din_bin.binstr[sel],'dout:',dout_bin.binstr)
        print('din_bin.binstr[7-sel] : ',din_bin.binstr[7-sel] , 'sel  : ' , sel)
        if din_bin.binstr[7-sel] != dout_bin.binstr:
            error_count += 1
     
        await Timer(10, 'ns')
       
    print('--------------------------------------------------------')
    if error_count > 0:
        logging.error('Number of failed test cases: %d', error_count)
    else:
        logging.info('All test cases passed')
    print('--------------------------------------------------------')
