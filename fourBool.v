module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	nand #50 (output0_branch0000100,input0,input0);
	buf #50 (output0_branch000010,output0_branch0000100);
	xor #50 (output0_branch00001100,input3,input3);
	buf #50 (output0_branch0000110,output0_branch00001100);
	and #50 (output0_branch000011,output0_branch0000110,input1);
	and #50 (output0_branch00001,output0_branch000010,output0_branch000011);
	nand #50 (output0_branch0000,input0,output0_branch00001);
	or #50 (output0_branch000,output0_branch0000,input1);
	and #50 (output0_branch0010,input0,input2);
	or #50 (output0_branch001,output0_branch0010,input3);
	and #50 (output0_branch00,output0_branch000,output0_branch001);
	not #50 (output0_branch0101,input0);
	xor #50 (output0_branch010,input1,output0_branch0101);
	xor #50 (output0_branch01,output0_branch010,input1);
	nand #50 (output0,output0_branch00,output0_branch01);

	not #50 (output1_branch00,input2);
	not #50 (output1,output1_branch00);

	not #50 (output2_branch0000,input0);
	or #50 (output2_branch0001100,input2,input1);
	or #50 (output2_branch000110,output2_branch0001100,input0);
	not #50 (output2_branch00011,output2_branch000110);
	or #50 (output2_branch0001,input1,output2_branch00011);
	and #50 (output2_branch000,output2_branch0000,output2_branch0001);
	xor #50 (output2_branch00,output2_branch000,input1);
	nand #50 (output2,output2_branch00,input0);

	buf #50 (output3_branch0001,input3);
	or #50 (output3_branch000,input0,output3_branch0001);
	not #50 (output3_branch0010,input2);
	buf #50 (output3_branch00111,input1);
	or #50 (output3_branch0011,input0,output3_branch00111);
	or #50 (output3_branch001,output3_branch0010,output3_branch0011);
	nand #50 (output3_branch00,output3_branch000,output3_branch001);
	buf #50 (output3,output3_branch00);


endmodule