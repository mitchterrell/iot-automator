#Requires -RunAsAdministrator

# Color Printing Methods
function Green
{
    process { Write-Host $_ -ForegroundColor Green }
}

function Red
{
    process { Write-Host $_ -ForegroundColor Red }
}

function Cyan
{
    process { Write-Host $_ -ForegroundColor Cyan }
}

#################################################################################################
# PYENV INSTALL

Write-Output "=== Installing Pyenv ===" | Cyan

# Check if pyenv already installed
$cmdName = "pyenv"

if (Get-Command $cmdName -errorAction SilentlyContinue)
{
    Write-Output "=== $cmdName exists, skipping install ===" | Green
}
else
{
	# If not installed, install it and set variables
	Write-Output "=== $cmdName DOES NOT exist, installing pyenv ===" | Red
	git clone https://github.com/pyenv-win/pyenv-win.git "$HOME\.pyenv"	
	
	# Setup Pyenv paths
	[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
	[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
	[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
	Write-Output "=== Successfully set PYENV, PYENV_ROOT and PYENV_HOME env variables ===" | Green

}

# For each supported version: [Install, upgrade pip, install pipx]
$supported_versions = '3.7.2', '3.10.5'
foreach ($ver in $supported_versions)
{
	Write-Output "=== Installing Version [$ver] ===" | Green
	pyenv install $ver
	
	Write-Output "=== Loading Version [$ver] ===" | Green
	pyenv local $ver
	pyenv versions
	
	Write-Output "=== Upgrading Pip ===" | Green
	python -m pip install --upgrade pip
	
	Write-Output "=== Installing Pipx ===" | Green
	pip install pipx --quiet
	
	Write-Output "=== Ensure Pipx Path ===" | Green
	pipx ensurepath
	
	#Refresh Path
	$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

#################################################################################################
# POETRY INSTALL

Write-Output "=== Installing Poetry ===" | Cyan

# Check if poetry already installed
$cmdName = "poetry"

if (Get-Command $cmdName -errorAction SilentlyContinue)
{
    Write-Output "=== $cmdName exists, skipping install, checking for upgrade ===" | Green
	
	pipx upgrade poetry
}
else
{
	# If not installed, install it and set variables
	Write-Output "=== $cmdName DOES NOT exist, installing Poetry ===" | Red
	
	pipx install poetry

}

#Refresh Path (needed for Poetry)
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

#################################################################################################
# FULL CONFIGURATION


Write-Output "=== Configuring Initial Environment ===" | Cyan

Write-Output "=== Installing Environment ===" | Green
poetry install