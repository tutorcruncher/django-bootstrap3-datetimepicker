# django-bootstrap3-datetimepicker

This package uses [Bootstrap v3 datetimepicker widget version 4](https://github.com/Eonasdan/bootstrap-datetimepicker).

This project is a fork of https://github.com/nkunihiko/django-bootstrap3-datetimepicker with the following changes:
* bug/warning fixes
* remove support for python 2.6 and associated clean up
* js/css files are no longer included in the project, managing them is up to the user
* the widget no longer has js/css assert so you can load them as you wish, this is important as loading 
bootstrap-datepicker.js multiple times can cause unexpected behavior.

 Install

* Run `pip git+https://github.com/samuelcolvin/django-bootstrap3-datetimepicker.git@<CHOOSE SHA HERE>#egg=django-bootstrap3-datetimepicker==2.4`
* Add `'bootstrap3_datetime'` to your `INSTALLED_APPS`


Example
--------------------------------

###### forms.py

```python
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

  class ToDoForm(forms.Form):
      todo = forms.CharField(
          widget=forms.TextInput(attrs={"class": "form-control"}))
      date = forms.DateField(
          widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                         "pickTime": False}))
      reminder = forms.DateTimeField(
          required=False,
          widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                         "pickSeconds": False}))
```

The `options` will be passed to the JavaScript datetimepicker instance. 
Available `options` are explained in the following documents:

* http://eonasdan.github.io/bootstrap-datetimepicker/

You don't need to set the `language` option, 
because it will be set the current language of the thread automatically.

###### template.html

```html+jinja
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
* Django >= 1.8
* Bootstrap == 3.X
* Moment >= 2.10.6
* bootstrap-datetimepicker >= 4.15.35

