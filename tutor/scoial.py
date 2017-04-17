def user_social(backend, user, response, *args, **kwargs):


    user.email = kwargs['details']['email']
	user.firstname = kwargs['details']['fullname']
	user.login_type = "facebook"
	user.save()
