{% extends 'base.tpl' %}
{% block content %}
<h2 style="text-align:center">我的好友</h2>
<div class="row">
<div class="tabbable tabs-left">
	<div class="span3">
		<ul class="nav nav-list well">
		{% for group in groups %}
		<li><a href="#group{{group.id}}" data-toggle="tab">{{group.name}}</a></li>
		{% endfor %}
		</ul>
	</div>

	<div class="span8">
	<div class="hero-unit">
		<div class="tab-content">
		{% for group in groups %}
			<div class="tab-pane" id="group{{group.id}}">
			<h2>{{group.name}}</h2>
			<dl>
			{% for friend in group.member.all %}
				<dt>{{friend.alias}}</dt>
				<dd>{{friend.sex}}</dd>
				<dd>{{friend.city}}</dd>
				<dd>{{friend.university}}</dd>
				<br>
			{% endfor %}
			</dl>
			</div>
		{% endfor %}
		</div>
		<form action="/friend/" method="POST">
			<dl>
			<dt>输入要添加的好友名：</dt>
			<dd><input type="text" name="alias"><dd>
			<dt>输入要添加到的分组：</dt>
			<dd><input type="text" name="group"><dd>
			</dl>
			<input type="submit" class="btn btn-info" value="提交">
		</form>
	</div>
	</div>
</div>
</div><!-- row -->
{% endblock%}
