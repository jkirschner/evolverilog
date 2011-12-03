module scootBot(output0,output1,output2,output3,input0,input1,input2,input3,input4);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3,input4;
	or #50 (output0_branch00000,input4,input4);
	buf #50 (output0_branch00001,input2);
	and #50 (output0_branch0000,output0_branch00000,output0_branch00001);
	or #50 (output0_branch00011,input4,input2);
	or #50 (output0_branch0001,input0,output0_branch00011);
	nand #50 (output0_branch000,output0_branch0000,output0_branch0001);
	not #50 (output0_branch00,output0_branch000);
	not #50 (output0,output0_branch00);

	not #50 (output1_branch00,input4);
	buf #50 (output1_branch010,input3);
	buf #50 (output1_branch01,output1_branch010);
	nand #50 (output1,output1_branch00,output1_branch01);

	xor #50 (output2_branch01,input1,input1);
	xor #50 (output2,input1,output2_branch01);

	not #50 (output3,input1);


endmodule