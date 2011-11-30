module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	buf #50 (output0_branch0100,input2);
	nand #50 (output0_branch0101,input0,input3);
	or #50 (output0_branch010,output0_branch0100,output0_branch0101);
	xor #50 (output0_branch01,output0_branch010,input3);
	xor #50 (output0,input3,output0_branch01);

	or #50 (output1_branch0000,input0,input0);
	and #50 (output1_branch0001,input2,input2);
	xor #50 (output1_branch000,output1_branch0000,output1_branch0001);
	not #50 (output1_branch00,output1_branch000);
	buf #50 (output1_branch0100,input0);
	and #50 (output1_branch010,output1_branch0100,input1);
	and #50 (output1_branch0110,input2,input3);
	buf #50 (output1_branch0111,input2);
	or #50 (output1_branch011,output1_branch0110,output1_branch0111);
	nand #50 (output1_branch01,output1_branch010,output1_branch011);
	nand #50 (output1,output1_branch00,output1_branch01);

	not #50 (output2_branch0100,input3);
	not #50 (output2_branch010,output2_branch0100);
	not #50 (output2_branch0110,input0);
	not #50 (output2_branch011,output2_branch0110);
	xor #50 (output2_branch01,output2_branch010,output2_branch011);
	nand #50 (output2,input3,output2_branch01);

	not #50 (output3,input3);


endmodule