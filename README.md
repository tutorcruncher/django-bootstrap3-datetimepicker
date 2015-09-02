# django-bootstrap3-datetimepicker

This package uses [Bootstrap v3 datetimepicker widget version 4](https://github.com/Eonasdan/bootstrap-datetimepicker).

This project is a fork of https://github.com/nkunihiko/django-bootstrap3-datetimepicker with the following changes:
* bug/warning fixes
* remove support for python 2.6 and associated clean up
* js/css files are no longer included in the project, managing them is up to the user
* the widget no longer has js/css assert so you can load them as you wish, this is important as loading 
bootstrap-datepicker.js multiple times can cause unexpected behavior.

 Install

* Run `pip install django-bootstrap3-datetimepicker`
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
    <link rel="stylesheet" 
        href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.css">
    <link rel="stylesheet" 
        href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-theme.css">
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.js">
    </script>
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.js">
    </script>
    {{ form.media }}
  </head>
  <body>
    <form method="post" role="form">
      {% for field in form.visible_fields %}
      <div id="div_{{ field.html_name }}" 
         class="form-group{% if field.errors %} has-error{% endif %}">
        {{ field.label_tag }}
        {{ field }}
        <div class="text-muted pull-right">
          <small>{{ field.help_text }}</small>
        </div>
        <div class="help-block">
          {{ field.errors }}
        </div>
      </div>
      {% endfor %}
      {% for hidden in form.hidden_fields %}
        {{ hidden }}
      {% endfor %}
      {% csrf_token %}
      <div class="form-group">
        <input type="submit" value="Submit" class="btn btn-primary" />
      </div>
    </form>
  </body>
</html>
```

Bootstrap3 and jQuery have to be included along with `{{ form.media }}`

Requirements
-------------------------------

* Python >= 2.7
* Django >= 1.8
* Bootstrap >= 3.0


