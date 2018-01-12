# django-bootstrap3-datetimepicker

This package uses [Bootstrap v3 datetimepicker widget version 4](https://github.com/Eonasdan/bootstrap-datetimepicker).

This project was originally a fork of https://github.com/nkunihiko/django-bootstrap3-datetimepicker, 
it now has the following breaking changes:

* js/css files are no longer included in the project, managing them is up to the user, eg. using 
[grablib](https://github.com/samuelcolvin/grablib).
* the widget no longer has js/css assets. these are left for you to deploy as you wish.
* bug/warning fixes
* remove support for python 2.6 and associated clean up

## Install

    pip install django-bootstrap3-datetimepicker-2

## Example

#### forms.py

```python
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

  class ToDoForm(forms.Form):
      todo = forms.CharField(
          widget=forms.TextInput(attrs={"class": "form-control"}))
      date = forms.DateField(
          widget=DateTimePicker(options={"format": "YYYY-MM-DD"}))
      reminder = forms.DateTimeField(
          required=False,
          widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))
```

The `options` will be passed to the JavaScript datetimepicker instance. 
Available `options` are explained in the following documents:

* http://eonasdan.github.io/bootstrap-datetimepicker/

You don't need to set the `language` option, 
because it will be set the current language of the thread automatically.

#### template.html

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- load all required js/css yourself here -->
  </head>
  <body>
    <form method="post" role="form">
      {{ form|bootstrap }}
      {% csrf_token %}
      <div class="form-group">
        <input type="submit" value="Submit" class="btn btn-primary" />
      </div>
    </form>
  </body>
</html>
```

Here we assume you're using [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) or 
[django-jinja-bootstrap-form](https://github.com/samuelcolvin/django-jinja-bootstrap-form) but you can
draw out your HTML manually.

## Requirements

* Python >= 2.7
* Django >= 1.11
* Bootstrap == 3.X
* Moment >= 2.10.6
* bootstrap-datetimepicker >= 4.15.35

### Backwards Compatibility

If you want to use the picker in a Django 1.9 or 1.10 project, you can adapt by overwriting `build_attrs` with

```python
def build_attrs(self, base_attrs=None, extra_attrs=None, **kwargs):
    if extra_attrs:
        base_attrs.update(extra_attrs)
    base_attrs.update(kwargs)
    return super().build_attrs(**base_attrs)
```
