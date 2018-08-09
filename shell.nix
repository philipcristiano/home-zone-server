let
  pkgs = import <nixpkgs> {};
  stdenv = pkgs.stdenv;

  # Get from github
  ghpkgs = pkgs.callPackage (fetchTarball https://github.com/philipcristiano/dev-env/archive/v0.0.12.tar.gz) {};

in stdenv.mkDerivation {
  name = "env";
  buildInputs = [ ghpkgs.cfssl
                  pkgs.git-crypt
                  pkgs.python2
                  pkgs.openssl
                  pkgs.libffi
                  pkgs.postgresql100
                  pkgs.python27Packages.virtualenv
                  # pkgs.python27Packages.psycopg2 # Need a newer version than nix has :/
                  # pkgs.ansible
                ];
}
