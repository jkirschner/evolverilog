module delme(output0,output1,input0,input1,input2,input3);

	output output0,output1;
	input input0,input1,input2,input3;
	not #50 (output0_branch0000,input1);
	xor #50 (output0_branch0001,input3,input0);
	xor #50 (output0_branch000,output0_branch0000,output0_branch0001);
	not #50 (output0_branch00,output0_branch000);
	not #50 (output0_branch0100,input1);
	not #50 (output0_branch010,output0_branch0100);
	buf #50 (output0_branch01,output0_branch010);
	xor #50 (output0,output0_branch00,output0_branch01);

	xor #50 (output1_branch0000,input2,input3);
	not #50 (output1_branch0001,input1);
	xor #50 (output1_branch000,output1_branch0000,output1_branch0001);
	or #50 (output1_branch00,output1_branch000,input2);
	not #50 (output1_branch0100,input1);
	not #50 (output1_branch010,output1_branch0100);
	xor #50 (output1_branch01,output1_branch010,input3);
	or #50 (output1,output1_branch00,output1_branch01);


endmodule