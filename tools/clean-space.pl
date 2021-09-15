#!/usr/bin/env perl

# cleaning heading spaces, training spaces, double spaces and blank lines
# Ye Kyaw Thu, AI Lab., OPU, Japan
#
# Preparation for KNLP 2016 conf. paper
# e.g. $ perl clean-space.pl <input-file>

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {
        chomp($line);
        $line =~ s/^\s+|\s+$//g;
        $line =~ s/ +/ /g;
         
        print "$line\n";
    }

}

close ($inputFILE);
