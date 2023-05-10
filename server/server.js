const http = require('http');
const server = http.createServer()

const socketio = require('socket.io')

const io = socketio(server, {
    cors:{
        origin:'http://127.0.0.1:8000',
        methods:['GET', 'POST']
    }
})

const room = 'testRoom'

io.on('connection', socket => {
    console.log('connected')
    console.log(socket.id)

    socket.join(room)
    // io.to(room).emit("Welcome", "a new user joined the room")
    socket.broadcast.emit("Welcome2", "a new user joined the room !!!!")
    socket.on('message', msg => {
        console.log(msg)
        io.emit('messageToClient',msg)
    })

    socket.on('disconnect', () =>{
        io.to(room).emit('bye',"User have left the room")
    })
})

server.listen(8000, () => console.log('listening on port 8000'))