<script>
  import { websocket } from "./stores";
  import Header from "./components/Header.svelte";

  function buttonClicked() {
    console.log("Button clicked");
    $websocket.send(JSON.stringify({ action: "Button clicked" }));
  }
</script>

<Header />
<button on:click={buttonClicked}>Test</button>

<style lang="scss">
</style>
