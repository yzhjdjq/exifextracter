# EXIF Extracter

Python-скрипт для извлечения даты создания фото или видео из их EXIF для последующего переименования файла. А именно, к изначальному имени добавляется Android-шаблон `MEDIATYPE_YYYYMMDD_HHMMSS`.
Например, фото `DSCN1234.jpg` будет переименовано в `DSCN1234 IMG_20240822_122436.jpg`.

## Поддерживаемые типы файлов
- `jpg`;
- `jpeg`;
- `mov`;
- `mp4`.

Соответственно для кажого типа присваиваются следующие `MEDIATYPE`:
- `IMG`;
- `VID`.

## Зависимости
Python:
- `exifread` \[[ссылка](https://pypi.org/project/ExifRead/)\];
- `ffmpeg-python` \[[ссылка](https://pypi.org/project/ffmpeg-python/)\].

Также необходим пакет `ffprobe` библиотеки `ffmpeg`, который использует библиотека обертка `ffmpeg-python` для извлечения метаданных из видеофайлов.

## Использование

Необходимо скопировать скрипт `ExifExtracter.py` в папку с файлами, которые необходимо обработать. Далее, ввести:

```sh
$ python3 ExifExtracter.py
```

Скрипт переименует все файлы без рекурсии. В случае успешной обработки _файла_, в консоль будет осуществлен вывод формата:
```
<OldFilename>.<type> -> <OldFileName> MEDIATYPE_YYYYMMDD_HHMMSS.<type> Is success...
```