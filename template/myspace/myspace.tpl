{% extends 'base.tpl' %}
{% block content %}
<div class=row>
	<table>
	<tr valign="top">
	<td>
	{% include 'mynavlist.tpl' %}	
	</td>	
	
	<td>
	<div class="span10">
	{% if mypage %}
	{% include mypage %}
	{% endif %}
	</div>

	</td>
	</tr>
	</table>
</div>
{% endblock%}
