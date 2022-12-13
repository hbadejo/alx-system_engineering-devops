#!/usr/bin/env ruby

##Requirements:

#The regular expression must be exactly matching a string that starts with h ends with n... 
#and can have any single character in between
#Using the project instructions, create a Ruby script that accepts one argument and... 
#pass it to a regular expression matching method

puts ARGV[0].match(/^h.n$/)