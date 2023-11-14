import socketio
import base64

# with socketio.SimpleClient() as sio:


sio = socketio.Client()

connected = False

# @sio.event
# def message(data):
#     print(data)

while not connected:
    try:
        # sio.connect('http://192.168.1.11:8900')
        sio.connect('https://socketiopractice.onrender.com')
        print('My ID:', sio.sid)
        connected = True
        # sio.wait()
        while True:
            image_file = input('Image name: ')
            with open(image_file, 'rb') as f:
                content = f.read()
                print(content)
                sio.emit('message', base64.b64encode(content))
                # print(f.read())
            # sio.emit('message', x)
            
    except Exception as ex:
        print(ex)




