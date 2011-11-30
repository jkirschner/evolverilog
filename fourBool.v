module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	and #50 (output0_branch0000,input2,input3);
	and #50 (output0_branch000,output0_branch0000,input3);
	not #50 (output0_branch00,output0_branch000);
	or #50 (output0,output0_branch00,input2);

	xor #50 (output1_branch000,input1,input1);
	buf #50 (output1_branch00,output1_branch000);
	xor #50 (output1,output1_branch00,input1);

	buf #50 (output2_branch0001,input2);
	or #50 (output2_branch000,input3,output2_branch0001);
	not #50 (output2_branch00,output2_branch000);
	buf #50 (output2_branch01,input2);
	nand #50 (output2,output2_branch00,output2_branch01);

	buf #50 (output3_branch010,input2);
	or #50 (output3_branch0110,input1,input0);
	nand #50 (output3_branch011,output3_branch0110,input1);
	xor #50 (output3_branch01,output3_branch010,output3_branch011);
	xor #50 (output3,input3,output3_branch01);

	or #50 (output0,input1,input0);
	buf #50 (output1,input1);
	nand #50 (output2,input0,input1);
	xor #50 (output3,input2,input3);

endmodule