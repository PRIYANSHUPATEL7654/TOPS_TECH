
async function sendMessage(){

    let input = document.getElementById("message");
    let message = input.value;

    if(message.trim() === ""){
        return;
    }

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `
        <div class="user-message">
            <b>You:</b> ${message}
        </div>
    `;

    input.value = "";

    try{

        let response = await fetch("http://127.0.0.1:8000/chat",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                message:message
            })
        });

        let data = await response.json();

        chatBox.innerHTML += `
            <div class="bot-message">
                <b>Bot:</b> ${data.reply}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    }catch(error){

        chatBox.innerHTML += `
            <div class="bot-message">
                <b>Bot:</b> Error connecting backend.
            </div>
        `;
    }
}
