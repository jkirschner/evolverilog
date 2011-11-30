module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	buf #50 (output0_branch01010,input2);
	or #50 (output0_branch0101,output0_branch01010,input1);
	or #50 (output0_branch010,input0,output0_branch0101);
	buf #50 (output0_branch0110,input1);
	or #50 (output0_branch0111,input3,input2);
	nand #50 (output0_branch011,output0_branch0110,output0_branch0111);
	nand #50 (output0_branch01,output0_branch010,output0_branch011);
	and #50 (output0,input2,output0_branch01);

	and #50 (output1_branch01000,input2,input0);
	not #50 (output1_branch0100,output1_branch01000);
	and #50 (output1_branch0101,input2,input0);
	nand #50 (output1_branch010,output1_branch0100,output1_branch0101);
	not #50 (output1_branch01,output1_branch010);
	xor #50 (output1,input1,output1_branch01);

	xor #50 (output2_branch000000,input0,input2);
	or #50 (output2_branch000001,input2,input1);
	or #50 (output2_branch00000,output2_branch000000,output2_branch000001);
	not #50 (output2_branch0000,output2_branch00000);
	or #50 (output2_branch0001,input2,input1);
	and #50 (output2_branch000,output2_branch0000,output2_branch0001);
	xor #50 (output2_branch00,output2_branch000,input1);
	nand #50 (output2,output2_branch00,input0);

	buf #50 (output3_branch010,input2);
	buf #50 (output3_branch01,output3_branch010);
	xor #50 (output3,input3,output3_branch01);


endmodule