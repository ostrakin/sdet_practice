# Form Automation Test

Проект для автоматического тестирования веб-форм с использованием Selenium и pytest.

## Краткое описание

Автоматизированные тесты покрывают работу с веб-формой: заполнение полей, валидация, отправка, проверка ответов и обработка всплывающих уведомлений. Тесты запускаются в двух браузерах — Chrome и Firefox — благодаря параметризации в pytest.

---

## Структура проекта

- `form_page_v2.py` — Page Object Model для работы с формой  
- `test_form_v2.py` — тестовые сценарии  
- `requirements.txt` — зависимости проекта  
- `README.md` — этот файл

---

## Требования

- Python 3.8+  
- Установленные браузеры: Chrome и/или Firefox  
- chromedriver/geckodriver в PATH или использование WebDriverManager

---

## Установка

Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt

pytest test_form_v2.py -v
