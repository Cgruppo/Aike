<h2 style="text-align:center">{{title}}</h2>
<div class="hero-unit">
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
		<br><input class="btn btn-info"  type="submit" value="提交">
	</form>
</div>
