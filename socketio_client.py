import socketio
import base64

# with socketio.SimpleClient() as sio:


sio = socketio.Client()

connected = False

@sio.event
def message(data):
    print('message: ', data)

@sio.event
def door_control(data):
    print(data)

@sio.event
def light_control(data):
    print(data)

while not connected:
    try:
        # sio.connect('http://localhost:8900')
        sio.connect('https://thesis-socketio-server.onrender.com')
        print('My ID:', sio.sid)
        connected = True
        # sio.wait()
        while True:
            message_type = int(input('Enter message number: '))
            if message_type == 0:
                image_file = input('Image name: ')
                with open(image_file, 'rb') as f:
                    content = f.read()
                    print(content)
                    sio.emit('image_capture', base64.b64encode(content))
                    # print(f.read())
            else:
                text_message = input('Enter ypur message: ')
                sio.emit('message', text_message)
            
    except Exception as ex:
        print(ex)




