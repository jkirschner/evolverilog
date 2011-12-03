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

	dFlipFlop #100 (pUp, lUp, clock);
	dFlipFlop #100 (pRight, lRight, clock);
	dFlipFlop #100 (pDown, lDown, clock);
	dFlipFlop #100 (pLeft, lLeft, clock);

	or #50 (mUp, lUp, pUp);
	or #50 (mRight, lRight, pRight);
	or #50 (mDown, lDown, pDown);
	or #50 (mLeft, lLeft, pLeft);
endmodule

module scootBotSimulator;
	localparam WIDTH = 10;
	localparam HEIGHT = 10;
	localparam NUM_STEPS = 100;
	localparam x = WIDTH/2;
	localparam y = HEIGHT/2;

	reg [HEIGHT-1:0] a[WIDTH-1:0];
	integer i;
	
	for (i = 0; i < WIDTH; i = i + 1)
	begin
		a[i] = 'b0010101001;
	end

	wire mUp, mRight, mDown, mLeft;
	reg clock;

	initial
	begin
		repeat(NUM_STEPS) begin
			$display("x: %d\ty: %d", x, y);
			if (a[x][y] == 1'b1) begin
				$display("Picked one up!");
				a[x][y]=1'b0;
			end
			scootBot #2000 sb (mUp, MRight, mDown, mLeft, a[x][(y+1)%HEIGHT], a[(x+1)%WIDTH][y], a[x][(y-1)%HEIGHT], a[(x-1)%WIDTH][y], clock);
			x = (x+mRight-mLeft)%WIDTH;
			y = (y+mUp-mDown)%HEIGHT;
		end
	end

	always
		#200 clock=!clock

endmodule
