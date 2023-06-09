# Exelib - библиотека для exe-файлов
### <a href=https://github.com/Damir-Sayfullin/ExeLib/blob/main/README.md>In English</a>
## О проекте
<p align="center">
    <a href=https://www.python.org/downloads/release/python-3917><img src="https://img.shields.io/badge/Python-3.9-green?style=for-the-badge" alt="Python Version"></a>
    <a href=https://github.com/Damir-Sayfullin/ExeLib/releases/tag/v1.0.0><img src="https://img.shields.io/badge/Версия-1.0.0-red?style=for-the-badge" alt="Version"></a><br>
    <a href=https://github.com/Damir-Sayfullin/ExeLib/stargazers><img src="https://img.shields.io/github/stars/Damir-Sayfullin/ExeLib?style=for-the-badge&color=yellow&label=%D0%97%D0%B2%D0%B5%D0%B7%D0%B4%D1%8B" alt="Stars"></a>
    <a href=https://github.com/Damir-Sayfullin/ExeLib/watchers><img src="https://img.shields.io/github/watchers/Damir-Sayfullin/ExeLib?style=for-the-badge&label=%D0%9F%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D1%8B" alt="Watchers"></a>
</p>
 
Проект ExeLib представляет собой графическое приложение, созданное с использованием библиотеки tkinter в Python. Это приложение позволяет пользователям организовать коллекцию ссылок на исполняемые файлы (exe-файлы) на их компьютере. Пользователи могут добавлять ссылки на файлы, указывая название и путь к файлу. Они также могут переименовывать ссылки и запускать выбранный exe-файл непосредственно из приложения. Коллекция ссылок сохраняется в файле JSON (paths.json) для последующего использования. Это полезный инструмент для упорядочивания и быстрого доступа к различным exe-файлам на компьютере пользователей.

<a href="https://ibb.co/kmznmpY"><img src="https://i.ibb.co/6XGhX26/Exe-Lib-Image.png" alt="Exe-Lib-Image" width=600></a>

## Установка
Для установки и запуска приложения ExeLib есть 2 способа:
1. Склонируйте репозиторий с помощью `git clone https://github.com/Damir-Sayfullin/ExeLib.git` и запустите `Tkinter.py`.
2. Скачайте установщик `ExeLib-setup.exe` или само приложение `ExeLib.exe` в ассетах релиза. Текущая версия: [v1.0.0](https://github.com/Damir-Sayfullin/ExeLib/releases/tag/v1.0.0)

## Использование
- Добавьте исполняемый файл в библиотеку, нажав кнопку `Добавить`. Выберите файл в файловом диалоге и введите название файла.
- Чтобы удалить исполняемый файл из библиотеки, выберите его в списке и нажмите кнопку `Удалить`.
- Чтобы переименовать исполняемый файл в библиотеке, выберите его в списке и нажмите кнопку `Переименовать`. Введите новое название файла и выберите новый файл, если хотите изменить его.
- Чтобы запустить выбранный исполняемый файл, выберите его в списке и нажмите кнопку `Запустить`.
- Чтобы сохранить изменения и список исполняемых файлов, нажмите кнопку `Сохранить`. Они сохраняются в файл paths.json`, который создается в той же папке, где находится Tkinter.py или приложение ExeLib

## Документация
### Методы
`__init__(self, master)` - конструктор класса ExeLibrary. Принимает объект master - корневое окно tkinter.

`_add_path(self)` - метод для добавления новой ссылки на exe-файл в коллекцию. Открывает диалоговое окно выбора файла, где пользователь может выбрать exe-файл, и затем запрашивает название файла у пользователя.

`_remove_path(self)` - метод для удаления выбранной ссылки на exe-файл из коллекции. Удаляет выбранный элемент из списка ссылок.

`_rename_path(self)` - метод для переименования выбранной ссылки на exe-файл. Запрашивает у пользователя новое название файла и новый путь к exe-файлу.

`_run_path(self)` - метод для запуска выбранного exe-файла. Получает путь к выбранному файлу, определяет директорию файла и выполняет его с помощью subprocess.run().

`_save_paths(self)` - метод для сохранения списка ссылок на exe-файлы в файл paths.json. Сериализует список ссылок и сохраняет его в файл.

`_load_paths(self)` - метод для загрузки списка ссылок на exe-файлы из файла paths.json. Десериализует список ссылок из файла и добавляет их в список.
