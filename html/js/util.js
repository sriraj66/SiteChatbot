
const DOM =    `
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<link rel="stylesheet" href="./css/style.css">
  <button class="btn-pop-message" onclick="toggleMessage()"><span><i class="fas fa-close" ></i></span></button>

<section class="msger --hide" id="msger">
<header class="msger-header">
  <div class="msger-header-title">
    <i class="fas fa-comment-alt"></i> KRCT BOT
  </div>
  <div class="msger-header-options" onclick="toggleMessage()" >
    <span><i class="fas fa-times"></i></span>
  </div>
</header>

<main class="msger-chat">
  
</main>

<form class="msger-inputarea">
<input type="text" name='query' class="msger-input" placeholder="Enter your message...">
<input type="text" name='uuid' value='3bb915ee-dfa9-46fb-8a1c-4142fccf2194' hidden class="msger-uuid"">

  <button type="submit" class="msger-send-btn">Send</button>
</form>
</section>


`

document.getElementsByTagName("body")[0].innerHTML = DOM;