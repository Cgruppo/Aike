{% extends 'base.tpl' %}
{% block content %}
<div class="row-fluid">
<div class="span8 well offset2">
{{info}}
<h2>请先登陆</h2>
<hr>
{% if request.user.is_authenticated %}
<h4>您已经登陆！</h4>
{% else %}
<h4>请输入帐号和密码</h4>
<form action="{% url logon %}" method="post">
    {% csrf_token %}
	<dl>
	<dt>帐号</dt>
	<dd><input type="text" name="username"></dd>
	<dt>密码</dt>
	<dd><input type="password" name="password"><dd>
	<div align="center">
	<br><input type="submit" value="登陆" class="btn btn-info">
	</div>
	<dl>
</form>
{% endif %}
</div>
<div class="sapn4"></div>
</div>
{% endblock%}
