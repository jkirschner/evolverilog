module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	or #50 (output0_branch0010,input0,input3);
	not #50 (output0_branch001,output0_branch0010);
	nand #50 (output0_branch00,input2,output0_branch001);
	not #50 (output0,output0_branch00);

	buf #50 (output1,input1);

	not #50 (output2_branch00,input2);
	or #50 (output2,output2_branch00,input2);

	or #50 (output3_branch0000,input3,input2);
	buf #50 (output3_branch0001010,input1);
	or #50 (output3_branch000101,output3_branch0001010,input0);
	xor #50 (output3_branch00010,input3,output3_branch000101);
	xor #50 (output3_branch0001,output3_branch00010,input0);
	and #50 (output3_branch000,output3_branch0000,output3_branch0001);
	buf #50 (output3_branch00,output3_branch000);
	not #50 (output3_branch0100,input1);
	buf #50 (output3_branch0101,input3);
	nand #50 (output3_branch010,output3_branch0100,output3_branch0101);
	nand #50 (output3_branch01,output3_branch010,input0);
	and #50 (output3,output3_branch00,output3_branch01);


endmodule