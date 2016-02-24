Welcome to the webapi wiki!

# webapi
## user id
`api/user/userid/password` : send userid, password and if success, return userid, token
## user list
`api/userlist` : return all user list 
## user permission
`api/perm/systemid/userid` : send systemid, userid and if success, return programid list

## ajax function sample

    function request_user()
	{
		var userid=$("#user_id").val();
		var password=$("#password").val();
		var req = $.ajax({
		url: "/api/user/"+userid+"/"+password,
		dataType: "json"
		});
		req.done(function(json_data) {
			var userid=json_data['userid'];
			var pass=json_data['password'];
			var token=json_data['token']
			var html_text = "User id : " + userid + "<br />" + "Password : " + pass + "<br />" + "Token : " + token;
			$("#result").html(html_text);
		});
	};

	function request_userlist()
	{
		var req = $.ajax({
		url: "/api/userlist/",
		dataType: "json"
		});
		req.done(function(json_data) {
			var html_text = "<ul>";
			for (var i = 0; i < json_data.length; i++) {
				var object = json_data[i];
				var fields = object["fields"];
				html_text += "<li>"+fields["username"]+"</li>"; 
			};
			html_text +="</ul>"
			$("#result_list").html(html_text);
		});
	};

	function request_perm()
	{
		var systemid=$("#systemid").val();
		var userid=$("#user_id2").val();
		var req = $.ajax({
		url: "/api/perm/"+systemid+"/"+userid,
		dataType: "json"
		});
		req.done(function(json_data) {
			var html_text = "<ul>";
			var prog_list = json_data["programid"]
			for (var i = 0; i < prog_list.length; i++) {
				var fields = prog_list[i];
				html_text += "<li>"+fields+"</li>"; 
			};
			html_text +="</ul>"
			$("#result_perm").html(html_text);
		});
	};
