# Beispiel VSCode mit Pytest

### Pytest

https://docs.pytest.org/en/latest/

https://pypi.org/project/pytest/

### Pytest installieren

Terminal im Stammverzeichnis des Repostories

>uv add pytest

### Pytest starten 

Terminal im Stammverzeichnis des Repostories

>uv run pytest _30_Verschiedenes/VSCode_Pytest_example/test -q


# .vscode\settings.json

In der Datei _.vscode\settings.json_ wird mit dem Parameter 
_python.testing.pytestArgs_ das Verzeichnis angegeben, wo nach Unittests gesucht werden soll:

```json
{
    "python.testing.pytestArgs": [
        "_30_Verschiedenes/VSCode_Pytest_example/test"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

