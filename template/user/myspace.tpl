{% extends 'base.tpl' %}
{% block content %}
<div class="row-fluid">
		<div class="span2">
		{% include 'user/mynavlist.tpl' %}	
		</div>
	<div class="span8">
	{% if mypage %}
	{% include mypage %}
	{% endif %}
	</div>
</div>
{% endblock%}