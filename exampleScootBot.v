module botFlipFlop (q, in, clk);
 	output q;
 	reg q;
	input in, clk;

	initial q=1'b0;

	always @(posedge clk)
		q = in;
endmodule

module scootBot(mUp, mRight, mDown, mLeft, lUp, lRight, lDown, lLeft, clk);
	output mUp, mRight, mDown, mLeft;
	input lUp, lRight, lDown, lLeft, clk;
	wire pUp, pRight, pDown, pLeft;

	botFlipFlop fUp(pUp, lUp, clk);
	botFlipFlop fRight(pRight, lRight, clk);
	botFlipFlop fDown(pDown, lDown, clk);
	botFlipFlop fLeft(pLeft, lLeft, clk);
	//buf #50 (pUp,lUp);
	//buf #50 (pRight,lRight);
	//buf #50 (pDown,lDown);
	//buf #50 (fLeft,lLeft);

	or #50 (mUp, lUp, pRight);
	or #50 (mRight, lRight, pUp);
	or #50 (mDown, lDown, !pUp);
	or #50 (mLeft, lLeft, !pRight);
endmodule
