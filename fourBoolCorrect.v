module fourBool(output0,output1,output2,output3,input0,input1,input2,input3);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3;

	wire output0,output1,output2,output3;

	//and #50 (output0,input1,input2);

	buf #50 (output1,1);

	//nand #50 (output2,input1,input0);
	
	//xor #50 (output3, input3, input2);

   buf #50 (output2, 1);
   buf #50 (output3, 1);
   buf #50 (output0, 1);
   
endmodule
