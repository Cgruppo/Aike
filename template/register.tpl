{% extends 'base.tpl' %}
{% block content %}
<style>
	 .controls >ul{
	 	list-style: none;
	 }

</style>

<p>{{requestdata}}</p>
{% if request.user.is_authenticated %}
<p>你已经登陆</p>
<p>{{request.user}}</p>
{% else %}
<div class="row">
<fieldset>
<legend>请输入个人信息</legend>
<div class="span6">
<div class="alert alert-info">
<br>
<p>加*号为必填项</p>
<br>
</div>
<br>
<div>
<button class="btn btn-info" id="hide">隐藏非必填字段</button>
</div>
<br>
<form action="/register/" method="POST" class="form-horizontal">
	<div class="control-group {{error.account}}">
		<label class="control-label" for="id_account">帐号(*)：</label>
		<div class="controls">
			<div class="input-append ">
			{{form.account}}<span class="help-inline">{{span.account}}</span>
			</div>
		</div>
	</div>
	<div class="control-group {{error.password}}">
		<label class="control-label" for="id_password">密码(*)：</label>
		<div class="controls">
			<div class="input-append ">
			{{form.password}}<span class="help-inline">{{span.password}}</span>
			</div>
		</div>
	</div>
	<div class="control-group">
		<label class="control-label" for="id_alias">别名(*)：</label>
		<div class="controls">
		{{form.alias}}
		</div>
	</div>

	<div class="nrq">
	<div class="control-group">
		<label class="control-label" for="id_name">真名：</label>
		<div class="controls">
		{{form.name}}
		</div>
	</div>
	<div class="control-group">
		<label class="control-label" for="id_email">Email：</label>
		<div class="controls">
			<div class="input-append">
			{{form.email}}<span class="add-on"><i class="icon-envelope"></i></span>
			</div>
		</div>
	</div>
	<div class="control-group">
		<label class="control-label" for="id_sex">性别：</label>
		<div class="controls">
		{{form.sex}}
		</div>
	</div>
	<div class="control-group {{error.age}}">
		<label class="control-label" for="id_age">年龄：</label>
		<div class="controls">
			<div class="input-append ">
			{{form.age}}<span class="help-inline">{{span.age}}</span>
			</div>
		</div>
	</div>
	<div class="control-group">
		<label class="control-label" for="id_city">城市：</label>
		<div class="controls">
		{{form.city}}
		</div>
	</div>
	<div class="control-group">
		<label class="control-label" for="id_university">大学：</label>
		<div class="controls">
		{{form.university}}
		</div>
	</div>
	</div><!-- nrq -->

	<div class="form-actions">
		<input type="submit" value="注册" class="btn btn-success">
	</div>
</form>
</div><!-- span8 -->

<div class="span5 well">
<h3 align="center">注册须知</h3>
<br>
<pre>
1.本站目前处于测试阶段，还存在很多bug
2.……
</pre>
</div>

</fieldset>
</div><!-- row -->
{% endif %}
{% endblock%}

{% block js%}
	<script type="text/javascript">
	var $hideBtn = $("#hide")
	var $nrq = $(".nrq")
	$hideBtn.click(function(){
		if ($nrq.is(":visible")) {
			$nrq.hide()
			$hideBtn.html("显示更多字段")
		}
		else{
			$nrq.show()
			$hideBtn.html("隐藏非必填字段")
		}

	})
	</script>
{% endblock %}
