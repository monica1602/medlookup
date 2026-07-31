@echo off
title MedLookup - Servidor
echo.
echo  ==========================================
echo   MedLookup - Iniciando servidor...
echo  ==========================================
echo.

cd /d "%~dp0"

:: Verifica se Python esta disponivel
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado. Instale o Python em python.org
    pause
    exit /b 1
)

:: Abre o navegador depois de 2 segundos (em paralelo)
start "" cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:5000"

echo  Servidor rodando em: http://localhost:5000
echo  Pressione CTRL+C para parar o servidor.
echo.

python app.py

pause
