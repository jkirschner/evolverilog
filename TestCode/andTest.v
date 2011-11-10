module andTest;
	
    reg A,B;
    wire out;
    
    parameter settleDelay = 10000;
    
    trivialAnd uut (out,A,B);
    
    integer i;
    
    initial
    begin
        for (i = 0; i < 4; i = i + 1) begin
            {A,B} = i;
            #settleDelay
            $display ("%d,%d,%d",A,B,out);
        end
    end
    
endmodule

module trivialAnd(out,A,B);

    output out;
    input A,B;

    and #50 (out,A,B);

endmodule
