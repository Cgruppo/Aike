{% extends 'base.tpl' %}
{% block content %}
{% if visitor %}
<div class="row">
	<div class="span3">
	<div class="well">
	<h3>用户资料</h3>
	<dl>
		<dt>别名</dt>
		<dd>{{visitor.alias}}</dd>
		<dt>年龄</dt>
		<dd>{{visitor.age}}</dd>
		<dt>性别</dt>
		<dd>{% if visitor.sex %}白富美{% else %}高富帅{% endif %}</dd>
		<dt>居住城市</dt>
		<dd>{{visitor.city}}</dd>
		<dt>所在大学</dt>
		<dd>{{visitor.university}}</dd>
	</dl>
	</div>
	<a class="btn btn-success" href="/friend/add/u{{visitor.id}}">加为好友</a>
	</div>

	<div class="span5 well">
		<h3>动态</h3>
		<div class="span5">
		<dl>
		<dt>最近举办的活动</dt>
		<dd>
			{% if organizerRs %}
			{% for organizerR in organizerRs %}
			<a href="/show/ac{{organizerR.activity.id}}">{{organizerR.activity.name}}</a>&nbsp;
			{% endfor %}
			{% else %}
			该用户暂时没有举办过任何活动。
			{% endif %}
		</dd>
		<dt>最近参与的活动</dt>
		<dd>
			{% if participantRs %}
			{% for participantR in participantRs %}
			<a href="/show/ac{{participantR.activity.id}}">{{participantR.activity.name}}</a>&nbsp;
			{% endfor %}
			{% else %}
			该用户暂时没有参加过任何活动哦，给Ta推荐活动吗。
			{% endif %}
		</dd>
		<dl>
		</div>
		
		<form name="messageboard" method="POST">
		<h4>留言板</h4>
		{% if messageboards %}
		{% for messageboard in messageboards %}
			{% ifequal messageboard.owner messageboard.to %}
			<dl style="background:pink" class="well">
			<dt style="text-align:right">{{messageboard.owner.alias}}</dt>
			{% else %}
			<dl style="background:white" class="well">
			<dt>{{messageboard.owner.alias}}</dt>
			{% endifequal %}
			<dd>{{messageboard.text}}</dd>
			<dd style="text-align:right">{{messageboard.date}}</dd>
			</dl>
		{% endfor %}
		{% else %}
		<p>留言板一片空白哦，快来抢沙发啦～～～</p>
		{% endif %}
		<br>
		{{form.text}}
		<input class="btn btn-info"  type="submit" value="提交">
		</form>
	</div>

	<div class="span2 well">
	<h3>杂项，待定</h3>
	</div>
{% else %}
<p>该用户不存在！</p>
{% endif %}
</div> <!-- row -->
{% endblock %}
