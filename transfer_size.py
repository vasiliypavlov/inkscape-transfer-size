#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transfer Size — расширение для Inkscape.

Берёт мастер-объект в выделенной группе элементов (по умолчанию — объект
с заданной заливкой и без обводки) и переносит его ширину и высоту
на все остальные объекты выделения.
"""

import inkex
from inkex import Transform, Color


SVG_NS = "http://www.w3.org/2000/svg"


class TransferSize(inkex.EffectExtension):
    """Перенос размеров мастер-объекта на остальные объекты."""

    def add_arguments(self, pars):
        pars.add_argument("--tab", type=str, default="options")
        pars.add_argument(
            "--master_color",
            type=Color,
            default=Color("black"),
            help="Цвет заливки мастер-объекта",
        )
        pars.add_argument(
            "--tolerance",
            type=float,
            default=10.0,
            help="Допуск совпадения цвета по каждому каналу (0–255)",
        )

    # ---------- вспомогательные методы ----------

    def _iter_shapes(self, elem):
        """Рекурсивно отдаёт все графические элементы из группы."""
        if isinstance(elem, inkex.Group):
            for child in elem:
                yield from self._iter_shapes(child)
        elif isinstance(elem, inkex.ShapeElement):
            yield elem

    def _style_value(self, obj, name):
        """Возвращает значение свойства (style или presentation attribute)."""
        try:
            val = obj.style.get(name, None)
        except Exception:
            val = None
        if val is None:
            val = obj.get(name, None)
        return val

    def _color_matches(self, color_str, target, tol):
        """Проверяет, совпадает ли цвет с целевым с заданным допуском."""
        if not color_str or color_str in ("none", "transparent", "inherit"):
            return False
        try:
            c = Color(color_str)
        except Exception:
            return False
        return (
            abs(c.red   - target.red)   <= tol
            and abs(c.green - target.green) <= tol
            and abs(c.blue  - target.blue)  <= tol
        )

    def _is_master(self, obj, target_color, tol):
        """Объект является мастером: заливка совпадает, обводки нет."""
        fill = self._style_value(obj, "fill")
        if not self._color_matches(fill, target_color, tol):
            return False

        stroke = self._style_value(obj, "stroke")
        if stroke and stroke not in ("none", "transparent"):
            return False

        return True

    def _resize(self, obj, w, h):
        """Масштабирует объект так, чтобы его bbox был w × h."""
        try:
            bbox = obj.bounding_box()
        except Exception:
            return

        if bbox.width <= 0 or bbox.height <= 0:
            return

        sx = w / bbox.width
        sy = h / bbox.height

        tag = obj.tag
        has_transform = bool(obj.get("transform"))

        # Простые случаи — правим сами геометрические атрибуты.
        if tag == f"{{{SVG_NS}}}rect" and not has_transform:
            obj.set("width", str(w))
            obj.set("height", str(h))
            return

        if tag == f"{{{SVG_NS}}}ellipse" and not has_transform:
            obj.set("rx", str(w / 2.0))
            obj.set("ry", str(h / 2.0))
            return

        # Общий случай — масштабируем вокруг центра bbox.
        cx = bbox.center_x
        cy = bbox.center_y

        t = Transform()
        t.add_translate(cx, cy)
        t.add_scale(sx, sy)
        t.add_translate(-cx, -cy)

        obj.transform = t @ obj.transform

    # ---------- основная логика ----------

    def effect(self):
        selection = self.svg.selection
        if not selection:
            raise inkex.AbortExtension(
                "Выделите объекты: мастер и цели (можно выделить группу)."
            )

        # Собираем плоский список графических объектов.
        objects = []
        for elem in selection.values():
            objects.extend(self._iter_shapes(elem))

        if len(objects) < 2:
            raise inkex.AbortExtension(
                "Нужно как минимум 2 объекта: мастер и хотя бы одна цель."
            )

        target_color = self.options.master_color
        tol = self.options.tolerance

        # Ищем мастер-объект.
        master = None
        for obj in objects:
            if self._is_master(obj, target_color, tol):
                master = obj
                break

        if master is None:
            raise inkex.AbortExtension(
                "Мастер-объект не найден.\n"
                "Проверьте, что у него задана указанная заливка и нет обводки."
            )

        master_bbox = master.bounding_box()
        if master_bbox.width <= 0 or master_bbox.height <= 0:
            raise inkex.AbortExtension("Мастер-объект имеет нулевой размер.")

        target_w = master_bbox.width
        target_h = master_bbox.height

        # Применяем размеры ко всем остальным объектам.
        for obj in objects:
            if obj is master:
                continue
            self._resize(obj, target_w, target_h)


if __name__ == "__main__":
    TransferSize().run()