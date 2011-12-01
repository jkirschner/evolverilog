module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	not #50 (output0_branch00,input1);
	or #50 (output0_branch0110,input1,input2);
	nand #50 (output0_branch011,output0_branch0110,input1);
	or #50 (output0_branch01,input0,output0_branch011);
	or #50 (output0,output0_branch00,output0_branch01);

	not #50 (output1_branch0000,input3);
	nand #50 (output1_branch000,output1_branch0000,input3);
	not #50 (output1_branch00,output1_branch000);
	not #50 (output1_branch0100,input1);
	nand #50 (output1_branch010,output1_branch0100,input0);
	buf #50 (output1_branch01,output1_branch010);
	nand #50 (output1,output1_branch00,output1_branch01);

	and #50 (output2_branch00,input0,input2);
	or #50 (output2,output2_branch00,input2);

	buf #50 (output3_branch0000,input2);
	not #50 (output3_branch000,output3_branch0000);
	nand #50 (output3_branch0010,input0,input3);
	nand #50 (output3_branch0011,input1,input1);
	and #50 (output3_branch001,output3_branch0010,output3_branch0011);
	or #50 (output3_branch00,output3_branch000,output3_branch001);
	buf #50 (output3,output3_branch00);


endmodule