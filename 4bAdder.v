module 4bAdder(out4,out3,out2,out1,out0,a3,a2,a1,a0,b3,b2,b1,b0);

  output out0,out1,out2,out3,out4;
  input a0,a1,a2,a3;
  input b0,b1,b2,b3;
  wire carry1,carry2,carry3;

  1bAdder #50 (out0, carry1, a0, b0, 0'1b);
  1bAdder #50 (out1, carry2, a1, b1, carry1);
  1bAdder #50 (out2, carry3, a2, b2, carry2);
  1bAdder #50 (out3, out4, a3, b3, carry3);

endmodule

module 1bAdder(result, carry, a, b, c);
  output result, carry;
  input a, b, c;
  wire cmp1;
  
  and #50 (carry, a, b, c);
  xor #50 (cmp1, a, b);
  xor #50 (result, cmp1, c);  
endmodule
