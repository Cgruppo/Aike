{% extends 'base.tpl' %}
{% block content %}
<div class="row">
<div class="span3 well">
	{% include 'acnavlist.tpl' %}
</div>

<div class="span8 well">
	{% if has_per %}
	<p>为您自动生成的二维码</p>
	<img src="/show/ac{{activity.id}}/qrget">
	{% else %}
	<p>您未报名参加该活动</p>
	{% endif%}
</div>

</div> <!-- row -->
{% endblock %}
