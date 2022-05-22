<script>
  import { eventTypes, websocket, user } from "../stores";

  let usernameTextWidth = 0;
  let displayUsername = $user.name;

  const handleUsernameChange = (displayUsername) => {
    if ($user.name === displayUsername) {
      return;
    }

    user.set({ ...$user, name: displayUsername });
    $websocket.send(
      JSON.stringify({
        type: $eventTypes.NAME_CHANGE,
        user: { name: displayUsername },
      })
    );
  };

  $websocket.addEventListener("message", (event) => {
    const data = JSON.parse(event.data);
    if (![$eventTypes.USER_DETAILS].includes(data.type)) {
      return;
    }

    user.set(data.user);
    displayUsername = data.user.name;
  });
</script>

<div class="username">
  <span
    style="position: absolute; opacity: 0; z-index: -100;"
    class="username-input unselectable"
    bind:offsetWidth={usernameTextWidth}>{displayUsername}</span
  >
  <input
    class="username-input container"
    placeholder="Username"
    maxlength="20"
    bind:value={displayUsername}
    style="width: {displayUsername === ''
      ? 190
      : usernameTextWidth}px; color: {$user.color};"
    on:blur={() => handleUsernameChange(displayUsername)}
  />
  <h2 style="color: {$user.color};">#{$user.id}</h2>
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
      overflow-x: hidden;
      text-align: center;
      padding: 0 0.5rem;
      margin: 0;
    }
  }
</style>
