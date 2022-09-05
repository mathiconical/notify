import PySimpleGUI as sg

class Notify:
	def __init__(self):
		self.__STATIC_BGC = {
			'info': '#017880',
			'error': '#cf0000',
			'normal': '#272628',
			'success': '#1e8f03',
			'warning': '#a13105',
		}

		self.__STATIC_OUT = {
			'blink': -1,
			'turbo': 0.5,
			'fastest': 1.5,
			'fast': 3,
			'normal': 5,
			'slow': 8,
			'slowly': 12,
			'sleep': 16,
		}

		self.__DEFAULT_PARAMS = {
			'title':'TITLE',
			'message':'MESSAGE',
			'type_bgc':'normal',
			'duration_seconds':2,
			'fade_in':True,
			'custom_bgc':False,
			'add_y':0,
			'out_type':'blink',
		}
	
	def message(self, **kargs):
		PARAMS = {**self.__DEFAULT_PARAMS, **kargs}

		if not PARAMS['custom_bgc']:
			bgc = self.__STATIC_BGC[PARAMS['type_bgc']]
		else:
			bgc = PARAMS['custom_bgc']

		if len(PARAMS['message']) > 40:
			PARAMS['message'] = PARAMS['message'][:40] + '...'

		layout = [
			[
				sg.Text(' X ', background_color=bgc, relief=sg.RELIEF_RIDGE, font='Consolas 10 italic bold', text_color='#ffffff', enable_events=True, key='-symbol-'),
				sg.Text(f' { PARAMS["title"] } ', background_color=bgc, font='Consolas 10 italic bold', text_color='#ffffff', enable_events=True, key='-title-')
			],
			[
				sg.Text(f' {PARAMS["message"]} ', background_color=bgc,  font='Consolas 10 italic', text_color='#ffffff', enable_events=True, key='-message-')
			]
		]

		position = list(sg.Window.get_screen_size())

		if not PARAMS['add_y']:
			position = position[0] - 360, position[1] - 100
		else:
			position = position[0] - 360, position[1] - ( 100 + 65 * PARAMS['add_y'] )

		window = sg.Window(
			PARAMS['title'],
			layout,
			keep_on_top=True,
			finalize=True,
			disable_minimize=True,
			grab_anywhere_using_control=False,
			no_titlebar=True,
			location=position,
			margins=(0,0),
			background_color=bgc,
			size=(350, 60),
		)

		alpha = 1
		force_end = False

		for i in range(PARAMS['duration_seconds']):
			event, values = window.read(timeout=1000)

			#if event in ['-symbol-', '-message-', '-title-']:
			if event in ['-symbol-']:
				force_end = True
				break

		if force_end:
			window.close()
			return

		max_range = ( (PARAMS['duration_seconds'] // 2) + 1) * 25

		for j in range(max_range):
			event, values = window.read(timeout=self.__STATIC_OUT[PARAMS['out_type']])

			#if event in ['-symbol-', '-message-', '-title-']:
			if event in ['-symbol-']:
				window.close()
				return

			if PARAMS['fade_in']:
				alpha = alpha - 0.02
				window.SetAlpha(alpha)

			window.move(position[0], position[1] - j)

		window.close()