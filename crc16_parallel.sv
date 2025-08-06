module crc16_parallel (
    input wire clk,
    input wire reset,
    input wire enable,
    input wire [15:0] data_in,
    output reg [15:0] crc_out
);

    reg [15:0] crc;
    integer i;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            crc <= 16'hFFFF;  // Standard init value for CRC-CCITT
        end else if (enable) begin
            crc = crc_out;
            for (i = 0; i < 16; i = i + 1) begin
                if ((crc[15] ^ data_in[15 - i]) == 1'b1)
                    crc = (crc << 1) ^ 16'h1021;
                else
                    crc = crc << 1;
            end
            crc_out <= crc;
        end
    end

endmodule
