{
    description = "Python OpenCV Development Environment";

	inputs = {
		nixpkgs = { 
            url = "github:nixos/nixpkgs/nixos-unstable"; 
        };
        flake-utils = {
            url = "github:numtide/flake-utils";
        };
	};

	outputs = { nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system: 
        let
            pkgs = import nixpkgs {
                inherit system;
            };
            pythonEnvironment = pkgs.python3.withPackages (ps: with ps; [ 
                numpy
                (opencv4.override { enableGtk2 = true; })
            ]);
        in
        {
            devShell = pythonEnvironment.env;
        }
    ); 
}