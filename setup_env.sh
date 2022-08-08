#!/bin/bash


RED='\033[0;31m'
NC='\033[0m'
echo -e "${RED}=== Starting setup environment script ===${NC}"

#################################################################################################
# PYENV INSTALL
# Git should be installed in all ubuntu systems, but may be a dependency.

echo -e "${RED}=== Installing Pyenv ===${NC}"
if command -v pyenv >/dev/null; then
    # Add check for update in future
    echo -e "${RED}=== Pyenv already installed, skipping install ===${NC}"
else
    echo -e "${RED}=== Pyenv NOT installed, installing pyenv now ===${NC}"
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    PYENV_ROOT="$HOME/.pyenv"
    PATH="$PYENV_ROOT/bin:$PATH"
    # exec "$SHELL"
fi


# For each supported version: [Install, upgrade pip, install pipx]
#  ARE WE ONLY GETTING FROM PYPROJECT.TOML?
# Currently only gets one version
# version=$(sed -n 's/^ *python.*=.*"^\([^"]*\)".*/\1/p' pyproject.toml)
#################################################################################################
# PYENV INSTALL

supported_versions=$(grep python pyproject.toml | tr -d '^ python= "' | tr ',' '\n')
for version in $supported_versions; do
    echo -e "${RED}=== Installing Python $version ===${NC}"
    pyenv install $version

    echo -e "${RED}=== Loading Version [$ver] ===${NC}"
    pyenv local $ver
	pyenv versions

    echo -e "${RED}=== Upgrading Pip ===${NC}"
    python -m pip install --upgrade pip

    echo -e "${RED}=== Installing Pipx ===${NC}"
    pip install pipx

    echo -e "${RED}=== Ensure Pipx Path ===${NC}" 
	pipx ensurepath

    
done

#################################################################################################
# POETRY INSTALL
# Git should be installed in all ubuntu systems, but may be a dependency.

echo -e "${RED}=== Installing Poetry ===${NC}"

if command -v poetry >/dev/null; then
    echo -e "${RED}=== Poetry already installed, upgrading ===${NC}"
    pipx upgrade poetry
else
    echo -e "${RED}=== Poetry NOT installed, installing pyenv now ===${NC}"
    pipx install poetry
fi

#################################################################################################
# FULL CONFIGURATION

echo -e "${RED}=== Configuring Initial Environment ===${NC}"
echo -e "${RED}=== Installing Environment ===${NC}"
poetry install

