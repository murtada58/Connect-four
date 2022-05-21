<script>
  import { onMount } from "svelte";

  import { userId } from "../stores";
  export let messageUserId;
  export let messageUsername;
  export let messageUsernameColor;
  export let messageText;
  export let messageTime;

  const messageFromCurrentUser = messageUserId === $userId;
</script>

<div
  class="message-container container {messageFromCurrentUser
    ? 'current-user'
    : 'not-current-user'}"
>
  <div
    class="message-name"
    style="color: {messageUsernameColor}; text-align: {messageFromCurrentUser
      ? 'right'
      : 'left'};"
  >
    {`${messageUsername}#${messageUserId}`}
  </div>
  <p class="message">
    {messageText}
  </p>
  <div
    class="message-time"
    style="text-align: {messageFromCurrentUser ? 'right' : 'left'};"
  >
    {messageTime}
  </div>
</div>

<style lang="scss">
  .current-user {
    align-self: flex-end;
    margin: 0.5rem 3.5rem;
    margin-right: 1rem;
  }

  .not-current-user {
    align-self: flex-start;
    margin: 0.5rem;
    margin-right: 4rem;
  }

  .message-container {
    display: grid;
    grid-template-areas:
      "name"
      "message"
      "time";

    height: min-content;

    .message-name {
      grid-area: name;
      overflow-x: auto;
      overflow-wrap: break-word;
    }

    .message {
      grid-area: message;
      text-align: left;
      white-space: pre-wrap;
      overflow-x: auto;
      overflow-wrap: break-word;
    }

    .message-time {
      grid-area: time;
      font-size: 1rem;
      color: #777777;
    }
  }
</style>
