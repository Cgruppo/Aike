{% if addfriendNs %}
	{% for addfriendN in addfriendNs %}
	<li style="min-width:300px"><a href="/u{{addfriendN.owner.id}}">{{addfriendN.owner.alias}}</a>请求添加您为好友，<a href="/friend/add/u{{addfriendN.owner.id}}">接受</a>，<a href="/friend/ignore/u{{addfriendN.owner.id}}">忽略</a>
	</li>
	{% endfor %}
<li class="diviter"></li>
{% else %}
<li style="text-align:center"><b>无任何通知</b></li>
{% endif %}
