//This scootbot is a diagonal crawler
//It solved the gathering problem of:
//0010101001 * 10 of this row
//the general behavior - it moves up and left, and when it sees something to its right it just moves right.
//On the third run of a 20 generation limited evolution simulation, this solution in generation 13 was the first total solution to the map.
//I'd like to point out that thanks to a simple self-xor, this bot never moves down.

module scootBot(output0,output1,output2,output3,input0,input1,input2,input3,input4);

	output output0,output1,output2,output3;
	input input0,input1,input2,input3,input4;
	not #50 (output0,input1);

	not #50 (output1_branch00,input1);
	buf #50 (output1_branch010,input3);
	buf #50 (output1_branch01,output1_branch010);
	nand #50 (output1,output1_branch00,output1_branch01);

	xor #50 (output2,input1,input1);

	not #50 (output3,input1);


endmodule