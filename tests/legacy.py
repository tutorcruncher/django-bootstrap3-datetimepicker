import django

from bootstrap3_datetime.widgets import DateTimePicker


class DateTimePickerDjango110(DateTimePicker):
    def build_attrs(self, base_attrs=None, extra_attrs=None, **kwargs):
        if extra_attrs:
            base_attrs.update(extra_attrs)
        base_attrs.update(kwargs)
        return super(DateTimePickerDjango110, self).build_attrs(**base_attrs)


def is_legacy():
    x,y,z = [int(v) for v in django.__version__.split(".")]
    return x == 1 and y < 11
