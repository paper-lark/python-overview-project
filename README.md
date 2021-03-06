# Overview

![Build status](https://img.shields.io/github/workflow/status/paper-lark/python-overview-project/CI)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub](https://img.shields.io/github/license/paper-lark/python-overview-project)
![Python](https://img.shields.io/badge/python-%5E3.7-brightgreen)
[![Poetry](https://img.shields.io/badge/dependencies-poetry-blue)](https://python-poetry.org)

## Разработка

Для первоначальной разработки склонированного репозитория необходимо запустить команду `make init`.
Она настроит Git Hooks и установит все внешние зависимости.

При необходимости для форматирования кода перед коммитом необходимо запустить команду `make format`.

## Постановка задачи

Реализовать приложение, агрегирующую информацию из разных источников информации.
Получаемые из каждого источника данные преобразуются и отображаются в интерфейсе программы в виде виджета.
Пользователь имеет возможность настраивать, какие виджеты отображаются в интерфейсе.
Приложение имеет встроенные виджеты для:
- просмотра прогноза погоды;
- просмотра ближайших событий в календаре;
- создания коротких заметок;
- очередь web ссылок для прочтения.

Каждый виджет имеет собственный экран настроек, в котором находятся настройки этого виджета.
Также есть экран настроек самого приложения, в котором можно настроить расположение виджетов.
В случае, если хватит времени, виджеты будут устанавливаться отдельно от приложения в настройках приложения. 
Кроме этого, приложение будет поддерживать сторонние расширения.

### Макеты интерфейса

#### Виджеты

##### Календарь
![Calendar design draft](docs/assets/Calendar%20widget.png)

##### Погода
![Weather design draft](docs/assets/Weather%20widget.png)

##### Заметки
![Notes design draft](docs/assets/Note%20widget.png)

## Документация

Пользовательская документация: [ссылка](https://paper-lark.github.io/python-overview-project/)

Программная документация:
1. запустить `make sphinx-update`
2. открыть в браузере файл sphinx/build/html/index.html
