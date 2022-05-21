<script>
  import { websocket } from "../stores";

  let numberOfUsersOnline = 0;

  $websocket.addEventListener("message", (event) => {
    const data = JSON.parse(event.data);
    if (!["user"].includes(data.type)) {
      return;
    }

    numberOfUsersOnline = data.count;
  });
</script>

<h2 class="user-count">Users online: {numberOfUsersOnline}</h2>

<style>
  .user-count {
    font-size: 2rem;
  }
</style>
