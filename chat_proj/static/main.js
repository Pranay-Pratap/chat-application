const socket = io('http://localhost:8000')

const alertBox = document.getElementById("alert-box")
const messagesBox = document.getElementById("messages-box")
const messageInput = document.getElementById("message-input")
const sendBtn = document.getElementById("send-btn")

// socket.on("Welcome", msg =>{
//     console.log(msg)
// })

const handleAlerts = (msg,type) =>{
    alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
        ${msg}
    </div>
    `
    setTimeout(() => alertBox.innerHTML = "", 5000)
}

socket.on("Welcome2", msg =>{
    handleAlerts(msg,"primary")
})

socket.on("bye", msg =>{
    handleAlerts(msg,"danger")
})


sendBtn.addEventListener("click", ()=>{
    const message = messageInput.value
    messageInput.value = ""
    socket.emit("message", message)
    console.log(message)
})

socket.on("messageToClient", msg =>{
    console.log(msg)
    messagesBox.innerHTML += `<b>${msg}</b><br>`
})