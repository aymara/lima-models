use strict;

print("cmake_minimum_required(VERSION 3.12.1)\n\n\n");

while (<STDIN>) {
  chomp $_;
  my ($corp, $code) = split(/\s+/, $_);
  my ($lang, $abbr) = split(/\-/, $corp);
  my $lang_no_spaces = $lang;
  $lang =~ s/_/ /g;

  print <<EOT;
install(
    FILES
        tokenizer-$code.conf
        tokenizer-$code.model
    COMPONENT
        tokenizer-ud-$code
    DESTINATION
        share/apps/lima/resources/TensorFlowTokenizer/ud/
)

cpack_add_component(tokenizer-ud-$code
    DISPLAY_NAME
        "UD / $lang"
    GROUP
        $lang_no_spaces
)


EOT
}

