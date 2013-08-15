{% extends 'base.tpl' %}
{% block content %}
<div class="row">
<div class="span3 well">
	{% include 'acnavlist.tpl' %}
</div>

<div class="span8 well">
	<form atcion="/show/ac{{activity.id}}/acitemadmin/" method="POST">
		<dl>
		<dt>活动名称：</dt>
		<dd>{{activityChangeForm.name}}</dd>
		<br>
		<dt>地点：</dt>
		<dd>{{activityChangeForm.place}}</dd>
		<br>
		<dt>价格：</dt>
		<dd>{{activityChangeForm.price}}</dd>
		<br>
		<dt>举办时间：</dt>
		<dd>{{activityChangeForm.date}}</dd>
		<br>
		<dt>简介：</dt>
		<dd>{{activityChangeForm.introduction}}<dd>
		</dl>
		<br><input type="submit" value="提交" class="btn btn-primary">
	</form>
<br>

<div>
	<form action="/show/ac{{activity.id}}/acitemadmin/addorganizer/" method="GET">
		<h4>添加一名举办者<h4>
		<dl>
			<dt>请输入姓名<dt>
			<dd><input name="alias" type="text"></dd>
		</dl>
		<input type="submit" value="提交" class="btn btn-primary">
	</form>
</div>

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

</div> <!-- row -->
{% endblock %}

{% block css %}
<link rel="stylesheet" type="text/css" href="/static/datepicker/css/datepicker.css" />
<link rel="stylesheet" type="text/css" href="/static/bootstrap-wysihtml5/css/bootstrap-wysihtml5.css" />
{% endblock%}

{% block js %}
<script type="text/javascript" src="/static/datepicker/js/bootstrap-datepicker.js"></script>
<script type="text/javascript" src="/static/datepicker/js/jquery.ui.datepicker-zh-CN.js"></script>
<script type="text/javascript" src="/static/bootstrap-wysihtml5/js/wysihtml5.min.js"></script>
<script type="text/javascript" src="/static/bootstrap-wysihtml5/js/bootstrap-wysihtml5.min.js"></script>
<script type="text/javascript">
$("#id_date").datepicker({format:"yyyy-mm-dd"});
$("#id_introduction").wysihtml5();
</script>
{% endblock %}
