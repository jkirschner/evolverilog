module botFlipFlop (q, in, clk);
 	output q;
 	reg q;
	input in, clk;

	always @(posedge clk)
		q <= in;
endmodule

module scootBot(mUp, mRight, mDown, mLeft, lUp, lRight, lDown, lLeft, clk);
	output mUp, mRight, mDown, mLeft;
	input lUp, lRight, lDown, lLeft, clk;
	wire pUp, pRight, pDown, pLeft;

	botFlipFlop fUp(pUp, lUp, clk);
	botFlipFlop fRight(pRight, lRight, clk);
	botFlipFlop fDown(pDown, lDown, clk);
	botFlipFlop fLeft(pLeft, lLeft, clk);

	or #50 (mUp, lUp, pUp);
	or #50 (mRight, lRight, pRight);
	or #50 (mDown, lDown, pDown);
	or #50 (mLeft, lLeft, pLeft);
endmodule