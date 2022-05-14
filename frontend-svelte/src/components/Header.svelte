<script>
  import { websocket } from "../stores";

  let numberOfUsersOnline = 2;
  let userIdentificationNumber = 5123;
  let userName = "Murtada";

  function clickHeader() {
    console.log("Header clicked");
    $websocket.send(JSON.stringify({ action: "Header" }));
  }
</script>

<div class="header" on:click={clickHeader}>
  <h2>Users online: {numberOfUsersOnline}</h2>
  <h2>#{userIdentificationNumber}</h2>
  <h2>{userName}</h2>
</div>

<style lang="scss">
  .header {
    display: flex;
  }
</style>
