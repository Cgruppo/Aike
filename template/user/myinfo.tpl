<h2 style="text-align:center">{{title}}</h2>
<div class="well">
	<form action="/myspace/myinfo/" method="POST">
	<table>
	<tr>
	<th><label>帐号:</label></th>
	<th>{{request.user.username}}</th>
	</tr>
	<tr>
	<th><label>注册时间:</label></th>
	<th>{{request.user.date_joined}}</th>
	</tr>
	{{form.as_table}}
	<tr>
	<td></td>
	<td><input type="submit" value="提交修改" class="btn btn-info"></td>
	<td><a href="./"><button class="btn btn-danger" >重置本次修改</button></a></td>
	</tr>
	</table>
	</form>
</div>
