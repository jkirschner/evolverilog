module fourBitAdder(out4,out3,out2,out1,out0,a3,a2,a1,a0,b3,b2,b1,b0);

  output out0,out1,out2,out3,out4;
  input a0,a1,a2,a3;
  input b0,b1,b2,b3;
  wire carry1,carry2,carry3;

  oneBitAdder #50 z0 (out0, carry1, a0, b0, 0);
  oneBitAdder #50 z1 (out1, carry2, a1, b1, carry1);
  oneBitAdder #50 z2 (out2, carry3, a2, b2, carry2);
  oneBitAdder #50 z3 (out3, out4, a3, b3, carry3);

endmodule

module oneBitAdder(result, carry, a, b, c);

  output result, carry;
  input a, b, c;
  wire cmp1;
  
  and #50 (carry, a, b, c);
  xor #50 (cmp1, a, b);
  xor #50 (result, cmp1, c);

endmodule

module half_adder(sum, carry, A, B);
	output sum, carry;
	input A, B;
	
	parameter delay = 50;
	
	xor #delay g1(sum, A, B);
	and #delay g2(carry, A, B);
endmodule

module full_adder(sum, carry, A, B, C);
	output sum, carry;
	input A, B, C;
	wire carry_1, carry_2, internal_sum;
	
	parameter delay = 50;
	
	half_adder ha1(internal_sum, carry_1, A, B);
	half_adder ha2(sum, carry_2, internal_sum, C);
	or #delay res(carry, carry_1, carry_2);
endmodule

module adder_4(carryout,sum3,sum2,sum1,sum0,a3,a2,a1,a0,b3,b2,b1,b0);
    output carryout,sum3,sum2,sum1,sum0;
    input a3,a2,a1,a0,b3,b2,b1,b0;
	
    wire[2:0] carry;
	
	full_adder add0 (sum0, carry[0], a0, b0, 0);
	full_adder add1 (sum1, carry[1], a1, b1, carry[0]);
	full_adder add2 (sum2, carry[2], a2, b2, carry[1]);
	full_adder add3 (sum3, carryout, a3, b3, carry[2]);
endmodule