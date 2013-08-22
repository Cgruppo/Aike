{% extends 'base.tpl' %}
{% block content %}
<h2 style="text-align:center">活动展示</h2>
<div class="row">
	<div class="span3 well">
	
	</div>

	<div class="span8">
		{% for activity in activitys %}
			{% if activity %}	
				<div class="well" style="background-color:rgb(254,238,205)">
				<div>
					<dl>
					<dt><a href="/show/ac{{activity.id}}"><label>{{activity.name}}</label></a></dt>
					<br>
					<dt>活动举办方：
					</dt>
						<dd>
						{% for organizer in activity.organizer.all %}
						<a href="/u{{organizer.id}}/">{{organizer.aikeuser.alias}}</a>&nbsp;
						{% endfor %}
						</dd>
					<dt>活动简介：</dt>
						<dd>{{activity.introduction|safe}}</dd>
					</dl>
				</div>
				<!-- List界面不提供参加与退出按钮，为方便调试，暂时开启 -->
				<div class="btn-group">
					<a href="/show/ac{{activity.id}}/join/"><button class="btn btn-success">参加</button></a>
					<button class="btn btn-info">赞助</button>
				</div>
				

				</div>
			{% else %}
			{% endif %}
		{% endfor %}
	</div>
</div><!-- row -->
{% endblock%}
