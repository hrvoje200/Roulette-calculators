from abc import ABC, abstractmethod
from enum import Enum
import os
import re
import pdb


class Outcome(Enum):
  UNUSUAL = '*'
  NEGATIVE = '-'
  POSITIVE = '+'

class System(ABC):

  @staticmethod
  @abstractmethod
  def process_number_sequence(sequence):
    @staticmethod
    @abstractmethod
    def show_notification():
      pass

class Condition(ABC):
  @staticmethod
  @abstractmethod
  def check_outcome_sequence(sequence):
    pass

  @staticmethod
  @abstractmethod
  def show_notification():
    pass

class p066Last41(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqout=[]
    for (i, n) in enumerate(sequence):
      nInLast41 = False
      nSeq = sequence[0:i] 
      for m in nSeq[-41:]: 
        if m == n: nInLast41 = True
      if nInLast41:
        outcome = Outcome.POSITIVE
      else:
        outcome = Outcome.NEGATIVE
      seqout.append(outcome)
    return seqout

  @staticmethod
  def show_notification():
    return "p066Last41"

class Tv2red2row(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      black2ndrow = [2, 8, 11, 17, 20, 26, 29, 35]
      red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]   
      if l in red:
        Aoutcome = Outcome.POSITIVE
      elif l in black2ndrow:
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "Tv2red2row"

class A_1t_i_2t_(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(1,25):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "A_1t_i_2t_"    

class B_1t_i_3t_(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqBout=[]
    for m in sequence:
      if m in range(1,13):
        Boutcome = Outcome.POSITIVE
      elif m in range(25,37):
        Boutcome = Outcome.POSITIVE
      else:
        Boutcome = Outcome.NEGATIVE
      seqBout.append(Boutcome)
    return seqBout    

  @staticmethod
  def show_notification():
    return "B_1t_i_3t_"

class C_2t_i_3t_(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqCout=[]
    for n in sequence:
      if n in range(13,37):
        Coutcome = Outcome.POSITIVE
      else:
        Coutcome = Outcome.NEGATIVE
      seqCout.append(Coutcome)
    return seqCout    

  @staticmethod
  def show_notification():
    return "C_2t_i_3t_"

class D__4_do_27(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqDout=[]
    for p in sequence:
      if p in range(4,28):
        Doutcome = Outcome.POSITIVE
      else:
        Doutcome = Outcome.NEGATIVE
      seqDout.append(Doutcome)
    return seqDout    

  @staticmethod
  def show_notification():
    return "D__4_do_27"

class E_28_do_15(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqEout=[]
    for r in sequence:
      if r in range(28,37):
        Eoutcome = Outcome.POSITIVE
      elif r in range(1,16):
        Eoutcome = Outcome.POSITIVE
      else:
        Eoutcome = Outcome.NEGATIVE
      seqEout.append(Eoutcome)
    return seqEout  

  @staticmethod
  def show_notification():
    return "E_28_do_15"

class F_16_do_3_(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqFout=[]
    for s in sequence:
      if s in range(16,37):
        Foutcome = Outcome.POSITIVE
      elif s in range(1,4):
        Foutcome = Outcome.POSITIVE
      else:
        Foutcome = Outcome.NEGATIVE
      seqFout.append(Foutcome)
    return seqFout
    
  @staticmethod
  def show_notification():
    return "F_16_do_3_"    

class G__7_do_30(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqGout=[]
    for t in sequence:
      if t in range(7,31):
        Goutcome = Outcome.POSITIVE
      else:
        Goutcome = Outcome.NEGATIVE
      seqGout.append(Goutcome)
    return seqGout

  @staticmethod
  def show_notification():
    return "G__7_do_30"  

class H_31_do_18(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqHout=[]
    for u in sequence:
      if u in range(31,37):
        Houtcome = Outcome.POSITIVE
      elif u in range(1,19):
        Houtcome = Outcome.POSITIVE
      else:
        Houtcome = Outcome.NEGATIVE
      seqHout.append(Houtcome)
    return seqHout
    
  @staticmethod
  def show_notification():
    return "H_31_do_18"

class I_19_do_6_(System):
  def process_number_sequence(sequence):
    seqIout=[]
    for v in sequence:
      if v in range(19,37):
        Ioutcome = Outcome.POSITIVE
      elif v in range(1,7):
        Ioutcome = Outcome.POSITIVE
      else:
        Ioutcome = Outcome.NEGATIVE
      seqIout.append(Ioutcome)
    return seqIout
    
  @staticmethod
  def show_notification():
    return "I_19_do_6_" 

class J_10_do_33(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqJout=[]
    for w in sequence:
      if w in range(10,34):
        Joutcome = Outcome.POSITIVE
      else:
        Joutcome = Outcome.NEGATIVE
      seqJout.append(Joutcome)
    return seqJout

  @staticmethod
  def show_notification():
    return "J_10_do_33"  

class K_34_do_21(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqKout=[]
    for a in sequence:
      if a in range(34,37):
        Koutcome = Outcome.POSITIVE
      elif a in range(1,22):
        Koutcome = Outcome.POSITIVE
      else:
        Koutcome = Outcome.NEGATIVE
      seqKout.append(Koutcome)
    return seqKout
    
  @staticmethod
  def show_notification():
    return "K_34_do_21"

class L_22_do_9_(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqLout=[]
    for b in sequence:
      if b in range(22,37):
        Loutcome = Outcome.POSITIVE
      elif b in range(1,10):
        Loutcome = Outcome.POSITIVE
      else:
        Loutcome = Outcome.NEGATIVE
      seqLout.append(Loutcome)
    return seqLout
    
  @staticmethod
  def show_notification():
    return "L_22_do_9_"    

class I__1s_i_2s(System):                     
  @staticmethod
  def process_number_sequence(sequence):
    seqItout=[]
    for c in sequence:
      I = [c for c in range(1,37) if c % 3 == 1]
      II = [c for c in range(1,37) if c % 3 == 2]
      III = [c for c in range(1,37) if c % 3 == 0]
      if c in I:
        outcomeIt = Outcome.POSITIVE
      elif c in II:
        outcomeIt = Outcome.POSITIVE
      else:
        outcomeIt = Outcome.NEGATIVE
      seqItout.append(outcomeIt)
    return seqItout 
 
  @staticmethod
  def show_notification():
    return "I__1s_i_2s"    

class II_1s_i_3s(System):             
  @staticmethod
  def process_number_sequence(sequence):
    seqIIout=[]
    for d in sequence:
      I1 = [d for d in range(1,37) if d % 3 == 1]
      II2 = [d for d in range(1,37) if d % 3 == 2]
      III3 = [d for d in range(1,37) if d % 3 == 0]
      if d in I1:
        outcomeII = Outcome.POSITIVE
      elif d in III3:
        outcomeII = Outcome.POSITIVE
      else:
        outcomeII = Outcome.NEGATIVE
      seqIIout.append(outcomeII)
    return seqIIout 

  @staticmethod
  def show_notification():
    return "II_1s_i_3s"

class III2s_i_3s(System):           
  @staticmethod
  def process_number_sequence(sequence):
    seqIIIout=[]
    for e in sequence:
      Ia = [e for e in range(1,37) if e % 3 == 1]
      IIb = [e for e in range(1,37) if e % 3 == 2]
      IIIc = [e for e in range(1,37) if e % 3 == 0]
      if e in IIb:
        outcomeIII = Outcome.POSITIVE
      elif e in IIIc:
        outcomeIII = Outcome.POSITIVE
      else:
        outcomeIII = Outcome.NEGATIVE
      seqIIIout.append(outcomeIII)
    return seqIIIout 

  @staticmethod
  def show_notification():
    return "III2s_i_3s" 

class p050Last25(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqout25=[]
    for (i, n) in enumerate(sequence):
      nInLast25 = False
      nSeq = sequence[0:i] 
      for m in nSeq[-25:]: 
        if m == n: nInLast25 = True
      if nInLast25:
        outcome25 = Outcome.POSITIVE
      else:
        outcome25 = Outcome.NEGATIVE
      seqout25.append(outcome25)
    return seqout25
  
  @staticmethod
  def show_notification():
    return "p050Last25"

class p05_BLK_n0(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqBrout=[]
    for f in sequence:
      black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
      red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
      if f in black:
        first1outcome = Outcome.POSITIVE
      else:
        first1outcome = Outcome.NEGATIVE
      seqBrout.append(first1outcome)
    return seqBrout

  @staticmethod
  def show_notification():
    return "p05_BLK_n0"

class p05_red_n0(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqBrout=[]
    for f in sequence:
      black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
      red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
      if f in red:
        first1outcome = Outcome.POSITIVE
      else:
        first1outcome = Outcome.NEGATIVE
      seqBrout.append(first1outcome)
    return seqBrout

  @staticmethod
  def show_notification():
    return "p05_red_n0"

class p05_HIG_n0(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqhighlowout=[]
    for f in sequence:
      high = [f for f in range(1,37) if f >= 19]
      low = [f for f in range(1,37) if f <= 18]
      if f in high:
        first1outcome = Outcome.POSITIVE
      else:
        first1outcome = Outcome.NEGATIVE
      seqhighlowout.append(first1outcome)
    return seqhighlowout

  @staticmethod
  def show_notification():
    return "p05_HIG_n0" 

class p05_low_n0(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqhighlowout=[]
    for f in sequence:
      high = [f for f in range(1,37) if f >= 19]
      low = [f for f in range(1,37) if f <= 18]
      if f in low:
        first1outcome = Outcome.POSITIVE
      else:
        first1outcome = Outcome.NEGATIVE
      seqhighlowout.append(first1outcome)
    return seqhighlowout

  @staticmethod
  def show_notification():
    return "p05_low_n0"

class p05_EVN_n0(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqevenoddout=[]
    for f in sequence:
      even = [f for f in range(1,37) if f % 2 == 0]
      odd = [f for f in range(1,37) if f % 2 == 1]
      if f in even:
        first1outcome = Outcome.POSITIVE
      else:
        first1outcome = Outcome.NEGATIVE
      seqevenoddout.append(first1outcome)
    return seqevenoddout

  @staticmethod
  def show_notification():
    return "p05_EVN_n0"

class p05_odd_n0(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqevenoddout=[]
    for f in sequence:
      even = [f for f in range(1,37) if f % 2 == 0]
      odd = [f for f in range(1,37) if f % 2 == 1]
      if f in odd:
        first1outcome = Outcome.POSITIVE
      else:
        first1outcome = Outcome.NEGATIVE
      seqevenoddout.append(first1outcome)
    return seqevenoddout

  @staticmethod
  def show_notification():
    return "p05_odd_n0"     

class IICarry_BB(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqCarryout=[]
    for z in sequence:
      BBet = [0,1,2,3]
      BBetalt = [4,5,6]
      if z in BBet:
        Carryoutcome = Outcome.POSITIVE
      elif z in BBetalt:
        Carryoutcome = Outcome.UNUSUAL
      else:
        Carryoutcome = Outcome.NEGATIVE
      seqCarryout.append(Carryoutcome)
    return seqCarryout

  @staticmethod
  def show_notification():
    return "IICarry_BB"

class s_5SAME_BR(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqBout=[]
    for f in sequence:
      black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
      red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
      if f in black:
        first1outcome = Outcome.POSITIVE
      elif f in red:
        first1outcome = Outcome.NEGATIVE
      else:
        first1outcome = Outcome.UNUSUAL
      seqBout.append(first1outcome)
    return seqBout

  @staticmethod
  def show_notification():
    return "s_5SAME_BR"    

class s_5SAME_HL(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqhighout=[]
    for f in sequence:
      high = [f for f in range(1,37) if f >= 19]
      low = [f for f in range(1,37) if f <= 18]
      if f in high:
        first1outcome = Outcome.POSITIVE
      elif f in low:
        first1outcome = Outcome.NEGATIVE
      else:
        first1outcome = Outcome.UNUSUAL
      seqhighout.append(first1outcome)
    return seqhighout

  @staticmethod
  def show_notification():
    return "s_5SAME_HL" 

class s_5SAME_EO(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqevenout=[]
    for f in sequence:
      even = [f for f in range(1,37) if f % 2 == 0]
      odd = [f for f in range(1,37) if f % 2 == 1]
      if f in even:
        first1outcome = Outcome.POSITIVE
      elif f in odd:
        first1outcome = Outcome.NEGATIVE
      else:
        first1outcome = Outcome.UNUSUAL
      seqevenout.append(first1outcome)
    return seqevenout

  @staticmethod
  def show_notification():
    return "s_5SAME_EO" 

class s_SSDS_BR_(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqBout=[]
    for f in sequence:
      black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
      red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
      if f in black:
        first1outcome = Outcome.POSITIVE
      elif f in red:
        first1outcome = Outcome.NEGATIVE
      else:
        first1outcome = Outcome.UNUSUAL
      seqBout.append(first1outcome)
    return seqBout

  @staticmethod
  def show_notification():
    return "s_SSDS_BR_"    

class s_SSDS_HL_(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqhighout=[]
    for f in sequence:
      high = [f for f in range(1,37) if f >= 19]
      low = [f for f in range(1,37) if f <= 18]
      if f in high:
        first1outcome = Outcome.POSITIVE
      elif f in low:
        first1outcome = Outcome.NEGATIVE
      else:
        first1outcome = Outcome.UNUSUAL
      seqhighout.append(first1outcome)
    return seqhighout

  @staticmethod
  def show_notification():
    return "s_SSDS_HL_" 

class s_SSDS_EO_(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqevenout=[]
    for f in sequence:
      even = [f for f in range(1,37) if f % 2 == 0]
      odd = [f for f in range(1,37) if f % 2 == 1]
      if f in even:
        first1outcome = Outcome.POSITIVE
      elif f in odd:
        first1outcome = Outcome.NEGATIVE
      else:
        first1outcome = Outcome.UNUSUAL
      seqevenout.append(first1outcome)
    return seqevenout

  @staticmethod
  def show_notification():
    return "s_SSDS_EO_" 

class p033__1t__(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(1,13):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "p033__1t__"

class p033_4to15(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(4,16):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "p033_4to15"

class p033_7to18(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(7,19):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "p033_7to18"

class p033_10t21(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(10,22):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "p033_10t21"    

class p033__2t__(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(13,25):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "p033__2t__"

class p033_16t27(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(16,28):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "p033_16t27"    

class p033_19t30(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(19,31):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "p033_19t30"

class p033_22t33(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(22,34):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "p033_22t33"

class p033__3t__(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqAout=[]
    for l in sequence:
      if l in range(25,37):
        Aoutcome = Outcome.POSITIVE
      else:
        Aoutcome = Outcome.NEGATIVE
      seqAout.append(Aoutcome)
    return seqAout
  
  @staticmethod
  def show_notification():
    return "p033__3t__"        

class p033_28to3(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqFout=[]
    for s in sequence:
      if s in range(28,37):
        Foutcome = Outcome.POSITIVE
      elif s in range(1,4):
        Foutcome = Outcome.POSITIVE
      else:
        Foutcome = Outcome.NEGATIVE
      seqFout.append(Foutcome)
    return seqFout
    
  @staticmethod
  def show_notification():
    return "p033_28to3"

class p033_31to6(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqFout=[]
    for s in sequence:
      if s in range(31,37):
        Foutcome = Outcome.POSITIVE
      elif s in range(1,7):
        Foutcome = Outcome.POSITIVE
      else:
        Foutcome = Outcome.NEGATIVE
      seqFout.append(Foutcome)
    return seqFout
    
  @staticmethod
  def show_notification():
    return "p033_31to6"

class p033_34to9(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqFout=[]
    for s in sequence:
      if s in range(34,37):
        Foutcome = Outcome.POSITIVE
      elif s in range(1,10):
        Foutcome = Outcome.POSITIVE
      else:
        Foutcome = Outcome.NEGATIVE
      seqFout.append(Foutcome)
    return seqFout
    
  @staticmethod
  def show_notification():
    return "p033_34to9"

class sy_I___row(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqItout=[]
    for c in sequence:
      I = [c for c in range(1,37) if c % 3 == 1]
      II = [c for c in range(1,37) if c % 3 == 2]
      III = [c for c in range(1,37) if c % 3 == 0]
      if c in I:
        outcomeIt = Outcome.POSITIVE
      elif c in II:
        outcomeIt = Outcome.NEGATIVE
      else:
        outcomeIt = Outcome.NEGATIVE
      seqItout.append(outcomeIt)
    return seqItout 
 
  @staticmethod
  def show_notification():
    return "sy_I___row"  

class sy_II__row(System):             
  @staticmethod
  def process_number_sequence(sequence):
    seqIIout=[]
    for d in sequence:
      I1 = [d for d in range(1,37) if d % 3 == 1]
      II2 = [d for d in range(1,37) if d % 3 == 2]
      III3 = [d for d in range(1,37) if d % 3 == 0]
      if d in II2:
        outcomeII = Outcome.POSITIVE
      elif d in III3:
        outcomeII = Outcome.NEGATIVE
      else:
        outcomeII = Outcome.NEGATIVE
      seqIIout.append(outcomeII)
    return seqIIout 

  @staticmethod
  def show_notification():
    return "sy_II__row"

class sy_III_row(System):             
  @staticmethod
  def process_number_sequence(sequence):
    seqIIout=[]
    for d in sequence:
      I1 = [d for d in range(1,37) if d % 3 == 1]
      II2 = [d for d in range(1,37) if d % 3 == 2]
      III3 = [d for d in range(1,37) if d % 3 == 0]
      if d in II2:
        outcomeII = Outcome.NEGATIVE
      elif d in III3:
        outcomeII = Outcome.POSITIVE
      else:
        outcomeII = Outcome.NEGATIVE
      seqIIout.append(outcomeII)
    return seqIIout 

  @staticmethod
  def show_notification():
    return "sy_III_row"

class invz_12_21(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqinv1221out=[]
    for z in sequence:
      inv12 = [12]
      inv21 = [21]
      if z in inv12:
        inv1221outcome = Outcome.POSITIVE
      elif z in inv21:
        inv1221outcome = Outcome.UNUSUAL
      else:
        inv1221outcome = Outcome.NEGATIVE
      seqinv1221out.append(inv1221outcome)
    return seqinv1221out

  @staticmethod
  def show_notification():
    return "invz_12_21"

class invz_13_31(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqinv1331out=[]
    for z in sequence:
      inv13 = [13]
      inv31 = [31]
      if z in inv13:
        inv1331outcome = Outcome.POSITIVE
      elif z in inv31:
        inv1331outcome = Outcome.UNUSUAL
      else:
        inv1331outcome = Outcome.NEGATIVE
      seqinv1331out.append(inv1331outcome)
    return seqinv1331out

  @staticmethod
  def show_notification():
    return "invz_13_31"

class invz_23_32(System):
  @staticmethod
  def process_number_sequence(sequence):
    seqinv2332out=[]
    for z in sequence:
      inv23 = [23]
      inv32 = [32]
      if z in inv23:
        inv2332outcome = Outcome.POSITIVE
      elif z in inv32:
        inv2332outcome = Outcome.UNUSUAL
      else:
        inv2332outcome = Outcome.NEGATIVE
      seqinv2332out.append(inv2332outcome)
    return seqinv2332out

  @staticmethod
  def show_notification():
    return "invz_23_32"

class firstsixth(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq1st6thout=[]
    for f in sequence:
      lastfivesixts = [f for f in range(7,37) if f>=7]
      firstsixt = [f for f in range(1,7) if f<7]
      if f in lastfivesixts:
        firstoutcome = Outcome.POSITIVE
      elif f in firstsixt:
        firstoutcome = Outcome.NEGATIVE
      else:
        firstoutcome = Outcome.NEGATIVE
      seq1st6thout.append(firstoutcome)
    return seq1st6thout
    
  @staticmethod
  def show_notification():
    return "firstsixth"

class secndsixth(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq2nd6thout=[]
    for g in sequence:
      nosecondsixt = [g for g in range(1,37) if (g<7) or (g>=13)]
      secondsixt = [g for g in range(7,13)]        
      if g in nosecondsixt:
        secondoutcome = Outcome.POSITIVE
      elif g in secondsixt:
        secondoutcome = Outcome.NEGATIVE
      else:
        secondoutcome = Outcome.NEGATIVE
      seq2nd6thout.append(secondoutcome)
    return seq2nd6thout

  @staticmethod
  def show_notification():
    return "secndsixth"  

class t1H_3rd6th(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq3rd6thout=[]
    for h in sequence:
      nothirdsixt = [h for h in range(1,37) if (h<13) or (h>=19)]
      thirdsixt = [h for h in range(13,19)]        
      if h in nothirdsixt:
        thirdoutcome = Outcome.POSITIVE
      elif h in thirdsixt:
        thirdoutcome = Outcome.NEGATIVE
      else:
        thirdoutcome = Outcome.NEGATIVE
      seq3rd6thout.append(thirdoutcome)
    return seq3rd6thout

  @staticmethod
  def show_notification():
    return "t1H_3rd6th"

class l3t_4th6th(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq4th6thout=[]
    for i in sequence:
      nofourthsixt = [i for i in range(1,37) if (i<19) or (i>=25)]
      fourthsixt = [i for i in range(19,25)]        
      if i in nofourthsixt:
        fourthoutcome = Outcome.POSITIVE
      elif i in fourthsixt:
        fourthoutcome = Outcome.NEGATIVE
      else:
        fourthoutcome = Outcome.NEGATIVE
      seq4th6thout.append(fourthoutcome)
    return seq4th6thout

  @staticmethod
  def show_notification():
    return "l3t_4th6th"

class fifthsixth(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq5th6thout=[]
    for j in sequence:
      nofifthsixt = [j for j in range(1,37) if (j<25) or (j>=31)]
      fifthsixt = [j for j in range(25,31)]        
      if j in nofifthsixt:
        fifthoutcome = Outcome.POSITIVE
      elif j in fifthsixt:
        fifthoutcome = Outcome.NEGATIVE
      else:
        fifthoutcome = Outcome.NEGATIVE
      seq5th6thout.append(fifthoutcome)
    return seq5th6thout

  @staticmethod
  def show_notification():
    return "fifthsixth"

class sixthsixth(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq6th6thout=[]
    for k in sequence:
      nosixthsixt = [k for k in range(1,37) if (k<31)]
      sixthsixt = [k for k in range(31,37)]        
      if k in nosixthsixt:
        sixthoutcome = Outcome.POSITIVE
      elif k in sixthsixt:
        sixthoutcome = Outcome.NEGATIVE
      else:
        sixthoutcome = Outcome.NEGATIVE
      seq6th6thout.append(sixthoutcome)
    return seq6th6thout

  @staticmethod
  def show_notification():
    return "sixthsixth"

class _1st2ndsix(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq1st2nd6thout=[]
    for f in sequence:
      lastfivesixts = [f for f in range(1,37) if (f<4) or (f>=10)]
      firstsixt = [f for f in range(4,10) ]
      if f in lastfivesixts:
        firstoutcome = Outcome.POSITIVE
      elif f in firstsixt:
        firstoutcome = Outcome.NEGATIVE
      else:
        firstoutcome = Outcome.NEGATIVE
      seq1st2nd6thout.append(firstoutcome)
    return seq1st2nd6thout
    
  @staticmethod
  def show_notification():
    return "_1st2ndsix" 

class _2nd3rdsix(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq2nd3rd6thout=[]
    for f in sequence:
      lastfivesixts = [f for f in range(1,37) if (f<10) or (f>=16)]
      firstsixt = [f for f in range(10,16) ]
      if f in lastfivesixts:
        firstoutcome = Outcome.POSITIVE
      elif f in firstsixt:
        firstoutcome = Outcome.NEGATIVE
      else:
        firstoutcome = Outcome.NEGATIVE
      seq2nd3rd6thout.append(firstoutcome)
    return seq2nd3rd6thout
    
  @staticmethod
  def show_notification():
    return "_2nd3rdsix" 

class _3rd4thsix(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq3rd4th6thout=[]
    for f in sequence:
      lastfivesixts = [f for f in range(1,37) if (f<16) or (f>=22)]
      firstsixt = [f for f in range(16,22) ]
      if f in lastfivesixts:
        firstoutcome = Outcome.POSITIVE
      elif f in firstsixt:
        firstoutcome = Outcome.NEGATIVE
      else:
        firstoutcome = Outcome.NEGATIVE
      seq3rd4th6thout.append(firstoutcome)
    return seq3rd4th6thout
    
  @staticmethod
  def show_notification():
    return "_3rd4thsix" 

class _4th5thsix(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq4th5th6thout=[]
    for f in sequence:
      lastfivesixts = [f for f in range(1,37) if (f<22) or (f>=28)]
      firstsixt = [f for f in range(22,28) ]
      if f in lastfivesixts:
        firstoutcome = Outcome.POSITIVE
      elif f in firstsixt:
        firstoutcome = Outcome.NEGATIVE
      else:
        firstoutcome = Outcome.NEGATIVE
      seq4th5th6thout.append(firstoutcome)
    return seq4th5th6thout
    
  @staticmethod
  def show_notification():
    return "_4th5thsix" 

class _5th6thsix(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq5th6thout=[]
    for f in sequence:
      lastfivesixts = [f for f in range(1,37) if (f<28) or (f>=34)]
      firstsixt = [f for f in range(28,34)]
      if f in lastfivesixts:
        firstoutcome = Outcome.POSITIVE
      elif f in firstsixt:
        firstoutcome = Outcome.NEGATIVE
      else:
        firstoutcome = Outcome.NEGATIVE
      seq5th6thout.append(firstoutcome)
    return seq5th6thout
    
  @staticmethod
  def show_notification():
    return "_5th6thsix" 

class _6th1stsix(System):
  @staticmethod
  def process_number_sequence(sequence):
    seq6th1st6thout=[]
    for f in sequence:
      lastfivesixts = [f for f in range(1,37) if (f>=4) and (f<=33)]
      firstsixt = [f for f in range(1,37) if (f<=3) or (f>=34)]
      if f in lastfivesixts:
        firstoutcome = Outcome.POSITIVE
      elif f in firstsixt:
        firstoutcome = Outcome.NEGATIVE
      else:
        firstoutcome = Outcome.NEGATIVE
      seq6th1st6thout.append(firstoutcome)
    return seq6th1st6thout
    
  @staticmethod
  def show_notification():
    return "_6th1stsix" 

class same5B(Condition):
  p = re.compile('[^+]\+\+\+\+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return same5B.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "same5B"

class same5R(Condition):
  p = re.compile('[^-]\-\-\-\-\-$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return same5R.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "same5R"

class HLTn5B(Condition):
  p = re.compile('[^+]\+\+\+\+\+[^+][^+][^+][^+][^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return HLTn5B.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "HLTn5B"

class HLTn5R(Condition):
  p = re.compile('[^-]\-\-\-\-\-[^-][^-][^-][^-][^-]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return HLTn5R.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "HLTn5R"

class same5H(Condition):
  p = re.compile('[^+]\+\+\+\+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return same5H.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "same5H"

class same5L(Condition):
  p = re.compile('[^-]\-\-\-\-\-$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return same5L.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "same5L"

class HLTn5H(Condition):
  p = re.compile('[^+]\+\+\+\+\+[^+][^+][^+][^+][^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return HLTn5H.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "HLTn5H"

class HLTn5L(Condition):
  p = re.compile('[^-]\-\-\-\-\-[^-][^-][^-][^-][^-]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return HLTn5L.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "HLTn5L"

class same5E(Condition):
  p = re.compile('[^+]\+\+\+\+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return same5E.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "same5E"

class same5O(Condition):
  p = re.compile('[^-]\-\-\-\-\-$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return same5O.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "same5O"

class HLTn5E(Condition):
  p = re.compile('[^+]\+\+\+\+\+[^+][^+][^+][^+][^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return HLTn5E.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "HLTn5E"

class HLTn5O(Condition):
  p = re.compile('[^-]\-\-\-\-\-[^-][^-][^-][^-][^-]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return HLTn5O.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "HLTn5O"

class _bbRb_(Condition): 
  @staticmethod
  def check_outcome_sequence(sequence):
    seqgrSSDS = sequence[-4:]
    GrupSSDS = False
    if len(sequence) <= 3:
      GrupSSDS = False
    if len(seqgrSSDS) >= 4:
      if (seqgrSSDS[0] == Outcome.POSITIVE and seqgrSSDS[1] == Outcome.POSITIVE and seqgrSSDS[2] == Outcome.NEGATIVE and seqgrSSDS[3] == Outcome.POSITIVE):
        GrupSSDS = True
    return GrupSSDS

  @staticmethod
  def show_notification():
    return "_bbRb_"

class _rrBr_(Condition): 
  @staticmethod
  def check_outcome_sequence(sequence):
    seqgrSSDS = sequence[-4:]
    GrupSSDS = False
    if len(sequence) <= 3:
      GrupSSDS = False
    if len(seqgrSSDS) >= 4:
      if (seqgrSSDS[0] == Outcome.NEGATIVE and seqgrSSDS[1] == Outcome.NEGATIVE and seqgrSSDS[2] == Outcome.POSITIVE and seqgrSSDS[3] == Outcome.NEGATIVE):
        GrupSSDS = True
    return GrupSSDS

  @staticmethod
  def show_notification():
    return "_rrBr_"

class STPn5R(Condition):
  p = re.compile('\+\+\-\+[^-][^-][^-][^-][^-]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return STPn5R.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "STPn5R"

class STPn5B(Condition):
  p = re.compile('\-\-\+\-[^+][^+][^+][^+][^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return STPn5B.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "STPn5B"

class _hhLh_(Condition): 
  @staticmethod
  def check_outcome_sequence(sequence):
    seqgrSSDS = sequence[-4:]
    GrupSSDS = False
    if len(sequence) <= 3:
      GrupSSDS = False
    if len(seqgrSSDS) >= 4:
      if (seqgrSSDS[0] == Outcome.POSITIVE and seqgrSSDS[1] == Outcome.POSITIVE and seqgrSSDS[2] == Outcome.NEGATIVE and seqgrSSDS[3] == Outcome.POSITIVE):
        GrupSSDS = True
    return GrupSSDS

  @staticmethod
  def show_notification():
    return "_hhLh_"

class _llHl_(Condition): 
  @staticmethod
  def check_outcome_sequence(sequence):
    seqgrSSDS = sequence[-4:]
    GrupSSDS = False
    if len(sequence) <= 3:
      GrupSSDS = False
    if len(seqgrSSDS) >= 4:
      if (seqgrSSDS[0] == Outcome.NEGATIVE and seqgrSSDS[1] == Outcome.NEGATIVE and seqgrSSDS[2] == Outcome.POSITIVE and seqgrSSDS[3] == Outcome.NEGATIVE):
        GrupSSDS = True
    return GrupSSDS

  @staticmethod
  def show_notification():
    return "_llHl_"

class STPn5L(Condition):
  p = re.compile('\+\+\-\+[^-][^-][^-][^-][^-]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return STPn5L.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "STPn5L"

class STPn5H(Condition):
  p = re.compile('\-\-\+\-[^+][^+][^+][^+][^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return STPn5H.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "STPn5H"    

class _eeOe_(Condition): 
  @staticmethod
  def check_outcome_sequence(sequence):
    seqgrSSDS = sequence[-4:]
    GrupSSDS = False
    if len(sequence) <= 3:
      GrupSSDS = False
    if len(seqgrSSDS) >= 4:
      if (seqgrSSDS[0] == Outcome.POSITIVE and seqgrSSDS[1] == Outcome.POSITIVE and seqgrSSDS[2] == Outcome.NEGATIVE and seqgrSSDS[3] == Outcome.POSITIVE):
        GrupSSDS = True
    return GrupSSDS

  @staticmethod
  def show_notification():
    return "_eeOe_"

class _ooEo_(Condition): 
  @staticmethod
  def check_outcome_sequence(sequence):
    seqgrSSDS = sequence[-4:]
    GrupSSDS = False
    if len(sequence) <= 3:
      GrupSSDS = False
    if len(seqgrSSDS) >= 4:
      if (seqgrSSDS[0] == Outcome.NEGATIVE and seqgrSSDS[1] == Outcome.NEGATIVE and seqgrSSDS[2] == Outcome.POSITIVE and seqgrSSDS[3] == Outcome.NEGATIVE):
        GrupSSDS = True
    return GrupSSDS

  @staticmethod
  def show_notification():
    return "_ooEo_"

class STPn5O(Condition):
  p = re.compile('\+\+\-\+[^-][^-][^-][^-][^-]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return STPn5O.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "STPn5O"

class STPn5E(Condition):
  p = re.compile('\-\-\+\-[^+][^+][^+][^+][^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return STPn5E.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "STPn5E"

class _grp3L(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast3 = sequence[-3:]
    areNeg = True
    if len(sequence)<=42:               
      areNeg = False
    for i in seqlast3:
      if i != Outcome.NEGATIVE: 
        areNeg = False
    return areNeg

  @staticmethod
  def show_notification():
    return "_grp3L"

class _grp4L(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast4 = sequence[-4:]
    areNega = True
    if len(sequence)<=43:               
      areNega = False
    for j in seqlast4:
      if j != Outcome.NEGATIVE:
        areNega = False
    return areNega

  @staticmethod
  def show_notification():
    return "_grp4L"

class _grp5L(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast5 = sequence[-5:]
    areNega = True
    if len(sequence)<=44:               
      areNega = False
    for j in seqlast5:
      if j != Outcome.NEGATIVE:
        areNega = False
    return areNega

  @staticmethod
  def show_notification():
    return "_grp5L" 

class gr_2LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence[40:])
    return gr_2LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "gr_2LL"

class g_2isW(Condition): 
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence[40:]:
      charSeq += o.value
    return g_2isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "g_2isW"

class gr_3LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence[40:])
    return gr_3LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "gr_3LL"

class g_3isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence[40:]:
      charSeq += o.value
    return g_3isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "g_3isW"

class gr_4LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence[40:])
    return gr_4LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "gr_4LL"

class g_4isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence[40:]:
      charSeq += o.value
    return g_4isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "g_4isW"

class _gr3LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence[24:])
    return _gr3LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "_gr3LL"

class _gr3iW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence[24:]:
      charSeq += o.value
    return _gr3iW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "_gr3iW"

class _gr4LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence[24:])
    return _gr4LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "_gr4LL"

class _gr4iW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence[24:]:
      charSeq += o.value
    return _gr4iW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "_gr4iW"

class _gr5LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence[24:])
    return _gr5LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "_gr5LL"

class _gr5iW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence[24:]:
      charSeq += o.value
    return _gr5iW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "_gr5iW"

class Grup3L(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqalast3a = sequence[-3:]
    areNegt = True
    if len(sequence)<=2:               
      areNegt = False
    for i in seqalast3a:
      if i != Outcome.NEGATIVE: 
        areNegt = False
    return areNegt

  @staticmethod
  def show_notification():
    return "Grup3L"

class Grup4L(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast4a = sequence[-4:]
    areNegatt = True
    if len(sequence)<=3:               
      areNegatt = False
    for j in seqlast4a:
      if j != Outcome.NEGATIVE:
        areNegatt = False
    return areNegatt

  @staticmethod
  def show_notification():
    return "Grup4L"

class Grup5L(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast5 = sequence[-5:]
    areNega = True
    if len(sequence)<=4:               
      areNega = False
    for j in seqlast5:
      if j != Outcome.NEGATIVE:
        areNega = False
    return areNega

  @staticmethod
  def show_notification():
    return "Grup5L"       

class GrupLL(Condition): 
  p = re.compile('[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return GrupLL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "GrupLL"

class GrisoW(Condition): 
  p = re.compile('[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return GrisoW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "GrisoW"

class Grp2LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return Grp2LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Grp2LL"

class Grp3LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return Grp3LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Grp3LL"

class Gr2isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return Gr2isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Gr2isW"

class Gr3isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return Gr3isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Gr3isW"

class Grp4LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return Grp4LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Grp4LL"

class Gr4isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return Gr4isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Gr4isW"

class Grp5LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return Grp5LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Grp5LL"

class Gr5isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return Gr5isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Gr5isW"    

class Grp6LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return Grp6LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Grp6LL"

class Gr6isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return Gr6isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Gr6isW"

class Grp7LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return Grp7LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Grp7LL"

class Gr7isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return Gr7isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Gr7isW"

class Grp8LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return Grp8LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Grp8LL"

class Gr8isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return Gr8isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Gr8isW"

class Grp9LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return Grp9LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Grp9LL"

class Gr9isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return Gr9isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Gr9isW"

class Gr10LL(Condition):
  p = re.compile('[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+][^+]+\++[^+]$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''.join(o.value for o in sequence)
    return Gr10LL.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "Gr10LL"

class G10isW(Condition):
  p = re.compile('[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+[^+]+\+$')

  @staticmethod
  def check_outcome_sequence(sequence):
    charSeq = ''
    for o in sequence:
      charSeq += o.value
    return G10isW.p.search(charSeq) != None

  @staticmethod
  def show_notification():
    return "G10isW"        

class num_12(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast1 = sequence[-1]
    arePos = False
    if seqlast1 == Outcome.POSITIVE:
      arePos = True
    return arePos

  @staticmethod
  def show_notification():
    return "num_12"

class num_21(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast1 = sequence[-1]
    arePos = False
    if seqlast1 == Outcome.UNUSUAL:
      arePos = True
    return arePos

  @staticmethod
  def show_notification():
    return "num_21"

class num_13(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast1 = sequence[-1]
    arePos = False
    if seqlast1 == Outcome.POSITIVE:
      arePos = True
    return arePos

  @staticmethod
  def show_notification():
    return "num_13"

class num_31(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast1 = sequence[-1]
    arePos = False
    if seqlast1 == Outcome.UNUSUAL:
      arePos = True
    return arePos

  @staticmethod
  def show_notification():
    return "num_31"

class num_23(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast1 = sequence[-1]
    arePos = False
    if seqlast1 == Outcome.POSITIVE:
      arePos = True
    return arePos

  @staticmethod
  def show_notification():
    return "num_23"

class num_32(Condition):  
  @staticmethod
  def check_outcome_sequence(sequence):
    seqlast1 = sequence[-1]
    arePos = False
    if seqlast1 == Outcome.UNUSUAL:
      arePos = True
    return arePos

  @staticmethod
  def show_notification():
    return "num_32"

class ix2L10(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last10 = sequence[-10:]
    if last10.count(Outcome.POSITIVE) + last10.count(Outcome.UNUSUAL) == 2:
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "ix2L10"

class ix3L10(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last10 = sequence[-10:]
    if last10.count(Outcome.POSITIVE) + last10.count(Outcome.UNUSUAL) == 3:
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "ix3L10"

class ix4L25(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last25 = sequence[-25:]
    if last25.count(Outcome.POSITIVE) + last25.count(Outcome.UNUSUAL) == 4:
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "ix4L25"

class ix5L25(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last25 = sequence[-25:]
    if last25.count(Outcome.POSITIVE) + last25.count(Outcome.UNUSUAL) == 5:
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "ix5L25"

class _5L21n(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last21 = sequence[-21:]
    if last21.count(Outcome.POSITIVE) == 5 and last21.count(Outcome.UNUSUAL) == 0:
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_5L21n"

class _4B_nU(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last10 = sequence[-10:]
    if last10.count(Outcome.POSITIVE) == 4 and last10.count(Outcome.UNUSUAL) == 0:
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_4B_nU"

class _3B_nU(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last10 = sequence[-10:]
    if last10.count(Outcome.POSITIVE) == 3 and last10.count(Outcome.UNUSUAL) == 0:
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_3B_nU"

class _2BL10(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last10 = sequence[-10:]
    if last10.count(Outcome.POSITIVE) == 2 and last10.count(Outcome.UNUSUAL) == 0:
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_2BL10"

class _8L21w(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last21 = sequence[-21:]
    countPos = last21.count(Outcome.POSITIVE)
    countNeg = last21.count(Outcome.NEGATIVE)
    countUnu = last21.count(Outcome.UNUSUAL)
    if (countPos >= 3 and countUnu >= 4) and (countPos + countUnu == 8):
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_8L21w"

class _7L21w(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last21 = sequence[-21:]
    countPos = last21.count(Outcome.POSITIVE)
    countNeg = last21.count(Outcome.NEGATIVE)
    countUnu = last21.count(Outcome.UNUSUAL)
    if (countPos >= 3 and countUnu >= 3) and (countPos + countUnu == 7):
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_7L21w"

class _6L21w(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last21 = sequence[-21:]
    countPos = last21.count(Outcome.POSITIVE)
    countNeg = last21.count(Outcome.NEGATIVE)
    countUnu = last21.count(Outcome.UNUSUAL)
    if (countPos >= 3 and countUnu >= 2) and (countPos + countUnu == 6):
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_6L21w"

class _5L21w(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last21 = sequence[-21:]
    countPos = last21.count(Outcome.POSITIVE)
    countNeg = last21.count(Outcome.NEGATIVE)
    countUnu = last21.count(Outcome.UNUSUAL)
    if (countPos >= 2 and countUnu >= 2) and (countPos + countUnu == 5):
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_5L21w"

class _4L21w(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last21 = sequence[-21:]
    countPos = last21.count(Outcome.POSITIVE)
    countNeg = last21.count(Outcome.NEGATIVE)
    countUnu = last21.count(Outcome.UNUSUAL)
    if (countPos >= 2 and countUnu >= 1) and (countPos + countUnu == 4):
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_4L21w"

class _4B456(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last21 = sequence[-10:]
    countPos = last21.count(Outcome.POSITIVE)
    countNeg = last21.count(Outcome.NEGATIVE)
    countUnu = last21.count(Outcome.UNUSUAL)
    if (countPos >= 2 and countUnu >= 1) and (countPos + countUnu == 4):
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_4B456"

class _4L21n(Condition):
  @staticmethod
  def check_outcome_sequence(sequence):
    last21 = sequence[-21:]
    countPos = last21.count(Outcome.POSITIVE)
    countNeg = last21.count(Outcome.NEGATIVE)
    countUnu = last21.count(Outcome.UNUSUAL)
    if countPos >= 4 and countUnu == 0:
      return True
    else:
      return False

  @staticmethod
  def show_notification():
    return "_4L21n"

systems_their_conditions = {}
systems_their_conditions[p066Last41] = (_grp3L, _grp4L, _grp5L, gr_2LL, g_2isW, gr_3LL, g_3isW, gr_4LL, g_4isW) 
systems_their_conditions[Tv2red2row] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[A_1t_i_2t_] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW) 
systems_their_conditions[B_1t_i_3t_] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW) 
systems_their_conditions[C_2t_i_3t_] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW) 
systems_their_conditions[D__4_do_27] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW) 
systems_their_conditions[E_28_do_15] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW) 
systems_their_conditions[F_16_do_3_] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[G__7_do_30] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[H_31_do_18] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[I_19_do_6_] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[J_10_do_33] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[K_34_do_21] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[L_22_do_9_] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[I__1s_i_2s] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[II_1s_i_3s] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[III2s_i_3s] = (Grup3L, Grup4L, Grup5L, Grp2LL, Gr2isW, Grp3LL, Gr3isW, Grp4LL, Gr4isW)
systems_their_conditions[p050Last25] = (_gr3LL, _gr3iW, _gr4LL, _gr4iW, _gr5LL, _gr5iW) 
systems_their_conditions[p05_BLK_n0] = (Grp3LL, Gr3isW, Grp4LL, Gr4isW, Grp5LL, Gr5isW) 
systems_their_conditions[p05_red_n0] = (Grp3LL, Gr3isW, Grp4LL, Gr4isW, Grp5LL, Gr5isW)
systems_their_conditions[p05_HIG_n0] = (Grp3LL, Gr3isW, Grp4LL, Gr4isW, Grp5LL, Gr5isW) 
systems_their_conditions[p05_low_n0] = (Grp3LL, Gr3isW, Grp4LL, Gr4isW, Grp5LL, Gr5isW) 
systems_their_conditions[p05_EVN_n0] = (Grp3LL, Gr3isW, Grp4LL, Gr4isW, Grp5LL, Gr5isW)
systems_their_conditions[p05_odd_n0] = (Grp3LL, Gr3isW, Grp4LL, Gr4isW, Grp5LL, Gr5isW)
systems_their_conditions[IICarry_BB] = (_2BL10, _3B_nU, _4B_nU, _4B456, _4L21n, _5L21n, _4L21w, _5L21w, _6L21w, _7L21w, _8L21w)  
systems_their_conditions[s_5SAME_BR] = (same5B, same5R, HLTn5B, HLTn5R) 
systems_their_conditions[s_5SAME_HL] = (same5H, same5L, HLTn5H, HLTn5L)
systems_their_conditions[s_5SAME_EO] = (same5E, same5O, HLTn5E, HLTn5O)
systems_their_conditions[s_SSDS_BR_] = (_rrBr_, _bbRb_, STPn5B, STPn5R) 
systems_their_conditions[s_SSDS_HL_] = (_llHl_, _hhLh_, STPn5H, STPn5L)
systems_their_conditions[s_SSDS_EO_] = (_ooEo_, _eeOe_, STPn5E, STPn5O)
systems_their_conditions[invz_12_21] = (num_12, num_21, ix2L10, ix3L10, ix4L25, ix5L25) 
systems_their_conditions[invz_13_31] = (num_13, num_31, ix2L10, ix3L10, ix4L25, ix5L25) 
systems_their_conditions[invz_23_32] = (num_23, num_32, ix2L10, ix3L10, ix4L25, ix5L25) 
systems_their_conditions[firstsixth] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW) 
systems_their_conditions[secndsixth] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW) 
systems_their_conditions[t1H_3rd6th] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW)  
systems_their_conditions[l3t_4th6th] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW) 
systems_their_conditions[fifthsixth] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW)
systems_their_conditions[sixthsixth] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW)
systems_their_conditions[_1st2ndsix] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW)
systems_their_conditions[_2nd3rdsix] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW)
systems_their_conditions[_3rd4thsix] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW)
systems_their_conditions[_4th5thsix] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW)
systems_their_conditions[_5th6thsix] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW)
systems_their_conditions[_6th1stsix] = (GrupLL, GrisoW, Grup3L, Grup4L, Grp2LL, Gr2isW, Grp3LL, Gr3isW) 
systems_their_conditions[p033__1t__] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033__2t__] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033__3t__] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033_4to15] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033_7to18] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033_10t21] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033_16t27] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033_19t30] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033_22t33] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033_28to3] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033_31to6] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[p033_34to9] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[sy_I___row] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[sy_II__row] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)
systems_their_conditions[sy_III_row] = (Grp5LL, Gr5isW, Grp6LL, Gr6isW, Grp7LL, Gr7isW, Grp8LL, Gr8isW, Grp9LL, Gr9isW, Gr10LL, G10isW)


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def input_command(sequence):
  end = False

  i = input("Enter number (0-36), or command (U=Undo, X=Exit): ")
  if i.lower() == 'x':
    end = True
  elif i.lower() == 'u':
    n = sequence.pop()
  elif i.isdigit() and int(i) >= 0 and int(i) <= 36:
    n = int(i)
    sequence.append(n)
  else:
    pass

  return end

def print_number_sequence(no_seq):
  for n in no_seq[-110:-41]:
    print('% 3d' % n, end='')

  print('%s' % '|', end='')

  for n in no_seq[-41:-25]: 
    print('% 3d' % n, end='')

  print('%s' % '|', end='')

  for n in no_seq[-25:]:
    print('% 3d' % n, end='')

  print()

def print_outcome_sequence(outcome_seq):
  sign_seq = list(map(lambda o: o.value, outcome_seq))
  for s in sign_seq[-150:]:
    print('%s' % s, end='')

def main():
  no_seq = []
  while not input_command(no_seq):
    no_seq = no_seq[-800:]
    for (s, cs) in systems_their_conditions.items():
      outcome_seq = s.process_number_sequence(no_seq)
      for c in cs:
        if c.check_outcome_sequence(outcome_seq):
          print('%s %s' % (s.show_notification(), c.show_notification()), end=' | ')
    print()
    print_number_sequence(no_seq)
    for s in systems_their_conditions.keys():
      outcome_seq = s.process_number_sequence(no_seq)
      print('%s: ' % s.__name__, end='')
      print_outcome_sequence(outcome_seq)
      print()
    input("Press enter to input next number.")
main()