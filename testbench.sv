`timescale 1ns / 1ps

module testbench;
    reg clk = 0;
    reg reset = 1;
    reg enable = 0;
    reg [15:0] data_in;
    wire [15:0] crc_out;

    integer csv;

    // Instantiate CRC module
    crc16_parallel uut (
        .clk(clk),
        .reset(reset),
        .enable(enable),
        .data_in(data_in),
        .crc_out(crc_out)
    );

    // Clock generator
    always #5 clk = ~clk;

    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, testbench);

        csv = $fopen("crc_output.csv", "w");
        $fwrite(csv, "Time_ns,Data_in,CRC_out\n");

        #10 reset = 0;

        apply_input(16'hABCD);
        apply_input(16'h1234);
        apply_input(16'h0000);
        apply_input(16'hFFFF);
        apply_input(16'h8000);

        #50 $fclose(csv);
        #10 $finish;
    end

    task apply_input(input [15:0] data);
        begin
            @(negedge clk);
            data_in = data;
            enable = 1;
            @(negedge clk);
            enable = 0;
        end
    endtask

    always @(posedge clk) begin
        if (enable) begin
            $fwrite(csv, "%0t,%h,%h\n", $time, data_in, crc_out);
        end
    end
endmodule
