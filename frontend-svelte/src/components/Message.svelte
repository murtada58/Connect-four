<script>
  import { user } from "../stores";
  export let message;

  const isMessageFromCurrentUser = message.user.id === $user.id;
</script>

<div
  class="message-container container {isMessageFromCurrentUser
    ? 'current-user'
    : 'not-current-user'}"
>
  <div
    class="message-name"
    style="color: {message.user.color}; text-align: {isMessageFromCurrentUser
      ? 'right'
      : 'left'};"
  >
    {`${message.user.name}#${message.user.id}`}
  </div>
  <p class="message">
    {message.text}
  </p>
  <div
    class="message-time"
    style="text-align: {isMessageFromCurrentUser ? 'right' : 'left'};"
  >
    {message.time}
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
