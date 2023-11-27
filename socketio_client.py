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
        sio.connect('http://localhost:8900')
        # sio.connect('https://socketiopractice.onrender.com')
        print('My ID:', sio.sid)
        connected = True
        # sio.wait()
        while True:
            image_file = input('Image name: ')
            with open(image_file, 'rb') as f:
                content = f.read()
                print(content)
                sio.emit('image_capture', base64.b64encode(content))
                # print(f.read())
            # sio.emit('message', x)
            
    except Exception as ex:
        print(ex)




