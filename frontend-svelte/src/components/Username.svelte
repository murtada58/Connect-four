<script>
  import { websocket, userId, username, usernameColor } from "../stores";

  let usernameTextWidth = 0;
  let displayUsername = $username;

  const handleUsernameChange = (displayUsername) => {
    console.log("handling username change: ", displayUsername);
    if ($username === displayUsername) {
      return;
    }

    username.set(displayUsername);
    $websocket.send(
      JSON.stringify({
        action: "nameChange",
        username: displayUsername,
      })
    );
  };

  $websocket.addEventListener("message", (event) => {
    const data = JSON.parse(event.data);
    if (!["username"].includes(data.type)) {
      return;
    }

    userId.set(data.userId);
    username.set(data.username);
    usernameColor.set(data.usernameColor);
    displayUsername = data.username;
  });
</script>

<div class="username">
  <span
    style="position: absolute; opacity: 0;"
    class="username-input unselectable"
    bind:offsetWidth={usernameTextWidth}>{displayUsername}</span
  >
  <input
    class="username-input container"
    placeholder="Username"
    bind:value={displayUsername}
    style="width: {displayUsername === ''
      ? 190
      : usernameTextWidth}px; color: {$usernameColor};"
    on:blur={() => handleUsernameChange(displayUsername)}
  />
  <h2 style="color: {$usernameColor};">#{$userId}</h2>
</div>

<style lang="scss">
  .username {
    display: flex;
    align-items: center;

    .username-input,
    h2 {
      display: inline-block;
      font-size: 2rem;
    }

    .username-input {
      border-radius: 0.5rem;
      font-size: 2rem;
      max-width: 25rem;
      overflow-x: hidden;
      text-align: center;
      padding: 0 0.5rem;
      margin: 0;
    }
  }
</style>
