# Читаемость и сопровождаемость кода: форматирование и навигация

Учебный проект к курсовой **«Обеспечение читаемости и сопровождаемости кода через средства форматирования и навигации»**. Реальный пример написан на **Python** и демонстрирует отличие автоматического форматирования от структурного разделения модулей, а также навигацию между функциями и тестами.

## Структура

| Путь | Назначение |
| --- | --- |
| `examples/before_format.py` | намеренно неформатированный пример |
| `examples/after_format.py` | эквивалентный читаемый вариант |
| `src/readable_orders/models.py` | данные заявки |
| `src/readable_orders/validation.py` | проверка полей |
| `src/readable_orders/pricing.py` | формула итоговой стоимости |
| `src/readable_orders/service.py` | создание заявки и смена статуса |
| `tests/` | 26 тестовых случаев |
| `tools/metrics.py` | подсчёт простых текстовых показателей |
| `.editorconfig`, `pyproject.toml` | единый стиль и правила Ruff |
| `.vscode/` | рекомендованные расширения и форматирование при сохранении |
| `.github/workflows/quality.yml` | автоматическая проверка оформления и тестов |

## Запуск (Windows PowerShell)

Установите Python 3.10 или новее. Откройте распакованную папку проекта:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest -q
ruff format --check .
ruff check .
python tools/metrics.py
```

Для подготовки нового или изменённого файла: `ruff format .` и `ruff check . --fix` (автоматические исправления lint следует проверять в diff). Файл `examples/before_format.py` исключён из проверок намеренно: это демонстрация плохого стиля, но функционально он используется тестами для сопоставления поведения.

## Как показать навигацию в Visual Studio Code

1. Откройте папку проекта через **File → Open Folder** и выберите интерпретатор `.venv`.
2. Перейдите в `tests/test_orders.py`, выделите `create_order` и нажмите **F12** (Go to Definition) — попадёте в `src/readable_orders/service.py`.
3. Нажмите **Shift+F12** на `calculate_total` в `service.py` (Go to References), чтобы найти вызовы.
4. Откройте **Outline** или используйте **Ctrl+Shift+O**, чтобы перейти к функции в текущем файле.
5. Нажмите **Ctrl+P**, затем введите `validation.py`, чтобы быстро открыть файл. Используйте **Ctrl+Shift+F** для поиска по всему проекту.
6. Выполните сохранение файла, чтобы применить форматирование через расширение Ruff; нажмите **Ctrl+Shift+P** и выберите `Format Document`, если требуется явный запуск.

Команды перехода к определению и ссылкам зависят от доступности языкового сервера. Официальные расширения Python, Pylance и Ruff указаны в `.vscode/extensions.json`.

## Ожидаемый автоматический контроль качества на GitHub

Workflow `quality.yml` проверяет три независимых пункта: `ruff format --check .`, `ruff check .`, `python -m pytest -q`. Это не веб-приложение: GitHub хранит исходники и показывает результаты проверок.

**Примечание по проверке:** локальный запуск pytest и подсчёта метрик был выполнен при подготовке проекта. Результат GitHub Actions следует считать подтверждённым **только после загрузки кода в ваш новый репозиторий и появления зелёного запуска**.

## Источники

- https://peps.python.org/pep-0008/
- https://docs.astral.sh/ruff/formatter/
- https://code.visualstudio.com/docs/editing/editingevolved
- https://www.jetbrains.com/help/pycharm/reformat-and-rearrange-code.html
- https://www.jetbrains.com/help/pycharm/navigating-through-the-source-code.html
- https://docs.github.com/en/actions/tutorials/build-and-test-code/python
