module f(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	// input comment
	not #50 (output0_branch0000,input0);
	// input comment
	nand #50 (output0_branch000,output0_branch0000,input1);
	not #50 (output0_branch00,output0_branch000);
	// input comment
	or #50 (output0,output0_branch00,input1);

	// input comment

	// input comment
	// input comment
	or #50 (output2_branch0000,input1,input2);
	// input comment
	// input comment
	nand #50 (output2_branch0001,input1,input3);
	or #50 (output2_branch000,output2_branch0000,output2_branch0001);
	// input comment
	or #50 (output2_branch00,output2_branch000,input1);
	buf #50 (output2,output2_branch00);

	// input comment
	buf #50 (output3_branch0000,input1);
	buf #50 (output3_branch000,output3_branch0000);
	buf #50 (output3_branch00,output3_branch000);
	// input comment
	not #50 (output3_branch0100,input2);
	buf #50 (output3_branch010,output3_branch0100);
	// input comment
	buf #50 (output3_branch0110,input0);
	// input comment
	// input comment
	// input comment
	nand #50 (output3_branch011101,input1,input3);
	nand #50 (output3_branch01110,input2,output3_branch011101);
	not #50 (output3_branch0111,output3_branch01110);
	nand #50 (output3_branch011,output3_branch0110,output3_branch0111);
	xor #50 (output3_branch01,output3_branch010,output3_branch011);
	or #50 (output3,output3_branch00,output3_branch01);

endmodule