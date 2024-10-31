$VenvPath="venv"

if (-Not (Test-Path -Path $VenvPath))
{
	python -m venv $VenvPath
		
}


#attivo il venv
.\venv\scripts\activate.ps1 


pip install -r requirements.txt


python game.py
