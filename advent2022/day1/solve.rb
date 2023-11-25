#!/usr/bin/ruby
#
# Solution for Advent of Code 2022 puzzle #1: https://adventofcode.com/2022/day/1
#
# The elves are on a trek searching for magical reindeer food. Determine which
# elf is worth the most calories in case cannibalism becomes necessary.
#

class Elf
  def initialize
    @calories = 0
  end

  def add_calories(value)
    @calories += value
  end

  def fatness
    @calories
  end

  def to_s
    @calories.to_s
  end

  def <=>(other)
    if @calories == other.fatness
      0
    elsif @calories > other.fatness
      1
    else
      -1
    end
  end
end

# Find fattest elf.
$SANTA = Elf.new
array = []
File.open('input.txt') do |file|
  loop do
    elf = Elf.new
    file.each do |line|
      break if line == "\n"

      elf.add_calories(line.to_i)
    end
    $SANTA = elf if elf.fatness > $SANTA.fatness
    array.push(elf)
    break if file.eof?
  end
end

# Part 1
puts "The most well prepared elf for the crossing the Donner Pass is worth #{$SANTA} calories."

# Part 2
total = array.sort.reverse.take(3).sum(&:fatness)
puts "The top 3 most well prepared elves are worth #{total} calories."
