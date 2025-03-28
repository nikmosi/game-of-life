{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    pre-commit-hooks.url = "github:cachix/pre-commit-hooks.nix";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      pre-commit-hooks,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        checks = {
          pre-commit-check = pre-commit-hooks.lib.${system}.run {
            src = ./.;
            hooks = {
              isort.enable = true;
              ruff.enable = true;
              ruff-format.enable = true;
              end-of-file-fixer.enable = true;
              check-added-large-files.enable = true;
              trim-trailing-whitespace.enable = true;
              check-yaml.enable = true;
              fix-byte-order-marker.enable = true;
              convco.enable = true;
              trufflehog = {
                stages = [ "pre-push" ];
                enable = true;
              };
            };
          };
        };

        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            python312
            uv
          ];
          buildInputs = self.checks.${system}.pre-commit-check.enabledPackages;
          shellHook = ''
            ${self.checks.${system}.pre-commit-check.shellHook}
            exec fish
          '';
        };
      }
    );
}
