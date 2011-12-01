module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;
	buf #50 (output0_branch00000,input0);
	and #50 (output0_branch00001,input3,input1);
	xor #50 (output0_branch0000,output0_branch00000,output0_branch00001);
	buf #50 (output0_branch000,output0_branch0000);
	buf #50 (output0_branch0010,input3);
	buf #50 (output0_branch001,output0_branch0010);
	xor #50 (output0_branch00,output0_branch000,output0_branch001);
	not #50 (output0,output0_branch00);

	or #50 (output1,input1,input0);

	or #50 (output2_branch0000,input0,input0);
	buf #50 (output2_branch0001,input1);
	and #50 (output2_branch000,output2_branch0000,output2_branch0001);
	buf #50 (output2_branch00,output2_branch000);
	buf #50 (output2_branch0100,input0);
	buf #50 (output2_branch01011000000,input0);
	nand #50 (output2_branch0101100000,output2_branch01011000000,input0);
	not #50 (output2_branch010110000,output2_branch0101100000);
	or #50 (output2_branch01011000,output2_branch010110000,input0);
	buf #50 (output2_branch01011001,input1);
	and #50 (output2_branch0101100,output2_branch01011000,output2_branch01011001);
	buf #50 (output2_branch010110,output2_branch0101100);
	buf #50 (output2_branch010111,input0);
	nand #50 (output2_branch01011,output2_branch010110,output2_branch010111);
	or #50 (output2_branch0101,input0,output2_branch01011);
	nand #50 (output2_branch010,output2_branch0100,output2_branch0101);
	not #50 (output2_branch01,output2_branch010);
	nand #50 (output2,output2_branch00,output2_branch01);

	buf #50 (output3_branch00000,input3);
	not #50 (output3_branch0000,output3_branch00000);
	nand #50 (output3_branch00011,input2,input1);
	or #50 (output3_branch0001,input0,output3_branch00011);
	and #50 (output3_branch000,output3_branch0000,output3_branch0001);
	buf #50 (output3_branch0010,input3);
	not #50 (output3_branch001,output3_branch0010);
	and #50 (output3_branch00,output3_branch000,output3_branch001);
	or #50 (output3_branch011,input3,input3);
	or #50 (output3_branch01,input0,output3_branch011);
	nand #50 (output3,output3_branch00,output3_branch01);


endmodule