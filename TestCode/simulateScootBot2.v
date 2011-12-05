`include "scootBot.v"

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
		a[0] = 'b0010101110;
		a[1] = 'b0011011001;
		a[2] = 'b1011011001;
		a[3] = 'b0101000101;
		a[4] = 'b1100111000;
		a[5] = 'b0101111010;
		a[6] = 'b1001010110;
		a[7] = 'b1010110011;
		a[8] = 'b1100101000;
		a[9] = 'b0000011011;
		
		repeat(NUM_STEPS) begin
		
			$display("%d,%d", x, y);
			if (a[x][y] == 1'b1) begin
				$display("PickedUp");
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
		$finish;
	end

	always
		#200 clk=!clk;

endmodule
