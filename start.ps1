$pythonExe = Get-ChildItem "$HOME\AppData\Local\Programs\Python" -Directory |
    Where-Object { $_.Name -match '^Python(\d+)$' } |
    Sort-Object { [int]($_.Name -replace 'Python','') } -Descending |
    Select-Object -First 1 |
    ForEach-Object { Join-Path $_.FullName "python.exe" }

& $pythonExe -m pip install psutil