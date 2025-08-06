import csv

input_csv = "crc_output.csv"
output_stil = "crc_patterns_with_timing.stil"

def to_bin(val, bits):
    return format(int(val, 16), f'0{bits}b')

with open(input_csv, 'r') as infile, open(output_stil, 'w') as outfile:
    reader = csv.DictReader(infile)
    
    outfile.write("STIL 1.0;\n\n")

    # Signals
    outfile.write("Signals {\n")
    outfile.write("    clk, data_in[15:0], crc_out[15:0];\n")
    outfile.write("};\n\n")

    # Timing info
    outfile.write("SignalGroups {\n")
    outfile.write("    inputs = \"data_in\";\n")
    outfile.write("    outputs = \"crc_out\";\n")
    outfile.write("};\n\n")

    outfile.write("ClockDefs {\n")
    outfile.write("    clk {\n")
    outfile.write("        Period 100ns;\n")
    outfile.write("        Waveform { 0ns Low; 50ns High; }\n")
    outfile.write("    }\n")
    outfile.write("};\n\n")

    outfile.write("WaveformTable WT {\n")
    outfile.write("    Period 100ns;\n")
    outfile.write("    Waveforms {\n")
    outfile.write("        data_in   { 0ns D; }\n")
    outfile.write("        crc_out   { 0ns C; }\n")
    outfile.write("    }\n")
    outfile.write("};\n\n")

    # Timing reference
    outfile.write("Timing {\n")
    outfile.write("    TimingSpec \"ts1\" {\n")
    outfile.write("        WaveformTable WT;\n")
    outfile.write("        ScanWaveform default {\n")
    outfile.write("            Clocks = \"clk\";\n")
    outfile.write("        }\n")
    outfile.write("    }\n")
    outfile.write("};\n\n")

    # Pattern section
    outfile.write("PatternBurst burst1 {\n")
    outfile.write("    TimingSpec ts1;\n")

    for row in reader:
        data_in = row['Data_in'].lower()
        crc_out = row['CRC_out'].lower()

        # skip invalids
        if 'x' in data_in or 'x' in crc_out:
            continue

        data_bin = to_bin(data_in, 16)
        crc_bin = to_bin(crc_out, 16)

        vector = f'1 {data_bin} {crc_bin}'
        outfile.write(f'    Vector ({vector});\n')

    outfile.write("};\n")
