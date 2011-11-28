module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;

	wire output0,output1,output2,output3;

	buf #50 (output0,input1);
	or #50 (output1,input0,input3);
	nand #50 (output2,input1,input2);
	xor #50 (output3,input3,input0);

endmodule