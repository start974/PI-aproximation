with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "Python-Exercice";
  buildInputs = with pkgs; [
    python39
    python39Packages.tkinter
    pipenv
  ];
    shellHook = ''
    SOURCE_DATE_EPOCH=$(date +%s) # required for python wheels
    local venv=$(pipenv --bare --venv &>> /dev/null)
    if [[ -z $venv || ! -d $venv ]]; then
      pipenv install --dev &>> /dev/null
    fi
    export VIRTUAL_ENV=$(pipenv --venv)
    export PIPENV_ACTIVE=1
    export PYTHONPATH="$VIRTUAL_ENV/${pkgs.python3.sitePackages}:$PYTHONPATH"
    export PATH="$VIRTUAL_ENV/bin:$PATH"
    pipenv shell
  '';
}