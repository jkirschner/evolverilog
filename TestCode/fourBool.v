module fourBool(e,f,g,h,A,B,C,D);

    output e,f,g,h;
    input A,B,C,D;

    and #50 (e,A,B);
    or #50 (f,A,B);
    not #50 (g,C);
    buf #50 (h,D);
		

endmodule
