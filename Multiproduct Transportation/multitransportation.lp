\ Model Multiproduct Transportation
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  3 x_w1_1_A + 4 x_w1_1_B + 6 x_w1_1_C + 2 x_w1_2_A + 3 x_w1_2_B
   + 5 x_w1_2_C + 4 x_w1_3_A + 2 x_w1_3_B + 4 x_w1_3_C + 5 x_w2_1_A
   + 3 x_w2_1_B + 4 x_w2_1_C + 3 x_w2_2_A + 2 x_w2_2_B + 3 x_w2_2_C
   + 2 x_w2_3_A + 5 x_w2_3_B + 2 x_w2_3_C
Subject To
 R0: x_w1_1_A + x_w2_1_A = 40
 R1: x_w1_1_B + x_w2_1_B = 30
 R2: x_w1_1_C + x_w2_1_C = 50
 R3: x_w1_2_A + x_w2_2_A = 20
 R4: x_w1_2_B + x_w2_2_B = 30
 R5: x_w1_2_C + x_w2_2_C = 20
 R6: x_w1_3_A + x_w2_3_A = 20
 R7: x_w1_3_B + x_w2_3_B = 30
 R8: x_w1_3_C + x_w2_3_C = 30
 R9: x_w1_1_A + x_w1_2_A + x_w1_3_A <= 50
 R10: x_w1_1_B + x_w1_2_B + x_w1_3_B <= 40
 R11: x_w1_1_C + x_w1_2_C + x_w1_3_C <= 60
 R12: x_w2_1_A + x_w2_2_A + x_w2_3_A <= 30
 R13: x_w2_1_B + x_w2_2_B + x_w2_3_B <= 50
 R14: x_w2_1_C + x_w2_2_C + x_w2_3_C <= 40
Bounds
End
