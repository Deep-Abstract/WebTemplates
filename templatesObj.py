


formTemp=\
"""
<form action="{{action}}" {% if id %} id="{{id}}" {% endif %} method="{{method}}">
    <div class="divider"></div>
    {% for key in entity.attrs %}
    {% set v=entityStyle[key] -%}
    {%- if v -%}
    <div class="divider"></div>
    <div class="row">
          <div class="Section">
              <div class="input-field col s12">
                  {{key|capitalize()}}
                  <input placeholder="{{entity[key]}}" type="{{v}}" name="{{key}}" class="validate"/>
              </div>
              <div class="col s12 m6 l2"></div>
          </div>
    </div>
    {%- endif -%}
    {%- endfor -%}
    <div class="divider"></div>
    <input type="submit" value="{{submitValue}}" class="waves-effect waves-light btn {{btnColor}}"/>
</form>
"""
baseTemp=\
"""
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>{{title}}</title>
      <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <link type="text/css" rel="stylesheet" href="static/css/materialize.min.css"  media="screen,projection"/>
      {% if headplus %}
        {{headplus}}
      {% endif %}
</head>
<body>
<div class="container">
{{body}}
</div>
</body>
</html>
"""
pTemp=\
"""
<p>{{content}}</p>
"""
blockquoteTemp=\
"""
<blockquote>
{{content}}
</blockquote>
"""
tableTemp=\
"""
    <table class="{{classIs}}">
    <thead>
        <tr>
            {% if not attrFilter %}
            {% set fields= (entities[0].attrs)|sort() -%}
            {% else %}
            {% set fields= entities[0].attrs.difference(attrFilter) -%}
            {% endif %}
            {% for field in fields -%}
              <th data-field="{{field}}">{{field|capitalize()}}</th>
            {%- endfor %}

        </tr>
    </thead>
    <tbody>
        {% for entity in entities -%}
            <tr>
            {% for field in fields -%}
                <td>{{entity[field]}}</td>
            {%- endfor %}
            </tr>
        {%- endfor %}
    </tbody>
    </table>
"""

