#!/usr/bin/env ruby

#For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, 
#a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on 
#the TextMe app text messages transactions.

##Requirements:

#Your script should output: [SENDER],[RECEIVER],[FLAGS]
#The sender phone number or name (including country code if present)
#The receiver phone number or name (including country code if present)
#The flags that were used

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
