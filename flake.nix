{
  description = "Python OpenCV Development Environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs { inherit system; };
      python = pkgs.python3;
      pythonEnvironment = python.withPackages (ps: with ps; [
        jupyter
        ipython
        matplotlib
        numpy
        (opencv4.override { enableGtk2 = true; })
      ]);
    in
    {
      devShell = pkgs.mkShell {
        buildInputs = [ pythonEnvironment ];
      };
    }
  );
}
