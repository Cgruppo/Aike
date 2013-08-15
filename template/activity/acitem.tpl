{% extends 'base.tpl' %}
{% block content %}
<div class="row">
<div class="span3 well">
	{% include 'acnavlist.tpl' %}
</div>

<div class="span8 well">
	<div class="hero-unit" style="background-color:rgb(254,238,205)">
	<dl>
	<dt><a href="/show/ac{{activity.id}}"><label>{{activity.name}}</label></a></dt>
	<br><dt>活动举办方：</dt>
	<dd>
	<div style="padding:10px">
	{% for organizerR in activity.organizerR_activity.all %}
		<a href="/u{{organizerR.user.id}}" class="alert alert-info">{{organizerR.user.alias}}<i class="icon-user"></i></a>&nbsp;
		{% endfor %}
	</div>
	</dd>
	<dt>活动简介：</dt>
	<dd>{{activity.introduction|safe}}</dd>
	</dl>
	
	<div class="btn-group">
		{% if hasjoin %}
		<a href="/show/ac{{activity.id}}/remove/"><button class="btn btn-danger">退出</button></a>
		{% else %}
		<a href="/show/ac{{activity.id}}/join/"><button class="btn btn-success">参加</button></a>
		{% endif %}
		<button class="btn btn-info">赞助</button>
	</div>
	</div>
<br>
<div class="hero-unit">
<h4>评论:</h4>
	<div class="well">
	{% for comment in comments %}	
	{% if comment %}
		{% if comment.owner in activity.organizer_activity.all %}
		<dl style="background:pink" class="well">
		<dt style="text-align:right">{{comment.owner.alias}}</dt>
		{% else %}
		<dl style="background:white" class="well">
		<dt>{{comment.owner.alias}}</dt>
		{% endif %}
		<dd>{{comment.text}}</dd>
		<dd style="text-align:right">{{comment.date}}</dd>
		</dl>
		{% endif %}
	{% endfor %}
	</div>
</div>
	<form action="/show/ac{{activity.id}}/" method="POST">
	{{comment_add.text}}
	<br><input type="submit" class="btn btn-info" value="提交">
	</form>
</div>

</div> <!-- row -->
{% endblock %}
