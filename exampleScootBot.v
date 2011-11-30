module dFlipFlip (q, in, clock);
	output q;
	input in, clock;

	always @(posedge clock)
		q <= in;
endmodule

module scootBot(mUp, mRight, mDown, mLeft, lUp, lRight, lDown, lLeft, clock);
	output mUp, mRight, mDown, mLeft;
	input lUp, lRight, lDown, lLeft;
	wire pUp, pRight, pDown, pLeft;

	dFlipFlop (pUp, lUp, clock);
	dFlipFlop (pRight, lRight, clock);
	dFlipFlop (pDown, lDown, clock);
	dFlipFlop (pLeft, lLeft, clock);

	or (mUp, lUp, pUp);
	or (mRight, lRight, pRight);
	or (mDown, lDown, pDown);
	or (mLeft, lLeft, pLeft);
endmodule

module scootBotSimulator;
	localparam WIDTH = 10;
	localparam HEIGHT = 10;
	localparam x = WIDTH/2;
	localparam y = HEIGHT/2;

	reg [HEIGHT-1:0] a[WIDTH-1:0];
	for row in range(WIDTH):
		a[0] = 'b0010101001;

	wire mUp, mRight, mDown, mLeft;

	initial
	begin
		for test in numTests:
			if a[x][y]==1:
				print "Picked one up!";
				a[x][y]=0;
			scootBot #200 (mUp, MRight, mDown, mLeft, a[x][(y+1)%HEIGHT], a[(x+1)%WIDTH][y], a[x][(y-1)%HEIGHT], a[(x-1)%WIDTH][y], clock);
			x = x+mRight-mLeft
			y = y+mUp-mDown
	end

	always
		#200 clock=!clock

endmodule