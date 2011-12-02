module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	and #50 (output0_branch0000,input2,input1);
	and #50 (output0_branch0001011000,input2,input1);
	not #50 (output0_branch00010110010,input3);
	and #50 (output0_branch0001011001,output0_branch00010110010,input1);
	xor #50 (output0_branch000101100,output0_branch0001011000,output0_branch0001011001);
	or #50 (output0_branch00010110,output0_branch000101100,input1);
	not #50 (output0_branch0001011,output0_branch00010110);
	xor #50 (output0_branch000101,input3,output0_branch0001011);
	xor #50 (output0_branch00010,input3,output0_branch000101);
	nand #50 (output0_branch0001,output0_branch00010,input0);
	nand #50 (output0_branch000,output0_branch0000,output0_branch0001);
	not #50 (output0_branch00,output0_branch000);
	buf #50 (output0,output0_branch00);

	buf #50 (output1,input1);

	buf #50 (output2_branch000,input0);
	nand #50 (output2_branch00,output2_branch000,input1);
	buf #50 (output2,output2_branch00);

	or #50 (output3_branch000010,input3,input2);
	or #50 (output3_branch00001,output3_branch000010,input0);
	nand #50 (output3_branch0000,input2,output3_branch00001);
	buf #50 (output3_branch000,output3_branch0000);
	not #50 (output3_branch00,output3_branch000);
	xor #50 (output3,output3_branch00,input3);


endmodule