# CRC16-Parallel-Design-with-ATE-Pattern-Generation-STIL-Format

# CRC16 Parallel Verilog Project (ATE Ready)

This project implements a parallel CRC16 generator in Verilog with a testbench and STIL file for ATE pattern simulation.

## 📁 Files Included

- `crc16_parallel.v` – RTL implementation of a CRC16 generator using polynomial `0x1021` (`x^16 + x^12 + x^5 + 1`)
- `testbench.sv` – Simulation testbench with sample input vectors
- `crc_patterns.stil` – STIL file with test vectors for ATE simulation or pattern import

## 🧪 CRC Configuration

- **Polynomial**: `0x1021` (CRC-CCITT)
- **Initial value**: `0xFFFF`
- **Width**: 16 bits
- **Input width**: 16 bits (parallel)

## ▶️ Simulation Instructions

1. Use `iverilog` to compile:
   ```bash
   iverilog -g2012 crc16_parallel.v testbench.sv -o sim.out
   ```

2. Run simulation:
   ```bash
   vvp sim.out
   ```

3. View waveforms:
   ```bash
   gtkwave dump.vcd
   ```

## 🧾 STIL Pattern Format

The `crc_patterns.stil` file contains a basic `Signals` declaration and `PatternBurst` with input stimulus. You can import it into your ATE environment (e.g., Advantest, Teradyne) to evaluate digital test vector generation.

## 📌 Project Goal

To simulate, verify, and generate ATE-ready patterns for a CRC16 circuit, bridging RTL design and test engineering.

---

