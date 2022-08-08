import json

from legacy import DateTimePickerDjango110, is_legacy

from bootstrap3_datetime.widgets import DateTimePicker


def test_rendering():
    options = {"pickTime": True, "format": "YYYY-MM-DD HH:mm"}
    widget = (DateTimePickerDjango110 if is_legacy() else DateTimePicker)(options=options)
    expected_output = (
        '\n    <div class="input-group date" id="_pickers">\n      <input class="form-control" name="a" type="text"'
        ' value="b"/>\n      <span class="input-group-addon">\n        <span class="glyphicon'
        ' glyphicon-calendar"></span>\n      </span>\n    </div>\n    <script>\n        (function(window) {\n          '
        '  var callback = function() {\n               '
        ' $(function(){$("#_pickers:has(input:not([readonly],[disabled]))").datetimepicker(%s);});\n            };\n   '
        '         if(window.addEventListener)\n                window.addEventListener("load", callback, false);\n     '
        '       else if (window.attachEvent)\n                window.attachEvent("onload", callback);\n            else'
        ' window.onload = callback;\n        })(window);\n    </script>'
    )
    assert widget.render("a", "b", {}) == expected_output % json.dumps(options)
