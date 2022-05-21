<script>
  import { onMount } from "svelte";

  import { websocket } from "../stores";
  import Message from "./Message.svelte";

  let messageInputElement;
  let messageInputElementText = "";
  let chatWindowElement;
  let messageTextHeight = 0;
  let shiftKeyDown = false;
  let autoScroll = true;
  let messages = [];
  let lastScrollTop = 0;

  const handleMessage = (message) => {
    if (message.trim().length === 0) {
      return;
    }

    $websocket.send(
      JSON.stringify({
        action: "message",
        chatRoom: "general",
        message: message,
      })
    );
    messageInputElement.value = "";
    messageInputElementText = "";
  };

  $websocket.addEventListener("message", (event) => {
    const data = JSON.parse(event.data);
    if (!["message"].includes(data.type)) {
      return;
    }

    if (data.chatRoom !== "general") {
      return;
    }

    messages = [
      ...messages,
      {
        messageUserId: data.userId,
        messageUsername: data.username,
        messageUsernameColor: data.usernameColor,
        messageText: data.message,
        messageTime: data.time,
      },
    ];
  });
  let previousTimeStamp = 0;
  const autoScrollHandler = (timeStamp) => {
    let deltaTime = (timeStamp - previousTimeStamp) / 1000; // time between frames in seconds
    previousTimeStamp = timeStamp;
    const scrollSpeed = 800;
    if (autoScroll) {
      chatWindowElement.scrollTop += scrollSpeed * deltaTime;
    }
    window.requestAnimationFrame(autoScrollHandler);
  };
  onMount(() => window.requestAnimationFrame(autoScrollHandler));
</script>

<div class="chat-window-container container">
  <h2 class="chat-window-title title active-text-color">General chat</h2>

  <div
    class="chat-window"
    bind:this={chatWindowElement}
    on:scroll={() => {
      if (lastScrollTop > chatWindowElement.scrollTop) {
        autoScroll = false;
      } else if (!autoScroll) {
        autoScroll =
          chatWindowElement.scrollHeight -
            chatWindowElement.offsetHeight -
            chatWindowElement.scrollTop <=
          0;
      }
      lastScrollTop = chatWindowElement.scrollTop;
    }}
  >
    {#each messages as message, index (index)}
      <Message {...message} />
    {/each}
  </div>
  <textarea
    type="text"
    class="message-input container"
    placeholder="Message"
    maxlength="300"
    rows={Math.round((messageTextHeight - 34) / 24)}
    bind:value={messageInputElementText}
    on:keydown={function (event) {
      if (event.key === "Shift") {
        shiftKeyDown = true;
      }
      event.key === "Enter" && !shiftKeyDown && handleMessage(this.value);
    }}
    on:keyup={function (event) {
      if (event.key === "Shift") {
        shiftKeyDown = false;
      }
      if (event.key === "Enter" && !shiftKeyDown) {
        messageInputElement.value = "";
        messageInputElementText = "";
      }
    }}
    bind:this={messageInputElement}
  />
  <div class="message-input-span-container unselectable">
    <span class="message-input container" bind:offsetHeight={messageTextHeight}>
      {messageInputElementText}
    </span>
  </div>
</div>

<style lang="scss">
  .chat-window-container {
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .chat-window {
    grid-area: list;
    overflow-y: scroll;
    display: flex;
    flex-direction: column;
    height: 100%;
    max-width: 100%;
    gap: 0.5rem;
    padding: 0 0.5rem;
  }

  .message-input-span-container {
    display: grid;
    position: absolute;
    height: min-content;
    z-index: -100;
    margin-right: 1rem;
    opacity: 0;
  }

  .message-input {
    text-align: left;
    overflow-x: auto;
    overflow-wrap: break-word;
    resize: none;
    white-space: pre-wrap;
    min-height: 1.5rem;
    max-height: 10rem;
    -ms-overflow-style: none; /* IE and Edge */
    scrollbar-width: none; /* Firefox */
  }
  .message-input::-webkit-scrollbar {
    display: none;
  }
</style>
