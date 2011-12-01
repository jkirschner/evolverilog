module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	nand #50 (output0_branch000101,input0,input0);
	or #50 (output0_branch00010,input2,output0_branch000101);
	xor #50 (output0_branch000110,input2,input3);
	not #50 (output0_branch00011100,input2);
	buf #50 (output0_branch000111010,input0);
	buf #50 (output0_branch00011101,output0_branch000111010);
	xor #50 (output0_branch0001110,output0_branch00011100,output0_branch00011101);
	xor #50 (output0_branch000111,output0_branch0001110,input2);
	nand #50 (output0_branch00011,output0_branch000110,output0_branch000111);
	and #50 (output0_branch0001,output0_branch00010,output0_branch00011);
	or #50 (output0_branch000,input2,output0_branch0001);
	and #50 (output0_branch00,output0_branch000,input1);
	or #50 (output0_branch01,input0,input2);
	and #50 (output0,output0_branch00,output0_branch01);

	buf #50 (output1_branch000,input1);
	buf #50 (output1_branch00,output1_branch000);
	buf #50 (output1,output1_branch00);

	or #50 (output2_branch0000,input1,input3);
	and #50 (output2_branch0001,input0,input1);
	nand #50 (output2_branch000,output2_branch0000,output2_branch0001);
	buf #50 (output2_branch00,output2_branch000);
	and #50 (output2_branch0100,input1,input1);
	and #50 (output2_branch01010,input1,input1);
	nand #50 (output2_branch01011,input1,input1);
	or #50 (output2_branch0101,output2_branch01010,output2_branch01011);
	or #50 (output2_branch010,output2_branch0100,output2_branch0101);
	not #50 (output2_branch0110,input1);
	and #50 (output2_branch0111,input2,input2);
	nand #50 (output2_branch011,output2_branch0110,output2_branch0111);
	xor #50 (output2_branch01,output2_branch010,output2_branch011);
	or #50 (output2,output2_branch00,output2_branch01);

	not #50 (output3_branch0000,input2);
	not #50 (output3_branch0001,input3);
	xor #50 (output3_branch000,output3_branch0000,output3_branch0001);
	buf #50 (output3_branch00,output3_branch000);
	and #50 (output3_branch01000,input1,input2);
	xor #50 (output3_branch0100,output3_branch01000,input2);
	and #50 (output3_branch010,output3_branch0100,input1);
	not #50 (output3_branch011,input3);
	and #50 (output3_branch01,output3_branch010,output3_branch011);
	or #50 (output3,output3_branch00,output3_branch01);


endmodule