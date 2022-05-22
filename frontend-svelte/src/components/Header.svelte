<script>
  import UserCount from "./UserCount.svelte";
  import Username from "./Username.svelte";

  let innerWidth = 0;
  let innerHeight = 0;
</script>

<svelte:window bind:innerWidth bind:innerHeight />

<div class="header container">
  <div class="right-header-section">
    <UserCount />
  </div>
  {#if innerWidth > 800}
    <div class="left-header-section">
      <Username />
    </div>
  {/if}
</div>

<style lang="scss">
  .header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
</style>
