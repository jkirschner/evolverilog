module scootBot(output0,output1,output2,output3,input0,input1,input2,input3,input4);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3,input4;
	nand #50 (output0,input2,input3);

	xor #50 (output1_branch00,input0,input2);
	not #50 (output1_branch01,input1);
	xor #50 (output1,output1_branch00,output1_branch01);

	and #50 (output2,input4,input1);

	not #50 (output3,input1);


endmodule