`include "exampleScootBot.v"

module scootBotSimulator;

	localparam WIDTH = 10;
	localparam HEIGHT = 10;
	localparam NUM_STEPS = 100;
	integer x = WIDTH/2;
	integer y = HEIGHT/2;
	wire mUp, mRight, mDown, mLeft;
	reg clk;
	reg [HEIGHT-1:0] a[WIDTH-1:0];
	reg lUp, lRight, lDown, lLeft;
	integer i;

	scootBot uut (mUp, mRight, mDown, mLeft, lUp, lRight, lDown, lLeft, clk);

	initial
	begin
		for (i = 0; i < WIDTH; i = i + 1) begin
			a[i] = 'b0010101001;
		end

		repeat(NUM_STEPS) begin
			$display("x: %d\ty: %d", x, y);
			if (a[x][y] == 1'b1) begin
				$display("Picked one up!");
				a[x][y]=1'b0;
			end
			
			lUp=a[x][(y+1)%HEIGHT];
			lRight=a[(x+1)%WIDTH][y];
			lDown=a[x][(y-1)%HEIGHT];
			lLeft=a[(x-1)%WIDTH][y];
			
			#3000;
			x = (x+mRight-mLeft)%WIDTH;
			y = (y+mUp-mDown)%HEIGHT;
		end
	end

	always
		#200 clk=!clk;

endmodule
