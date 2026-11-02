# Inkscape Transfer Size

[🇬🇧 English](#-english) · [🇷🇺 Русский](#-русский)

---

## 🇬🇧 English

**Inkscape Transfer Size** is a small Inkscape extension that copies the **width and height** of a *master object* onto **all other selected objects**.

The master object is detected automatically — by default it is the first selected object with a **black fill** and **no stroke**. The fill colour can be changed in the extension's dialog.

### Features

- Finds the master object automatically inside the current selection (including inside groups).
- Configurable master colour (default: `#000000`) and colour tolerance.
- Copies both **width** and **height** from the master's bounding box.
- Smart handling of shapes:
  - `<rect>` and `<ellipse>` without transforms are resized natively (`width`/`height` or `rx`/`ry`).
  - Everything else is scaled via a transform matrix around its own centre.
- Works with groups: nested elements are discovered recursively.

### Requirements

- Inkscape **1.0** or newer (tested on 1.x).
- Python 3 (bundled with Inkscape).

### Installation

1. Download `transfer_size.inx` and `transfer_size.py`.
2. Copy both files into your Inkscape extensions folder:

   | OS      | Path |
   |---------|------|
   | Linux   | `~/.config/inkscape/extensions/` |
   | macOS   | `~/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions/` |
   | Windows | `%APPDATA%\inkscape\extensions\` |

3. On Linux/macOS make the script executable:

   ```bash
   chmod +x transfer_size.py
   ```

4. Restart Inkscape.

The extension will appear under:

```
Extensions → Custom → Transfer Size
```

### Usage

1. Select **two or more** objects (or a group containing them).
   - One of them must be the *master* — by default: black fill, no stroke.
   - All the others will receive the master's width and height.
2. Open **Extensions → Custom → Transfer Size**.
3. *(Optional)* Change the **master colour** or the **colour tolerance**.
4. Click **Apply**.

Each target object is resized so that its bounding box matches the master's width and height.

### Options

| Option             | Default     | Description |
|--------------------|-------------|-------------|
| **Master colour**  | `#000000`   | Fill colour of the master object. |
| **Colour tolerance** | `10`      | Per-channel tolerance (0–255) when matching the master's fill. Useful for near-black or anti-aliased colours. |

### Limitations

- All selected objects should share the same coordinate system (same parent or same selected group).
- For rotated objects the **bounding box** is used, so the visible result may differ slightly from the master.
- Gradient and pattern fills cannot be compared as a solid colour and are ignored when searching for the master.

### License

MIT — see [LICENSE](LICENSE).

---

## 🇷🇺 Русский

**Inkscape Transfer Size** — небольшое расширение для Inkscape, которое переносит **ширину и высоту** *мастер-объекта* на **все остальные выделенные объекты**.

Мастер-объект определяется автоматически: по умолчанию это первый выделенный объект с **чёрной заливкой** и **без обводки**. Цвет заливки мастера можно изменить в диалоге расширения.

### Возможности

- Автоматически находит мастер-объект в текущем выделении (включая объекты внутри групп).
- Настраиваемый цвет мастера (по умолчанию `#000000`) и допуск по цвету.
- Переносит **ширину** и **высоту** из bounding box мастера.
- Умная обработка фигур:
  - `<rect>` и `<ellipse>` без трансформаций масштабируются напрямую (`width`/`height` или `rx`/`ry`).
  - Остальные объекты масштабируются матрицей трансформации вокруг своего центра.
- Поддержка групп: вложенные элементы обнаруживаются рекурсивно.

### Требования

- Inkscape **1.0** или новее (проверено на 1.x).
- Python 3 (поставляется вместе с Inkscape).

### Установка

1. Скачайте `transfer_size.inx` и `transfer_size.py`.
2. Скопируйте оба файла в каталог расширений Inkscape:

   | ОС      | Путь |
   |---------|------|
   | Linux   | `~/.config/inkscape/extensions/` |
   | macOS   | `~/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions/` |
   | Windows | `%APPDATA%\inkscape\extensions\` |

3. На Linux/macOS сделайте скрипт исполняемым:

   ```bash
   chmod +x transfer_size.py
   ```

4. Перезапустите Inkscape.

Расширение появится в меню:

```
Расширения → Custom → Transfer Size
```

### Использование

1. Выделите **два или более** объекта (или группу, содержащую их).
   - Один из них должен быть *мастером* — по умолчанию: чёрная заливка, без обводки.
   - Все остальные получат ширину и высоту мастера.
2. Откройте **Расширения → Custom → Transfer Size**.
3. *(Необязательно)* Измените **цвет мастера** или **допуск по цвету**.
4. Нажмите **Применить**.

Каждый целевой объект масштабируется так, чтобы его bounding box совпал с шириной и высотой мастера.

### Параметры

| Параметр            | По умолчанию | Описание |
|---------------------|--------------|----------|
| **Цвет мастера**    | `#000000`    | Цвет заливки мастер-объекта. |
| **Допуск цвета**    | `10`         | Допуск по каждому каналу (0–255) при сравнении заливки. Полезно для почти-чёрных и сглаженных цветов. |

### Ограничения

- Все выделенные объекты должны находиться в одной системе координат (общий родитель или выделенная группа).
- Для повёрнутых объектов используется **bounding box**, поэтому визуальный результат может незначительно отличаться от мастера.
- Градиентные и pattern-заливки нельзя сравнить как сплошной цвет — они игнорируются при поиске мастера.

### Лицензия

MIT — см. [LICENSE](LICENSE).

---

## Авторы / Authors

Made with ❤️ for the Inkscape community.

## Contributing / Участие

Issues and pull requests are welcome!  
Issues и pull requests приветствуются!