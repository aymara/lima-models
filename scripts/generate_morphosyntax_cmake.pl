use strict;

print("cmake_minimum_required(VERSION 3.12.1)\n\n\n");

while (<STDIN>) {
  chomp $_;
  my ($corp, $code) = split(/\s+/, $_);
  my ($lang, $abbr) = split(/\-/, $corp);
  my $lang_no_spaces = $lang;
  $lang =~ s/_/ /g;

  print <<EOT;
get_filename_component(real_embd_path fasttext-$code.bin REALPATH)
get_filename_component(embd_fn \${real_embd_path} NAME)

install(
    FILES
        morphosyntax-$code.conf
        morphosyntax-$code.model
    COMPONENT
        morphosyntax-ud-$code
    DESTINATION
        share/apps/lima/resources/TensorFlowMorphoSyntax/ud/
)

install(
    FILES
        \${real_embd_path}
    RENAME
        fasttext-$code.bin
    COMPONENT
        morphosyntax-ud-$code
    DESTINATION
        share/apps/lima/resources/TensorFlowMorphoSyntax/ud/
)

cpack_add_component(morphosyntax-ud-$code
    DISPLAY_NAME
        "UD Analysis: $lang"
    GROUP
        $lang_no_spaces
)

EOT
}

