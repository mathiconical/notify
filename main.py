from notify import Notify

Notify = Notify()

params = {
	'title': 'NORMAL SPEED',
	'message': 'A NORMAL AND INFO MESSAGE',
	'type_bgc': 'info',
	'out_type': 'normal',
}

params2 = {
	'title': 'SLOW SPEED',
	'message': 'A SLOW AND SUCCESS MESSAGE',
	'type_bgc': 'success',
	'out_type': 'slow',
}

params3 = {
	'title': 'SLOWLY SPEED',
	'message': 'A SLOWLY AND WARNING MESSAGE',
	'type_bgc': 'warning',
	'out_type': 'slowly',
}

if __name__ == '__main__':
	Notify.message(**params)
	Notify.message(**params2)
	Notify.message(**params3)