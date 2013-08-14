{% extends 'base.tpl' %}
{% block content %}
<h2 style="text-align:center">创建属于你的活动吧！</h2>
<div class="row">
	<div class="span3">
	<div class="hero-unit">
                       
	</div>
	</div>

	<div class="span8 well">
		<form atcion="/create/" method="POST">
		<dl>
		<dt>活动名称：</dt>
		<dd>{{ActivityCreateForm.name}}</dd>
		<br>
		<dt>地点：</dt>
		<dd>{{ActivityCreateForm.place}}</dd>
		<br>
		<dt>价格：</dt>
		<dd>{{ActivityCreateForm.price}}</dd>
		<br>
		<dt>举办时间：</dt>
		<dd>{{ActivityCreateForm.date}}</dd>
		<br>
		<dt>简介：</dt>
		<dd>{{ActivityCreateForm.introduction}}<dd>
		</dl>
		<br><input type="submit" value="提交" class="btn btn-primary">
		</form>
	</div>

</div>
{% endblock%}

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
