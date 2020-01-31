use strict;

print("Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/\n\n\n");

my $ud_path = $ARGV[0];

while (<STDIN>) {
  chomp $_;
  my ($corp, $code) = split(/\s+/, $_);
  my ($lang, $abbr) = split(/\-/, $corp);
  my $lang_no_spaces = $lang;
  $lang =~ s/_/ /g;

  my $fn = "$ud_path/UD_$corp/README.md";
  if (! -e $fn) {
    $fn = "$ud_path/UD_$corp/README.txt";
  }
  my $license = undef;
  open(F, "<$fn");
  while (<F>) {
    chomp $_;
    if ($_ =~ /^License: (.+)/) {
      $license = $1;
    }
  }
  close(F);
  
  if (! defined($license)) {
    die "No license info for $corp in $fn\n";
  }

  $license =~ s/CC\s+([^0-9]+)\s+(\d+\.\d+)/CC-$1-$2/g;
  $license =~ s/CC\s+([^0-9]+)/CC-$1/g;
  $license =~ s/(GNU\s+)GPL\s+(\d+\.\d+)/GPL-$2/g;
  $license =~ s/\([^\)]+\)//g;
  $license =~ s/\s+\/\s+/ and /g;
  $license =~ s/PD/public domain/g;


  print("Files: TensorFlowTokenizer/ud/tokenizer-$code.* TensorFlowMorphosyntax/ud/morphosyntax-$code.*\n");
  print("Copyright: for list of copyright holders see files in corpus distribution.\n");
  print("License: $license\n");
  print("Comments: Model is generated from Universal Dependencies corpus $corp.\n");

  print("\n");

  print("Files: TensorFlowMorphosyntax/ud/fasttext-$code.bin\n");
  print("Copyright: Facebook Inc.\n");
  print("License: CC-BY-SA-3.0\n");
  print("Comments: Quantized version of fastText embeddings.\n");

  print("\n");
}

