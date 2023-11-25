#!/usr/bin/ruby
# frozen_string_literal: true

LIB_PATH = File.join([File.dirname(__FILE__), '../../lib/ruby']).freeze
$LOAD_PATH.unshift(LIB_PATH)
require 'intcode'

DATA = File.join([File.dirname(__FILE__), '../data/input.txt']).freeze
CPU_RESULT = 19690720

cpu = IntcodeCPU.new(DATA)
cpu.patch(0x01, 0x0c)
cpu.patch(0x02, 0x02)
puts "CPU return value for input 1202: #{cpu.run}"

noun, verb = cpu.run_expect(CPU_RESULT)
input = 100 * noun + verb
puts "CPU input for #{CPU_RESULT}: #{input}."
