#!/usr/bin/env ruby

require "cgi"
count = 0
cgi = CGI.new("html4")
cgi.out { count.to_s }
